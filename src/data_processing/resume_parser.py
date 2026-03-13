import pdfplumber

def extract_text_from_resume(file_path):
    text = ""

    with pdfplumber.open(file_path) as pdf:
        for page in pdf.pages:
            text += page.extract_text()

    return text


if __name__ == "__main__":
    file = "data/resumes/resume.pdf"

    text = extract_text_from_resume(file)

    print("\nResume Content:\n")
    print(text)