

# from fpdf import FPDF

# def save_as_txt(content):
#     file_path = "improved_resume.txt"

#     with open(file_path, "w", encoding="utf-8") as f:
#         f.write(content)

#     return file_path


# def save_as_pdf(content):
#     file_path = "improved_resume.pdf"

#     content = content.replace("–", "-")
#     content = content.replace("—", "-")
#     content = content.replace("•", "-")
#     content = content.replace("’", "'")

#     pdf = FPDF()
#     pdf.add_page()
#     pdf.set_auto_page_break(auto=True, margin=15)
#     pdf.set_font("Helvetica", size=11)

#     lines = content.split("\n")

#     for line in lines:
#         line = line.strip()

#         # blank line
#         if not line:
#             pdf.ln(5)
#             continue

#         # break extra long words
#         while len(line) > 90:
#             pdf.multi_cell(0, 8, line[:90])
#             line = line[90:]

#         pdf.multi_cell(0, 8, line)

#     pdf.output(file_path)
#     return file_path

from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet

def save_as_txt(content):
    file_path = "improved_resume.txt"

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)

    return file_path


def save_as_pdf(content):
    file_path = "improved_resume.pdf"

    doc = SimpleDocTemplate(file_path)
    styles = getSampleStyleSheet()
    story = []

    for line in content.split("\n"):
        if line.strip():
            story.append(Paragraph(line, styles["Normal"]))
            story.append(Spacer(1, 6))

    doc.build(story)

    return file_path