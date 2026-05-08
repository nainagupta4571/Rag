import os
from dotenv import load_dotenv
from src.vectorstore import FaissVectorStore
from langchain_groq import ChatGroq

load_dotenv()

class RAGSearch:
    def __init__(
        self,
        persist_dir: str = "faiss_store",
        embedding_model: str = "BAAI/bge-small-en-v1.5",
        llm_model: str = "llama-3.1-8b-instant"
    ):
        self.vectorstore = FaissVectorStore(persist_dir, embedding_model)

        faiss_path = os.path.join(persist_dir, "faiss.index")
        meta_path = os.path.join(persist_dir, "metadata.pkl")

        if not (os.path.exists(faiss_path) and os.path.exists(meta_path)):
            from src.data_loader import load_all_documents  
            docs = load_all_documents("data")
            self.vectorstore.build_from_documents(docs)
        else:
            self.vectorstore.load()

        groq_api_key = os.getenv("GROQ_API_KEY")

        self.llm = ChatGroq(
        groq_api_key=groq_api_key,
        model_name=llm_model,
        temperature=0  
    )

        print(f"[INFO] Groq LLM initialized: {llm_model}")

    def search_and_summarize(self, query: str, top_k: int = 5) -> str:
        results = self.vectorstore.query(query, top_k=top_k)
       
        texts = [r["metadata"].get("text", "") for r in results if r["metadata"]]
        context = "\n\n".join(texts)
        
        if not context:
            return "No relevant documents found."

        prompt = f"""
You are a resume assistant.

Answer ONLY using the resume context below.

IMPORTANT:
- Do not guess
- Do not invent information
- If answer not found, say:
  "Information not available in resume."


Question: {query}

Context:
{context}

Answer:
"""

        # ✅ FIXED
        response = self.llm.invoke([
    {"role": "user", "content": prompt}
])

        return response.content



    def ats_analysis(self, job_description: str):

        results = self.vectorstore.query("", top_k=10)
        texts = [r["metadata"].get("text", "") for r in results]
        resume_text = " ".join(texts)

        # Only LLM based clean output
        final_output = self.generate_ai_suggestions(resume_text, job_description)

        return final_output


    def generate_ai_suggestions(self, resume_text, job_description):

        prompt = f"""
    You are an ATS system.

    Analyze the resume vs job description and return STRICTLY in this format:

    ATS Score: <number>%

    Matched Skills: <comma separated>

    Missing Skills: <comma separated>

    Suggestions:
    - short bullet points (max 5)

    IMPORTANT RULES:
    - Do NOT rewrite resume
    - Do NOT explain
    - Keep output short and crisp
    - No paragraphs

    Resume:
    {resume_text}

    Job Description:
    {job_description}
    """

        response = self.llm.invoke([
            {"role": "user", "content": prompt}
        ])

        return response.content
    
    def generate_improved_resume(self, job_description: str):
        results = self.vectorstore.query("", top_k=10)

        texts = [r["metadata"].get("text", "") for r in results]
        resume_text = " ".join(texts)

        prompt = f"""
    Improve the resume based on the job description.

    Job Description:
    {job_description}

    Resume:
    {resume_text}

    Give a clean, ATS-optimized improved resume.
    """

        response = self.llm.invoke([
            {"role": "user", "content": prompt}
        ])

        return response.content

if __name__ == "__main__":
    rag_search = RAGSearch()
    query = "What is my degree?"
    summary = rag_search.search_and_summarize(query, top_k=3)
    
 
    print("Answer:", summary)