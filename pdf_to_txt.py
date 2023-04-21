import PyPDF2
import os


def extraction(pdf_name: str) -> str:
    # Look for file in the same directory
    pdf_path = os.path.join(os.path.dirname(__file__), pdf_name)
    with open(pdf_path, 'rb') as pdf:
        reader = PyPDF2.PdfReader(pdf, strict=False)

        out_str = str()

        for page in reader.pages:
            content = page.extract_text()
            out_str += content
            return out_str


filename = f"{input('Input filename: ')}.pdf"
pdftxt = extraction(filename)
print(pdftxt)
