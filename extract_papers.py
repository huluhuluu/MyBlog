import pdfplumber
import sys

def extract_pdf_text(pdf_path, max_pages=15):
    """Extract text from PDF, focusing on first few pages for abstract/intro"""
    try:
        with pdfplumber.open(pdf_path) as pdf:
            text = ""
            for i, page in enumerate(pdf.pages[:max_pages]):
                page_text = page.extract_text()
                if page_text:
                    text += f"\n--- Page {i+1} ---\n{page_text}"
            return text
    except Exception as e:
        return f"Error reading {pdf_path}: {e}"

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python extract_papers.py <pdf_path>")
        sys.exit(1)
    
    pdf_path = sys.argv[1]
    print(extract_pdf_text(pdf_path))
