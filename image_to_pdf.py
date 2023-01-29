import img2pdf

# Open the image file

with open("image.jpg", "rb") as image:
    # Convert the image to a pdf
    pdf_bytes = img2pdf.convert(image.read())
    
# Save the pdf to a file
with open("image.pdf", "wb") as pdf:
    pdf.write(pdf_bytes)
    