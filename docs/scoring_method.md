# Resume Screening Agent - Scoring Method

## Overview

The Resume Screening Agent ranks candidates using a weighted scoring system. The objective is to identify resumes that best match the provided Job Description based on semantic relevance, technical skills, and work experience.

---

## Scoring Components

### 1. AI Semantic Similarity (70%)

- Uses the SentenceTransformer model (`all-MiniLM-L6-v2`)
- Converts both the Job Description and Resume into embeddings.
- Calculates cosine similarity between the two embeddings.

Weight: **70%**

---

### 2. Skill Match (20%)

The system extracts technical skills from:

- Job Description
- Resume

It calculates:

Skill Match Score = Matching Skills / Total Job Description Skills

Weight: **20%**

---

### 3. Experience Bonus (10%)

The system extracts years of experience from the resume.

Bonus is assigned as follows:

| Experience | Bonus |
|------------|-------|
| 5+ Years | 1.0 |
| 3–4 Years | 0.8 |
| 1–2 Years | 0.6 |
| Less than 1 Year | 0.3 |
| Not Found | 0.0 |

Weight: **10%**

---

## Final Score Formula

Final Score =
(AI Similarity × 0.70)
+
(Skill Match × 0.20)
+
(Experience Bonus × 0.10)

---

## Candidate Ranking

Candidates are sorted in descending order based on the Final Score.

The candidate with the highest Final Score receives Rank 1.

---

## Output

The system generates:

- Console ranking
- ranked_resumes.csv
- ranked_resumes.json

These outputs include:

- Candidate Name
- Email
- Skills
- Experience
- Education
- Final Score
- Ranking Reason