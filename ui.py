import streamlit as st
import tempfile
import os

from src.search import RAGSearch
from src.data_loader import load_all_documents
from src.vectorstore import FaissVectorStore
from src.utils import save_as_txt, save_as_pdf

st.set_page_config(page_title="AI Resume Analyzer", layout="wide")

st.title("🚀 AI Resume Analyzer & ATS Optimizer")

# Initialize RAG
@st.cache_resource
def load_rag():
    return RAGSearch("faiss_store")

rag = load_rag()

# Sidebar
st.sidebar.header("Upload Files")

resume_file = st.sidebar.file_uploader("Upload Resume (PDF)", type=["pdf"])
jd_file = st.sidebar.file_uploader("Upload Job Description (TXT)", type=["txt"])

# Save uploaded files
if resume_file:
    with open("data/resume.pdf", "wb") as f:
        f.write(resume_file.read())

    # rebuild vector store
    docs = load_all_documents("data")
    store = FaissVectorStore("faiss_store")
    store.build_from_documents(docs)
    store.save()

    st.sidebar.success("Resume uploaded & indexed ✅")

jd_text = ""

if jd_file:
    jd_text = jd_file.read().decode("utf-8")
    st.sidebar.success("JD uploaded ✅")

# MAIN TABS
tab1, tab2 = st.tabs(["💬 Ask Questions", "📊 ATS Score"])

# ================= CHAT =================
with tab1:
    st.header("Ask Questions from Resume")

    query = st.text_input("Ask something about your resume:")

    if st.button("Get Answer"):
        if query:
            with st.spinner("Thinking..."):
                answer = rag.search_and_summarize(query)
            st.success(answer)
        else:
            st.warning("Please enter a question")

# ================= ATS =================

with tab2:
    st.header("ATS Score Analyzer")

    jd_manual = st.text_area("Or paste Job Description")

    jd_final = jd_text if jd_text else jd_manual

    if "result" not in st.session_state:
        st.session_state.result = None

    if "improved" not in st.session_state:
        st.session_state.improved = None

    # STEP 1 Analyze ATS
    if st.button("Analyze ATS"):
        if not jd_final:
            st.warning("Upload or paste Job Description!")
        else:
            with st.spinner("Analyzing..."):
                st.session_state.result = rag.ats_analysis(jd_final)

    # SHOW ATS RESULT
    if st.session_state.result:
        result = st.session_state.result

        st.markdown("### 📊 ATS Result")
        st.text(result)

        # STEP 2 Generate Resume button
        if st.button("Generate Improved Resume"):
            with st.spinner("Generating Resume..."):
                st.session_state.improved = rag.generate_improved_resume(jd_final)

    # SHOW IMPROVED RESUME
    if st.session_state.improved:
        improved = st.session_state.improved

        st.markdown("### ✨ Improved Resume")
        st.write(improved)

        format_type = st.radio("Download Format", ["TXT", "PDF"])

        if format_type == "TXT":
            file_path = save_as_txt(improved)
            mime = "text/plain"
            file_name = "resume.txt"
        else:
            file_path = save_as_pdf(improved)
            mime = "application/pdf"
            file_name = "resume.pdf"

        with open(file_path, "rb") as f:
            st.download_button(
                "⬇️ Download Resume",
                data=f,
                file_name=file_name,
                mime=mime
            )