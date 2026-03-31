import streamlit as st
import pdfplumber
import docx
import spacy
import json
import os

# Load NLP model
nlp = spacy.load("en_core_web_sm")

# Load predefined skills
with open("skills_list.json") as f:
    skills_db = json.load(f)

# ---------- Helper Functions ----------

def extract_text_from_pdf(pdf_path):
    text = ""
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n"
    return text

def extract_text_from_docx(docx_path):
    doc = docx.Document(docx_path)
    text = ""
    for para in doc.paragraphs:
        text += para.text + "\n"
    return text

def extract_skills(text):
    doc = nlp(text)
    tokens = [token.text.lower() for token in doc if not token.is_stop]
    found_skills = [skill for skill in skills_db if skill.lower() in tokens]
    return set(found_skills)

def analyze_resume(file, job_keywords=[]):
    # Save uploaded file temporarily
    file_path = os.path.join("resumes", file.name)
    with open(file_path, "wb") as f:
        f.write(file.getbuffer())

    # Extract text
    if file.name.endswith(".pdf"):
        text = extract_text_from_pdf(file_path)
    elif file.name.endswith(".docx"):
        text = extract_text_from_docx(file_path)
    else:
        return None, "Unsupported file format"

    # Extract skills
    skills_found = extract_skills(text)

    # Compare with job keywords
    job_keywords_lower = [k.lower() for k in job_keywords]
    missing_skills = [k for k in job_keywords_lower if k not in [s.lower() for s in skills_found]]

    # Simple ATS-like score
    total_keywords = len(job_keywords) if job_keywords else len(skills_db)
    matched = len(skills_found.intersection(set(job_keywords))) if job_keywords else len(skills_found)
    score = round((matched / total_keywords) * 100, 2) if total_keywords else 0

    return {
        "skills_found": list(skills_found),
        "missing_skills": missing_skills,
        "ats_score": score
    }, None

# ---------- Streamlit UI ----------

st.title("💼 AI-Powered Resume Analyzer")

st.write("Upload your resume (PDF or DOCX) and optionally upload a job description text file to see skill gaps and ATS-style score.")

# Resume upload
resume_file = st.file_uploader("Upload Resume", type=["pdf", "docx"])
job_file = st.file_uploader("Optional: Upload Job Description", type=["txt"])

job_keywords = []
if job_file:
    job_keywords = job_file.read().decode("utf-8").split()
    job_keywords = [k.strip() for k in job_keywords if k.strip()]

if resume_file:
    result, error = analyze_resume(resume_file, job_keywords)
    if error:
        st.error(error)
    else:
        st.subheader("✅ Resume Analysis Results")
        st.write(f"**Skills Found:** {', '.join(result['skills_found'])}")
        st.write(f"**Missing Skills:** {', '.join(result['missing_skills']) if result['missing_skills'] else 'None'}")
        st.write(f"**ATS-style Score:** {result['ats_score']}%")