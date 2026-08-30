'''
When starting a new project:
python -m venv .venv
source .venv/bin/activate
which python
which pip
python -m pip install streamlit


learning target final:
Python
  ↓
Streamlit basics
  ↓
Widgets
  ↓
Session State
  ↓
Forms + Layout
  ↓
File Upload
  ↓
Pandas / Charts
  ↓
Caching
  ↓
Secrets
  ↓
Multipage
  ↓
Deployment
  ↓
AI/ML Projects
'''



'''
============================================================
              STREAMLIT — BASIC TO ADVANCED
        Company-Ready + AI/ML Project Preparation
============================================================


============================================================
1. STREAMLIT MENTAL MODEL
============================================================

Think of Streamlit as a Python framework that allows us to
build interactive web applications using mostly Python.

You do NOT need to separately build:

    HTML
    CSS
    JavaScript
    React

for normal Streamlit applications.

The basic architecture is:

                    STREAMLIT
                        │
        ┌───────────────┴────────────────┐
        │                                │
     FRONTEND                         BACKEND
        │                                │
   UI Components                   Python Logic
   Widgets                         APIs
   Layout                          Databases
   Forms                           ML Models
   Charts                          LLMs
        │                                │
        └───────────────┬────────────────┘
                        │
                  STREAMLIT ENGINE
                        │
             Reruns + State + Cache
                        │
                 PRODUCTION APP


Example:

User enters:
    "Explain recursion"

        ↓

Streamlit Widget
    st.text_input()

        ↓

Python Code

        ↓

LLM API
    Gemini / OpenAI / etc.

        ↓

Response

        ↓

Streamlit UI
    st.write()
    st.markdown()


The most important Streamlit concepts are:

1. UI
2. Widgets
3. Rerun model
4. Session State
5. Callbacks
6. Forms
7. Layout
8. Caching
9. Secrets
10. File handling
11. Data visualization
12. Query parameters
13. Multipage applications
14. Deployment


------------------------------------------------------------
IMPORTANT MENTAL MODEL
------------------------------------------------------------

Streamlit is NOT like traditional Flask/Django where you
manually control every HTTP request.

Instead:

    User interaction
          ↓
    Streamlit reruns Python script
          ↓
    Python executes from TOP → BOTTOM
          ↓
    UI is rebuilt


This single concept explains a HUGE part of Streamlit.

You must understand this before advanced Streamlit.


============================================================
2. INSTALLATION & ENVIRONMENT
============================================================

Install:

    pip install streamlit


Check version:

    streamlit --version


Run application:

    streamlit run app.py


Alternative:

    python -m streamlit run app.py


Run Streamlit demo:

    streamlit hello


------------------------------------------------------------
VIRTUAL ENVIRONMENT
------------------------------------------------------------

Create:

    python -m venv .venv


Activate on macOS/Linux:

    source .venv/bin/activate


Windows:

    .venv\Scripts\activate


Install:

    pip install streamlit


Deactivate:

    deactivate


------------------------------------------------------------
REQUIREMENTS.TXT
------------------------------------------------------------

Create:

    requirements.txt


Example:

    streamlit
    pandas
    numpy
    plotly
    google-genai


Install everything:

    pip install -r requirements.txt


For production projects, requirements.txt is important
because another developer/server needs to know which
dependencies are required.


------------------------------------------------------------
BASIC PROJECT STRUCTURE
------------------------------------------------------------

Example:

    my_streamlit_app/
    │
    ├── .venv/
    │
    ├── .streamlit/
    │   ├── config.toml
    │   └── secrets.toml
    │
    ├── src/
    │   ├── app.py
    │   ├── components/
    │   ├── services/
    │   └── utils/
    │
    ├── requirements.txt
    ├── .gitignore
    └── README.md


For learning:

    app.py


is enough.

For company-level applications, separate:

    UI
    Business Logic
    API clients
    Database code
    Utility functions


============================================================
3. DISPLAY ELEMENTS
============================================================

Streamlit provides many functions to display information.


------------------------------------------------------------
st.write()
------------------------------------------------------------

Most flexible/basic output function.

Example:

    st.write("Hello")

    name = "Manish"
    st.write(name)

    st.write("Name:", name)


It can display:

    strings
    numbers
    lists
    dictionaries
    DataFrames
    Markdown-like content
    objects


Example:

    data = {
        "name": "Manish",
        "role": "Engineer"
    }

    st.write(data)


Use st.write() when you want a flexible output function.


------------------------------------------------------------
st.text()
------------------------------------------------------------

Displays plain text.

    st.text("Hello World")


Difference:

    st.text()
        ↓
    Plain text

    st.markdown()
        ↓
    Formatted text


------------------------------------------------------------
st.markdown()
------------------------------------------------------------

Used for formatted text.

Example:

    st.markdown("# Heading")

    st.markdown("**Bold text**")

    st.markdown("*Italic text*")


Can be used to create better UI documentation.


------------------------------------------------------------
st.title()
------------------------------------------------------------

Main application title.

    st.title("AI Document Analyzer")


------------------------------------------------------------
st.header()
------------------------------------------------------------

Major section.

    st.header("Upload Document")


------------------------------------------------------------
st.subheader()
------------------------------------------------------------

Smaller section.

    st.subheader("Analysis Result")


Hierarchy:

    st.title()
        ↓
    st.header()
        ↓
    st.subheader()


------------------------------------------------------------
st.caption()
------------------------------------------------------------

Small supporting text.

    st.caption("Powered by Gemini")


Useful for:

    metadata
    descriptions
    timestamps
    small notes


------------------------------------------------------------
st.code()
------------------------------------------------------------

Displays code.

    st.code(
        "print('Hello World')",
        language="python"
    )


Useful for AI coding assistants and developer tools.


------------------------------------------------------------
st.latex()
------------------------------------------------------------

Displays mathematical formulas.

    st.latex(r"E = mc^2")


Useful for:

    ML applications
    education apps
    mathematical tools


------------------------------------------------------------
MESSAGES
------------------------------------------------------------

Success:

    st.success("File uploaded successfully!")


Information:

    st.info("Processing your document...")


Warning:

    st.warning("Please upload a file.")


Error:

    st.error("Something went wrong.")


Exception:

    try:
        result = 10 / 0
    except Exception as e:
        st.exception(e)


These are very useful for user-friendly error handling.


------------------------------------------------------------
MEDIA
------------------------------------------------------------

Image:

    st.image("image.png")


Audio:

    st.audio("audio.mp3")


Video:

    st.video("video.mp4")


These become useful in:

    Computer Vision
    Speech AI
    Multimedia AI
    Education apps


============================================================
4. INPUT WIDGETS
============================================================

Widgets allow users to interact with your Python program.

Think:

    Widget
       ↓
    User input
       ↓
    Python variable


------------------------------------------------------------
TEXT INPUT
------------------------------------------------------------

    name = st.text_input("Enter your name")


If user enters:

    Manish


then:

    name == "Manish"


Important:

The widget returns a value.


------------------------------------------------------------
TEXT AREA
------------------------------------------------------------

Used for larger text.

    prompt = st.text_area(
        "Enter your question"
    )


Useful for:

    LLM prompts
    document input
    feedback
    descriptions


------------------------------------------------------------
NUMBER INPUT
------------------------------------------------------------

    age = st.number_input(
        "Enter your age",
        min_value=0,
        max_value=100
    )


Useful for numerical parameters.


------------------------------------------------------------
SLIDER
------------------------------------------------------------

    temperature = st.slider(
        "Temperature",
        0.0,
        1.0,
        0.7
    )


Useful for:

    model parameters
    filters
    ranges
    configuration


------------------------------------------------------------
SELECT SLIDER
------------------------------------------------------------

    level = st.select_slider(
        "Difficulty",
        options=["Easy", "Medium", "Hard"]
    )


------------------------------------------------------------
SELECTBOX
------------------------------------------------------------

Choose one option.

    language = st.selectbox(
        "Choose language",
        ["Python", "Java", "C++"]
    )


------------------------------------------------------------
MULTISELECT
------------------------------------------------------------

Choose multiple values.

    skills = st.multiselect(
        "Select skills",
        ["Python", "AWS", "Docker", "Kubernetes"]
    )


Returns a list.


Example:

    ["Python", "AWS"]


------------------------------------------------------------
RADIO
------------------------------------------------------------

Choose exactly one option.

    role = st.radio(
        "Choose role",
        ["SDE", "Cloud", "DevOps"]
    )


------------------------------------------------------------
CHECKBOX
------------------------------------------------------------

Boolean input.

    agree = st.checkbox(
        "I agree"
    )


Returns:

    True
    False


------------------------------------------------------------
TOGGLE
------------------------------------------------------------

Similar to checkbox but visually represented as
an on/off switch.

    dark_mode = st.toggle(
        "Dark Mode"
    )


------------------------------------------------------------
DATE INPUT
------------------------------------------------------------

    date = st.date_input(
        "Select date"
    )


------------------------------------------------------------
TIME INPUT
------------------------------------------------------------

    time = st.time_input(
        "Select time"
    )


------------------------------------------------------------
FILE UPLOADER
------------------------------------------------------------

    file = st.file_uploader(
        "Upload a file"
    )


Can accept:

    PDF
    CSV
    TXT
    DOCX
    images
    etc.


Example:

    file = st.file_uploader(
        "Upload CSV",
        type=["csv"]
    )


------------------------------------------------------------
COLOR PICKER
------------------------------------------------------------

    color = st.color_picker(
        "Choose color"
    )


Returns a color value.


------------------------------------------------------------
FEEDBACK
------------------------------------------------------------

Useful for AI applications.

    feedback = st.feedback(
        "thumbs"
    )


Can be used to collect:

    👍
    👎


This is useful for evaluating LLM responses.

'''





































