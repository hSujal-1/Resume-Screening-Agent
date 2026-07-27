# 📄 Resume Screening Agent

An AI-powered Resume Screening Agent that automatically analyzes, scores, and ranks resumes against a given Job Description using Natural Language Processing (NLP) and semantic similarity.

The system extracts candidate information, compares resumes with the job description, calculates an intelligent score, ranks candidates, and exports the results in CSV and JSON formats.

---

##  Features

-  Parse resumes in **TXT**, **PDF**, and **DOCX** formats
-  AI-powered semantic similarity using Sentence Transformers
-  Extract candidate information
  - Name
  - Email
  - Skills
  - Experience
  - Education
-  Intelligent candidate scoring
-  Automatic resume ranking
-  Export ranked candidates to CSV and JSON
-  Easy to use and extend

---

##  Tech Stack

| Technology | Purpose |
|------------|---------|
| Python | Core Programming Language |
| Sentence Transformers | AI Semantic Similarity |
| Scikit-learn | Cosine Similarity |
| PyMuPDF (fitz) | PDF Parsing |
| python-docx | DOCX Parsing |
| Regex | Information Extraction |
| JSON | Output Export |
| CSV | Output Export |

---

##  Project Structure

```
Resume-Screening-Agent/
│
├── data/
│   ├── jd/
│   │   └── job_description.txt
│   │
│   ├── resumes/
│   │   ├── resume_1.txt
│   │   ├── resume_2.txt
│   │   ├── resume_3.txt
│   │   └── resume_4.txt
│   │
│   └── output/
│       ├── ranked_resumes.csv
│       └── ranked_resumes.json
│
├── docs/
│   └── scoring_method.md
│
├── src/
│   ├── main.py
│   ├── parser.py
│   ├── scorer.py
│   └── exporter.py
│
├── requirements.txt
├── README.md
└── .gitignore
```

---

#  Installation

## 1. Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/Resume-Screening-Agent.git
```

---

## 2. Navigate to the Project

```bash
cd Resume-Screening-Agent
```

---

## 3. Create Virtual Environment

Windows

```bash
python -m venv .venv
```

Activate

```bash
.venv\Scripts\activate
```

---

## 4. Install Dependencies

```bash
pip install -r requirements.txt
```

---

# ▶️ How to Run

Navigate to the source folder:

```bash
cd src
```

Run:

```bash
python main.py
```

The program will automatically:

- Read the Job Description
- Read every resume inside `data/resumes`
- Extract candidate details
- Calculate AI similarity
- Calculate skill match
- Calculate experience bonus
- Generate the final score
- Rank all candidates
- Export results

---

# Input

## Job Description

Place your Job Description here:

```
data/jd/job_description.txt
```

---

## Resumes

Place all resumes inside:

```
data/resumes/
```

Supported formats:

- TXT
- PDF
- DOCX

Example:

```
resume_1.txt
resume_2.pdf
resume_3.docx
resume_4.txt
```

---

# Output

The application generates:

Console Output

```
Rank #1

Resume:
resume_2.txt

Name:
Priya Verma

Email:
priya.verma@gmail.com

Skills:
Python, SQL, Power BI, Pandas

Experience:
5 Years

Education:
Master of Computer Applications

Score:
0.91

Reason:
Excellent overall match based on AI similarity, skills, and experience.
```

---

CSV Export

```
data/output/ranked_resumes.csv
```

Contains:

- Rank
- Resume
- Name
- Email
- Skills
- Experience
- Education
- Final Score
- Reason

---

JSON Export

```
data/output/ranked_resumes.json
```

Contains complete structured ranking information.

---

# Scoring Method

Final Score is calculated using:

| Component | Weight |
|-----------|--------|
| AI Semantic Similarity | 70% |
| Skill Match | 20% |
| Experience Bonus | 10% |

Formula:

```
Final Score =
(AI Similarity × 0.70)
+
(Skill Match × 0.20)
+
(Experience Bonus × 0.10)
```

Detailed explanation is available in:

```
docs/scoring_method.md
```

---

# Supported Resume Formats

- TXT
- PDF
- DOCX

---

# Future Improvements

- OCR support for scanned resumes
- Resume keyword highlighting
- Streamlit web interface
- REST API integration
- Advanced skill ontology
- LLM-powered resume summarization
- Cloud deployment
- ATS compatibility scoring

---

# Sample Workflow

```
Job Description
        │
        ▼
Read All Resumes
        │
        ▼
Extract Candidate Information
        │
        ▼
Generate AI Embeddings
        │
        ▼
Calculate Similarity
        │
        ▼
Calculate Skill Match
        │
        ▼
Calculate Experience Bonus
        │
        ▼
Generate Final Score
        │
        ▼
Rank Candidates
        │
        ▼
Export CSV & JSON
```

---

# Use Cases

- HR Resume Screening
- Campus Hiring
- Internship Shortlisting
- Initial Candidate Filtering
- ATS Prototype
- AI Recruitment Systems

---

# 👨‍💻 Author

**Sujal Jambotkar**

AI-Powered Data Analyst | Building Intelligent Automation Solutions

Passionate about transforming raw data into actionable insights using AI, Machine Learning, and Modern Data Analytics.

📧 Email: sujaljambotkar11@gmail.com

GitHub:
https://github.com/hSujal-1

LinkedIn:
https://www.linkedin.com/in/sujaljambotkar11

---

# ⭐ If you found this project useful, consider giving it a star!