import PyPDF2
import docx

def extract_text(file_path):
    text = ""

    ext = file_path.split(".")[-1].lower()

    if ext == "txt":
        with open(file_path, "r", encoding="utf-8") as f:
            text = f.read()

    elif ext == "pdf":
        reader = PyPDF2.PdfReader(file_path)
        for page in reader.pages:
            text += page.extract_text() or ""

    elif ext == "docx":
        doc = docx.Document(file_path)
        for para in doc.paragraphs:
            text += para.text + "\n"

    return text