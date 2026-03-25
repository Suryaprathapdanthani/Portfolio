import fitz

doc = fitz.open("CV_202601021051302117_12310678 (2).pdf")
text = ""
for page in doc:
    text += page.get_text() + "\n"

print(text)
