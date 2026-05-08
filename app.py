
from src.data_loader import load_all_documents
from src.vectorstore import FaissVectorStore
from src.search import RAGSearch
from src.ats import load_jd
import os

if __name__ == "__main__":

    # Build vector store only once
    if not os.path.exists("faiss_store/faiss.index"):
        docs = load_all_documents("data")
        store = FaissVectorStore("faiss_store")
        store.build_from_documents(docs)
        store.save()

    rag_search = RAGSearch("faiss_store")

    # ✅ LOOP SHOULD BE INSIDE MAIN
    while True:
        print("\n1. Ask Question")
        print("2. ATS Score")
        print("3. Exit")

        choice = input("Choose option: ")

        if choice == "1":
            query = input("Ask your question: ")
            answer = rag_search.search_and_summarize(query, top_k=3)
            print("Answer:", answer)

        elif choice == "2":
            jd = load_jd()

            if not jd:
                print("JD file not found or empty!")
                continue   # 🔥 IMPORTANT

            result = rag_search.ats_analysis(jd)

          
            print("\n", result)

            

        elif choice == "3":
            break