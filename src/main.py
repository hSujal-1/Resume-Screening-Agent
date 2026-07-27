from parser import load_job_description, load_all_resumes
from scorer import calculate_similarity


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

        results.append({
            "filename": resume["filename"],
            "score": score
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
        print(f"{index}. {result['filename']} -> {result['score']:.4f}")


if __name__ == "__main__":
    main()