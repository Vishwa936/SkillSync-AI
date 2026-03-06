import re
from src.skills import TECH_SKILLS


def extract_keywords(text):

    text = text.lower()
    found_skills = set()

    for skill in TECH_SKILLS:
        pattern = r"\b" + re.escape(skill) + r"\b"

        if re.search(pattern, text):
            found_skills.add(skill)

    return found_skills


def analyze_skills(resume_text, job_text):

    resume_skills = extract_keywords(resume_text)
    job_skills = extract_keywords(job_text)

    matched = resume_skills.intersection(job_skills)
    missing = job_skills - resume_skills

    return resume_skills, job_skills, matched, missing