"""
parser.py

Handles reading resumes and job descriptions.

Supported formats:
- PDF
- DOCX
- TXT
"""

import os
import fitz
from docx import Document


def extract_txt_text(file_path):
    """
    Reads a TXT resume and returns its text.
    """

    try:
        with open(file_path, "r", encoding="utf-8") as file:
            return file.read()

    except Exception as error:
        print(f"Error reading TXT file: {error}")
        return ""

def extract_pdf_text(file_path):
        """
        Reads a PDF resume and returns its text.
        """

        try:
            text = ""

            pdf = fitz.open(file_path)

            for page in pdf:
                text += page.get_text()

            pdf.close()

            return text

        except Exception as error:
            print(f"Error reading PDF file: {error}")
            return ""
def extract_docx_text(file_path):
    """
    Reads a DOCX resume and returns its text.
    """

    try:
        document = Document(file_path)

        text = ""

        for paragraph in document.paragraphs:
            text += paragraph.text + "\n"

        return text

    except Exception as error:
        print(f"Error reading DOCX file: {error}")
        return ""
def load_job_description(file_path):
    """
    Reads the Job Description file and returns its text.
    Supports TXT format.
    """

    try:
        with open(file_path, "r", encoding="utf-8") as file:
            return file.read()

    except Exception as error:
        print(f"Error reading Job Description: {error}")
        return ""
def load_all_resumes(folder_path):
    """
    Reads all resumes from the given folder.

    Supports:
    - PDF
    - DOCX
    - TXT

    Returns:
        A list of dictionaries containing:
        filename and extracted text.
    """

    resumes = []

    try:

        for filename in os.listdir(folder_path):

            file_path = os.path.join(folder_path, filename)

            if filename.lower().endswith(".pdf"):
                text = extract_pdf_text(file_path)

            elif filename.lower().endswith(".docx"):
                text = extract_docx_text(file_path)

            elif filename.lower().endswith(".txt"):
                text = extract_txt_text(file_path)

            else:
                continue

            resumes.append({
                "filename": filename,
                "text": text
            })

        return resumes

    except Exception as error:
        print(f"Error loading resumes: {error}")
        return []