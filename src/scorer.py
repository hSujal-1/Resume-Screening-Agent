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