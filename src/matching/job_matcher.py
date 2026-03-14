import os
from src.models.embedding import get_embedding
from src.matching.similarity import calculate_similarity
from src.data_processing.job_parser import read_job_description

def match_jobs(resume_text, job_folder):

    results = []

    resume_embedding = get_embedding(resume_text)

    for job_file in os.listdir(job_folder):

        job_path = os.path.join(job_folder, job_file)

        job_text = read_job_description(job_path)

        job_embedding = get_embedding(job_text)

        score = calculate_similarity(resume_embedding, job_embedding)

        # FIX HERE
        results.append((job_file, float(score)))

    results.sort(key=lambda x: x[1], reverse=True)

    return results