from parser import load_job_description, load_all_resumes


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

if __name__ == "__main__":
    main()