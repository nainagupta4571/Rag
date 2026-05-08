from sentence_transformers import SentenceTransformer, util

model = SentenceTransformer("all-MiniLM-L6-v2")


def load_jd():
    try:
        with open("data/job_description.txt", "r", encoding="utf-8") as f:
            return f.read()
    except:
        return None