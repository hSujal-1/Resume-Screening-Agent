"""
parser.py

Handles reading resumes and job descriptions.

Supported formats:
- PDF
- DOCX
- TXT
"""

import os
import re
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


def extract_name(text):
    """
    Extract the candidate's name.

    Assumption:
    The first non-empty line of the resume is the candidate's name.
    """

    lines = text.splitlines()

    for line in lines:
        line = line.strip()

        if line:
            return line

    return "Not Found"


def extract_email(text):
    """
    Extract the candidate's email address using Regular Expressions.
    """

    email_pattern = r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}"

    match = re.search(email_pattern, text)

    if match:
        return match.group()

    return "Not Found"
def extract_skills(text):
    """
    Extract skills from the resume using a predefined skill list.
    """

    skill_database = [
        "Python",
        "SQL",
        "Power BI",
        "Excel",
        "Tableau",
        "Pandas",
        "NumPy",
        "Machine Learning",
        "Deep Learning",
        "Data Analysis",
        "Data Analytics",
        "Statistics",
        "Git",
        "GitHub",
        "Snowflake",
        "Databricks",
        "MySQL",
        "PostgreSQL",
        "MongoDB",
        "AWS",
        "Azure",
        "Docker",
        "Linux",
        "C",
        "C++",
        "Java",
        "JavaScript",
        "HTML",
        "CSS"
    ]

    found_skills = []

    for skill in skill_database:

        pattern = r"\b" + re.escape(skill) + r"\b"

        if re.search(pattern, text, re.IGNORECASE):
            found_skills.append(skill)

    return found_skills
def extract_experience(text):
    """
    Extract years of experience from the resume.
    """

    experience_pattern = r"\b\d+\+?\s*(?:years?|yrs?)\b"

    match = re.search(
        experience_pattern,
        text,
        re.IGNORECASE
    )

    if match:
        return match.group()

    return "Not Found"
def extract_education(text):
    """
    Extract the candidate's highest education qualification.
    """

    education_list = [
        "Bachelor of Engineering",
        "Bachelor of Technology",
        "Master of Technology",
        "Master of Engineering",
        "Bachelor of Science",
        "Master of Science",
        "Bachelor of Computer Applications",
        "Master of Computer Applications",
        "B.E",
        "BE",
        "B.Tech",
        "M.Tech",
        "BSc",
        "MSc",
        "BCA",
        "MCA",
        "MBA",
        "PhD",
        "Diploma"
    ]

    text_lower = text.lower()

    for education in education_list:

        if education.lower() in text_lower:
            return education

    return "Not Found"