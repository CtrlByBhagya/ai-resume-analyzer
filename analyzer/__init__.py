from .extract import extract_text
from .skills import extract_skills
from .similarity import similarity_score

def run_analysis(resume_file, job_description):
    resume_text = extract_text(resume_file)

    resume_skills = extract_skills(resume_text)
    job_skills = extract_skills(job_description)

    score = similarity_score(resume_text, job_description)

    return{
        "score":round(score * 100),
        "matched":sorted(resume_skills & job_skills),
        "missing":sorted(job_skills - resume_skills),
    }