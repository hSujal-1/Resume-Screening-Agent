from parser import (
    load_job_description,
    load_all_resumes,
    extract_name,
    extract_email,
    extract_skills,
    extract_experience,
    extract_education
)
from scorer import calculate_similarity
from exporter import export_to_csv, export_to_json


def main():

    # Load Job Description
    job_description = load_job_description("../data/jd/job_description.txt")

    print("=" * 50)
    print("JOB DESCRIPTION")
    print("=" * 50)
    print(job_description)

    # Load all resumes
    resumes = load_all_resumes("../data/resumes")

    print("\n" + "=" * 50)
    print("RESUMES")
    print("=" * 50)

    for resume in resumes:
        print(f"\nFilename: {resume['filename']}")
        print("-" * 50)
        print(resume["text"])

    # ---------------------------------
    # Calculate Similarity Scores
    # ---------------------------------

    print("\n" + "=" * 50)
    print("SIMILARITY SCORES")
    print("=" * 50)

    results = []

    for resume in resumes:
        score = calculate_similarity(
            job_description,
            resume["text"]
        )

        if score >= 0.80:
            reason = "High semantic similarity to the Job Description"
        elif score >= 0.60:
            reason = "Moderate semantic similarity to the Job Description"
        else:
            reason = "Low semantic similarity to the Job Description"

        results.append({
            "filename": resume["filename"],
            "score": score,
            "reason": reason
        })
        results = []

        for resume in resumes:

            name = extract_name(resume["text"])
            email = extract_email(resume["text"])
            skills = extract_skills(resume["text"])
            experience = extract_experience(resume["text"])
            education = extract_education(resume["text"])

            score = calculate_similarity(
                job_description,
                resume["text"]
            )

            if score >= 0.80:
                reason = "High semantic similarity to the Job Description"
            elif score >= 0.60:
                reason = "Moderate semantic similarity to the Job Description"
            else:
                reason = "Low semantic similarity to the Job Description"

            results.append({
                "filename": resume["filename"],
                "name": name,
                "email": email,
                "skills": skills,
                "experience": experience,
                "education": education,
                "score": score,
                "reason": reason
            })

    # ---------------------------------
    # Sort Results (Highest Score First)
    # ---------------------------------

    results.sort(
        key=lambda x: x["score"],
        reverse=True
    )

    # ---------------------------------
    # Print Final Ranking
    # ---------------------------------

    print("\n" + "=" * 50)
    print("RANKING")
    print("=" * 50)

    for index, result in enumerate(results, start=1):
        print(f"\nRank #{index}")
        print(f"Resume      : {result['filename']}")
        print(f"Name        : {result['name']}")
        print(f"Email       : {result['email']}")
        print(f"Skills      : {', '.join(result['skills']) if result['skills'] else 'Not Found'}")
        print(f"Experience  : {result['experience']}")
        print(f"Education   : {result['education']}")
        print(f"Score       : {result['score']:.4f}")
        print(f"Reason      : {result['reason']}")
        # ---------------------------------
        # Export Results
        # ---------------------------------

        export_to_csv(
            results,
            "../data/output/ranked_resumes.csv"
        )

        export_to_json(
            results,
            "../data/output/ranked_resumes.json"
        )


if __name__ == "__main__":
    main()