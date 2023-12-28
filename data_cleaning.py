import os
import PyPDF2
from pdfminer.high_level import extract_text

pdf_dir = r"C:\Users\ADMIN\Desktop\rp"
pdf_files = [f for f in os.listdir(pdf_dir) if f.endswith('.pdf')]

# Initialize an empty string to store the combined text
combined_text = ""

# Process PDFs using PyPDF2 (PdfReader)
for pdf_file in pdf_files:
    pdf_path = os.path.join(pdf_dir, pdf_file)
    
    # Open the PDF file using PdfReader
    with open(pdf_path, 'rb') as pdf:
        pdf_reader = PyPDF2.PdfReader(pdf)

        # Process each page of the PDF if needed
        for page in pdf_reader.pages:
            text = page.extract_text()
            # Append the differentiator and text to the combined_text
            combined_text += f"--- {pdf_file} ---\n{text}\n"

# Process PDFs using pdfminer
for pdf_file in pdf_files:
    pdf_path = os.path.join(pdf_dir, pdf_file)
    
    # Extract text from the PDF using pdfminer
    text = extract_text(pdf_path)
    # Append the differentiator and text to the combined_text
    combined_text += f"--- {pdf_file} ---\n{text}\n"

# Save to a text file with differentiators
with open("Sample.txt", "w", encoding="utf-8") as text_file:
    text_file.write(combined_text)


