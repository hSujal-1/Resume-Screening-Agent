"""
scorer.py

Handles resume scoring using Sentence Transformers.
"""
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity


# Load the pre-trained Sentence Transformer model
print("Loading AI model...")
model = SentenceTransformer("all-MiniLM-L6-v2")
print("AI model loaded successfully!")
def generate_embedding(text):
    """
    Converts text into an embedding (vector).
    """
    try:
        embedding = model.encode(text)
        return embedding

    except Exception as error:
        print(f"Error generating embedding: {error}")
        return None
def calculate_similarity(job_description, resume_text):
    try:
        print("Generating JD embedding...")
        jd_embedding = generate_embedding(job_description)

        print("Generating Resume embedding...")
        resume_embedding = generate_embedding(resume_text)

        print("Calculating similarity...")
        similarity = cosine_similarity(
            [jd_embedding],
            [resume_embedding]
        )[0][0]

        print("Similarity calculated!")

        return float(similarity)

    except Exception as error:
        print(f"Error calculating similarity: {error}")
        return 0.0

def calculate_skill_match(jd_skills, resume_skills):
        """
        Calculate the percentage of Job Description skills
        that are present in the resume.
        """

        if not jd_skills:
            return 0.0

        jd_skill_set = {skill.lower() for skill in jd_skills}
        resume_skill_set = {skill.lower() for skill in resume_skills}

        matched_skills = jd_skill_set.intersection(resume_skill_set)

        skill_match_score = len(matched_skills) / len(jd_skill_set)

        return skill_match_score
import re


def calculate_experience_bonus(experience_text):
    """
    Calculate an experience bonus score based on
    the number of years of experience.
    """

    match = re.search(r"\d+", experience_text)

    if not match:
        return 0.0

    years = int(match.group())

    if years >= 5:
        return 1.0

    elif years >= 3:
        return 0.8

    elif years >= 1:
        return 0.6

    else:
        return 0.3
def calculate_final_score(similarity_score, skill_match_score, experience_bonus):
    """
    Calculate the final weighted score for a candidate.
    """

    final_score = (
        (similarity_score * 0.70) +
        (skill_match_score * 0.20) +
        (experience_bonus * 0.10)
    )

    return round(final_score, 4)