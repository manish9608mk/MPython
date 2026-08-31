'''
Common Streamlit widgets:
| Widget               | Use                     |
| -------------------- | ----------------------- |
| `st.button()`        | Button click            |
| `st.selectbox()`     | Dropdown                |
| `st.multiselect()`   | Multiple options select |
| `st.radio()`         | One option select       |
| `st.checkbox()`      | True/False              |
| `st.slider()`        | Value/range choose      |
| `st.text_input()`    | Single-line text        |
| `st.text_area()`     | Large text              |
| `st.number_input()`  | Number input             |
| `st.date_input()`    | Date select              |
| `st.file_uploader()` | File upload              |
| `st.color_picker()`  | Color choose             |



Project:

           Developer Profile Builder

Name:          [______________]

Choose Role:
[ Cloud Engineer ▼ ]

Experience:
[──────●──────]  2 years

Skills:
☑ Python
☑ AWS
☐ Docker
☑ Kubernetes

Preferred Language:
( ) Python
( ) C++
( ) Java

        [ Generate Profile ]

--------------------------------
 Your Profile

Role: Cloud Engineer
Experience: 2 years
Skills: Python, AWS, Kubernetes
Language: Python
--------------------------------
'''

# Developer Profile Builder app
import streamlit as st

st.title("Developer Profile Builder")
st.caption("Create your developer profile using streamlit")

# user input
name = st.text_input("Enter your name: ")

dob = st.date_input("Select your date of birth:")

about = st.text_area("Tell us about yourself:")

# role
role = st.selectbox(
  "Choose your role:",
  [
    "Cloud Engineer",
    "DevOps Engineer",
    "Software Engineer",
    "Data Scientist",
    "AI/ML Engineer",
  ]
)

# Experience 
experience = st.slider(
  "Years of Experience:",
  min_value=0,
  max_value=10,
  value=2
)

# Expected salary
salary = st.number_input(
  "Expected Salary (LPA):",
  min_value=0.0,
  max_value=100.0,
  value=6.0,
  step=0.5
)

# skills
st.write("Select your skills:")

python_skill = st.checkbox("Python")
aws_skill = st.checkbox("AWS")
docker_skill = st.checkbox("Docker")
kubernetes_skill = st.checkbox("Kubernetes")

# Technologies
technologies = st.multiselect(
  "Select your technologies:",
  [
    "Python",
    "AWS",
    "Docker",
    "Kubernetes",
    "Terraform",
    "Git",
    "Linux",
    "Jenkins"
  ]
)

# Preferred programming language
language = st.radio(
  "Preferred programming language",
  ["Python", "C++", "Java"]
)

# Resume
resume = st.file_uploader(
  "Upload your resume:",
  type=["pdf", "docx"]
)

# Profile color
profile_color = st.color_picker(
  "Choose your profile color:",
  "#00FF00"
)

# generate profile
if st.button("Generate Profile"):

  # stored selected skill
  skills = []

  if python_skill:
    skills.append("Python")

  if aws_skill:
    skills.append("AWS")

  if docker_skill:
    skills.append("Docker")

  if kubernetes_skill:
    skills.append("Kubernetes")


  # display profile
  st.divider()

  st.subheader("Your profile")

  st.write(f"Name: {name}")
  st.write(f"Date of Birth: {dob}")
  st.write(f"Role: {role}")
  st.write(f"Experience: {experience} years")
  st.write(f"Expected Salary: {salary} LPA")
  st.write(f"Preferred Language: {language}")
  st.write(f"Profile Color: {profile_color}")

  st.write(f"About: {about}")

  # skill
  if skills:
    st.write("Skills:")

    for skill in skills:
      st.write(f"- {skill}")

  else:
    st.write("No skill selected")

  # technologies
  if technologies:
    st.write("Technologies:")

    for technology in technologies:
      st.write(f"- {technology}")

  else:
    st.write("No technology selected")

  # resume
  if resume:
    st.success(f"Resume uploaded: {resume.name}")

  else:
    st.write("No resume uploaded")

  st.success(f"Profile generated successfully for {name}!")