# 🚀 AI Resume Analyzer & ATS Optimizer

An AI-powered Resume Analyzer that helps job seekers evaluate and optimize their resumes against a Job Description (JD). The application leverages **Retrieval-Augmented Generation (RAG)** with **FAISS**, **LangChain**, and **Groq Llama 3.1** to answer resume-related questions, calculate ATS compatibility, and generate an improved ATS-friendly resume.

## 🌐 Live Demo

**Application:** [AI Resume Analyzer Live Demo](https://5xfnkxyfabx9jrtvrpf8xh.streamlit.app/)

## 🎥 Demo Video

Add your demo video link here:

```
https://your-demo-video-link
```

---

## ✨ Features

* 📄 Upload your resume (PDF)
* 💬 Ask questions about your resume using AI
* 📊 ATS Score Analysis based on a Job Description
* ✅ Matched Skills Detection
* ❌ Missing Skills Identification
* 💡 Personalized Resume Improvement Suggestions
* ✨ Generate an ATS-Optimized Resume
* 📥 Download the generated resume in **PDF** or **TXT** format
* ⚡ Fast semantic search using FAISS Vector Database

---

## 🛠️ Tech Stack

**Frontend**

* Streamlit

**Backend**

* Python

**AI & LLM**

* LangChain
* Groq (Llama 3.1)
* Sentence Transformers (BAAI/bge-small-en-v1.5)

**Vector Database**

* FAISS

**Libraries**

* PyPDF
* python-dotenv
* ReportLab

---

## 📂 Project Structure

```
AI-Resume-Analyzer/
│
├── data/
├── faiss_store/
├── src/
│   ├── ats.py
│   ├── data_loader.py
│   ├── embedding.py
│   ├── search.py
│   ├── utils.py
│   └── vectorstore.py
│
├── ui.py
├── requirements.txt
├── README.md
└── .env
```

---

## ⚙️ Installation

Clone the repository

```bash
git clone <your-repository-url>
cd AI-Resume-Analyzer
```

Create a virtual environment

```bash
python -m venv venv
```

Activate the environment

**Windows**

```bash
venv\Scripts\activate
```

**Mac/Linux**

```bash
source venv/bin/activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

Create a `.env` file

```env
GROQ_API_KEY=your_groq_api_key
```

Run the application

```bash
streamlit run ui.py
```

---

## 📖 How It Works

1. Upload your resume (PDF).
2. The resume is parsed and converted into vector embeddings.
3. Embeddings are stored in a FAISS vector database.
4. Ask questions about your resume using RAG.
5. Upload or paste a Job Description.
6. Receive:

   * ATS Score
   * Matching Skills
   * Missing Skills
   * Improvement Suggestions
7. Generate and download an ATS-optimized resume.

---

## 📸 Screenshots

Add screenshots of:

* Home Page
* Resume Upload
* AI Chat
* ATS Analysis
* Generated Resume

---

## 🔮 Future Enhancements

* DOCX Resume Support
* Multi-Resume Comparison
* Chat History
* Authentication
* Multiple LLM Support
* Resume Templates
* Interview Question Generator

---

## 👩‍💻 Author

**Naina Gupta**

LinkedIn: *(Add your LinkedIn URL)*

GitHub: *(Add your GitHub Profile URL)*

---

## 📄 License

This project is licensed under the MIT License.
