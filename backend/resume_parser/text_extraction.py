import fitz  # PyMuPDF

def extract_text_from_pdf(pdf_file):
    try:
        doc = fitz.open(stream=pdf_file.read(), filetype="pdf")
        text = " ".join([page.get_text("text") for page in doc])
        return text.strip()
    except Exception as e:
        return f"Error extracting text: {str(e)}"

# # Test with a sample PDF file
# with open("sample_resume.pdf", "rb") as f:
#     text = extract_text_from_pdf(f)
#     print(text)  # Should print extracted text, or an error message
