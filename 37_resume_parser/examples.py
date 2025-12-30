from file1_resume_parser import parse_resume

data = parse_resume("resume.pdf")

print("Name:", data["name"])
print("Email:", data["email"])
print("Skills:", data["skills"])
