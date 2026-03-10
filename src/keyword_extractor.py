from src.ai.skill_extractor_llm import extract_skills_llm
from src.skills import TECH_SKILLS
import re


def extract_keywords(text):

    text = text.lower()
    found_skills = set()

    for skill in TECH_SKILLS:

        pattern = r"\b" + re.escape(skill) + r"\b"

        if re.search(pattern, text):
            found_skills.add(skill)

    return found_skills


def analyze_skills(resume_text, job_text):

    # Try LLM extraction first
    resume_skills = extract_skills_llm(resume_text)
    job_skills = extract_skills_llm(job_text)

    # fallback if LLM fails
    if not resume_skills:
        resume_skills = extract_keywords(resume_text)

    if not job_skills:
        job_skills = extract_keywords(job_text)

    matched = resume_skills.intersection(job_skills)
    missing = job_skills - resume_skills

    return resume_skills, job_skills, matched, missing