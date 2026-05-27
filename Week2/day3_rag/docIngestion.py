from pypdf import PdfReader
import os
reader = PdfReader("sample.pdf")

text = ""

for page in reader.pages:
    text += page.extract_text()

print(text)