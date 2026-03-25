from pypdf import PdfReader

reader = PdfReader("CV_202601021051302117_12310678 (2).pdf")
text = ""
for page in reader.pages:
    text += page.extract_text() + "\n"

print(text)
