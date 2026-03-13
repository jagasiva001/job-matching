SKILLS = [
    "python",
    "machine learning",
    "deep learning",
    "docker",
    "kubernetes",
    "aws",
    "linux",
    "sql",
    "tensorflow",
    "pytorch"
]

def extract_skills(text):

    found_skills = []

    for skill in SKILLS:
        if skill in text:
            found_skills.append(skill)

    return found_skills