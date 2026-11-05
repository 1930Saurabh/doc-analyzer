from pypdf import PdfReader
from pypdf.errors import PdfReadError, FileNotDecryptedError
from docx import Document
from pathlib import Path
from docx.opc.exceptions import PackageNotFoundError

def extract_pdf_text(filename):
    try:
        reader = PdfReader(filename) 
        pdf_texts = [
        page.extract_text() or ""
        for page in reader.pages
    ]
        return "\n".join(pdf_texts)

    except FileNotFoundError: 
       print("PDF file not found")
       return ""
    except PdfReadError: 
       print("Unable to read PDF. File may be corrupted.")
       return ""
    except FileNotDecryptedError: 
       print("PDF is password protected")
       return ""

def extract_doc_text(filename):
    try:
        doc_reader = Document(filename)
        paragraph_texts = [
            paragraph.text or ""
            for paragraph in doc_reader.paragraphs 
        ]
        table_texts = [
            cell.text or ""
            for table in doc_reader.tables
            for row in table.rows
            for cell in row.cells
        ]

        all_texts = paragraph_texts + table_texts

        return "\n".join(all_texts) 

    except FileNotFoundError: 
           print("Doc file not found")
           return ""
    except PackageNotFoundError:
        print("Invalid or corrupted DOCX file")
        return ""

def extract_document(filename):
    path = Path(filename)
    extension = path.suffix.lower()
    if extension == ".pdf":
        return extract_pdf_text(filename)
    elif extension == ".docx":
        return extract_doc_text(filename)
    
    elif extension == ".txt":
        try:
            return path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            print("TXT file encoding is not UTF-8")
            return ""

        except OSError as e:
            print(f"Could not read TXT file: {e}")
            return ""
    else:
        print("Unsupported file type") 
        return ""




       

