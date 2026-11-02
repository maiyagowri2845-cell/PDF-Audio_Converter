import pymupdf

def extract_text_from_pdf(pdf_path):
    extracted_text = ""
    with pymupdf.open(pdf_path) as pdf:
        for page in pdf:
            page_text = page.get_text("text")
            extracted_text += page_text + "\n"

    return extracted_text
