import os
from src.data_processing.resume_parser import extract_text_from_resume
from src.data_processing.preprocessing import clean_text
from src.matching.job_matcher import match_jobs

# Resume path
resume_path = "data/resumes/sample_ml_engineer_resume.pdf"

# Check resume file
if not os.path.exists(resume_path):
    print("Resume file not found!")
    exit()

# Extract text from resume
resume_text = extract_text_from_resume(resume_path)

# Clean the resume text
cleaned_resume = clean_text(resume_text)

# Match jobs
results = match_jobs(cleaned_resume, "data/job_descriptions")

print("\nTop Job Matches:\n")

# Display top matches
for job, score in results[:3]:
    print(f"{job}  ->  {round(score * 100, 2)}% match")