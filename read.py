import pytesseract 
from PIL import Image
from pdf2image import convert_from_path

pages=convert_from_path("text/asme-journal-article-template.pdf")
text= ""
for page in pages:
    text += pytesseract.image_to_string(page)

print(text)



