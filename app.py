import streamlit as st

from src.preprocess import clean_text
from src.similarity import calculate_similarity
from src.keyword_extractor import analyze_skills
from src.file_parser import extract_text_from_pdf, extract_text_from_docx

SUGGESTIONS = {
    "docker": "Add Docker experience or containerization projects.",
    "aws": "Mention AWS cloud services or deployments.",
    "kubernetes": "Highlight container orchestration or Kubernetes deployments.",
    "machine learning": "Add ML projects or model deployment examples.",
    "rest apis": "Mention API design, development, or backend services."
}


st.title("AI Resume ↔ Job Match Analyzer")

st.write("Upload your resume and compare it with a job description.")


uploaded_file = st.file_uploader(
    "Upload Resume (PDF or DOCX)", type=["pdf", "docx"]
)

resume_text = ""

if uploaded_file is not None:
    if uploaded_file.type == "application/pdf":
        resume_text = extract_text_from_pdf(uploaded_file)

    elif uploaded_file.type == "application/vnd.openxmlformats-officedocument.wordprocessingml.document":
        resume_text = extract_text_from_docx(uploaded_file)

    st.success("Resume uploaded successfully!")

job_description = st.text_area("Paste Job Description")


if st.button("Analyze Match"):

    if resume_text and job_description:

        resume_clean = clean_text(resume_text)
        job_clean = clean_text(job_description)

        text_similarity = calculate_similarity(resume_clean, job_clean) / 100

        resume_skills, job_skills, matched_skills, missing = analyze_skills(resume_clean,job_clean)

        skill_ratio = len(matched_skills) / max(len(job_skills), 1)

        final_score = (0.7 * text_similarity) + (0.3 * skill_ratio)

        st.subheader("Match Score")

        st.write(f"{round(final_score * 100, 2)} %")

        st.subheader("Resume Skills Detected")

        for skill in sorted(resume_skills):
            st.write("•", skill)


        st.subheader("Job Skills Detected")

        for skill in sorted(job_skills):
            st.write("•", skill)

        st.subheader("Matched Skills")

        for skill in sorted(matched_skills):
            st.write("•", skill)


        st.subheader("Missing Skills")

        for skill in sorted(missing):
            st.write("•", skill)

        st.subheader("Suggested Improvements")

        for skill in sorted(missing):
            if skill in SUGGESTIONS:
                st.write("•", SUGGESTIONS[skill])

    else:
        st.warning("Please paste both resume and job description.")