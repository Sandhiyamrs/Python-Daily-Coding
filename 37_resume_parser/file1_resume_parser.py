import re

def parse_resume(text):
    email = re.findall(r"[\\w.-]+@[\\w.-]+", text)
    skills = []

    skill_keywords = ["python", "java", "machine learning", "data analysis"]

    for skill in skill_keywords:
        if skill in text.lower():
            skills.append(skill.title())

    return {
        "Email": email[0] if email else "Not Found",
        "Skills": skills
    }

# Example
resume_text = "Skilled in Python and Machine Learning. Email: test@gmail.com"
print(parse_resume(resume_text))
