from fastapi import FastAPI
from src.matching.job_matcher import match_jobs

app = FastAPI()

@app.get("/")
def home():

    return {"message": "Job Matching API Running"}


@app.post("/match")

def match(resume_text: str):

    results = match_jobs(resume_text, "data/job_descriptions")

    return {"matches": results[:3]}