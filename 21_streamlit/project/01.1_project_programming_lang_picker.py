import streamlit as st

# Page title
st.title("Programming Language Picker")
st.header("Choose Your Language")
st.subheader("Explore Popular Programming Languages")
st.caption("Learn about different programming languages")

# Language picker
languages = [
    "Python",
    "C++",
    "Java",
    "JavaScript",
    "TypeScript",
    "Go",
    "Rust"
]

languages = st.selectbox(
    "Choose your favourite programming language:",
    languages
)

# Language information
languages_info = {
    "Python": "Great for AI, ML, Data Science, Automation and Backend development.",
    "C++": "Excellent for DSA, competitive programming and performance-critical systems.",
    "Java": "Widely used for enterprise applications, backend systems and Android development.",
    "JavaScript": "The core language of web development and frontend applications.",
    "TypeScript": "JavaScript with types — popular for large-scale frontend and backend applications.",
    "Go": "Simple and fast language commonly used for cloud, networking and distributed systems.",
    "Rust": "A memory-safe systems programming language focused on performance and reliability."
}

# Display selected language
st.write(f"You selected: {languages}")

# Display information
st.info(languages_info[languages])

# Success message
st.success(f"Excellent choice! You selected {languages}.")