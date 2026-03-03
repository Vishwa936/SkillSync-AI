from preprocess import clean_text
from similarity import calculate_similarity

if __name__ == "__main__":
    resume = """
    Python developer with experience in Django, REST APIs, PostgreSQL,
    machine learning, and data analysis.
    """

    job_description = """
    Looking for a Python developer with experience in Django, REST APIs,
    PostgreSQL, machine learning, and data analysis.
    """

    resume_clean = clean_text(resume)
    job_clean = clean_text(job_description)

    score = calculate_similarity(resume_clean, job_clean)

    print(f"Match Score: {score}%")