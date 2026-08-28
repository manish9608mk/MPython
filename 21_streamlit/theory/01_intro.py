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


============================================================
5. BUTTONS & USER INTERACTION
============================================================

Basic button:

    if st.button("Submit"):
        st.write("Submitted!")


Important:

st.button() returns:

    True

only during the interaction/rerun triggered by
that button click.

Otherwise:

    False


------------------------------------------------------------
IMPORTANT PATTERN
------------------------------------------------------------

    if st.button("Generate"):
        result = generate_response()
        st.write(result)


This is extremely common in Streamlit.


------------------------------------------------------------
DOWNLOAD BUTTON
------------------------------------------------------------

Used to allow users to download generated data.

Example:

    data = "Hello World"

    st.download_button(
        label="Download",
        data=data,
        file_name="result.txt"
    )


Useful for:

    CSV
    JSON
    TXT
    generated reports
    processed documents


------------------------------------------------------------
LINK BUTTON
------------------------------------------------------------

    st.link_button(
        "Open GitHub",
        "https://github.com"
    )


Used to navigate users to another URL.


------------------------------------------------------------
BUTTON vs FORM SUBMIT BUTTON
------------------------------------------------------------

Normal button:

    st.button()


Used for individual actions.

Form button:

    st.form_submit_button()


Used inside:

    with st.form(...):


Main difference:

Normal widgets normally trigger reruns when their
values change.

Forms allow multiple inputs to be collected first
and submitted together.


============================================================
6. STREAMLIT EXECUTION MODEL
============================================================

THIS IS ONE OF THE MOST IMPORTANT STREAMLIT TOPICS.


Normal Python:

    Python executes once
        ↓
    program finishes


Streamlit:

    User interacts
        ↓
    Streamlit reruns script
        ↓
    Python executes TOP → BOTTOM
        ↓
    UI is rebuilt


------------------------------------------------------------
EXAMPLE
------------------------------------------------------------

    name = st.text_input("Name")

    if st.button("Submit"):
        st.write(name)


Suppose user enters:

    Manish


Streamlit runs the script.

The value of:

    name

is available during that run.


When user clicks Submit:

    Streamlit reruns the script

and:

    name = "Manish"

is available again because the widget maintains its
own state.


------------------------------------------------------------
WHY BEGINNERS GET CONFUSED
------------------------------------------------------------

Consider:

    count = 0

    if st.button("Increment"):
        count += 1

    st.write(count)


You click the button.

Result:

    1


But click again.

You may expect:

    2


Instead:

    1


Why?

Because the script reruns:

    count = 0

again.

Then:

    count += 1

makes it:

    1


So normal Python variables do NOT automatically persist
across Streamlit reruns.


This is why Session State exists.


------------------------------------------------------------
EXECUTION ORDER
------------------------------------------------------------

Very important:

    User interaction
          ↓
    Widget state updated
          ↓
    Callback executes
          ↓
    Full script reruns
          ↓
    Python executes top → bottom
          ↓
    UI updates


------------------------------------------------------------
WIDGET IDENTITY
------------------------------------------------------------

Streamlit identifies widgets based on things such as:

    widget type
    label
    key
    relevant parameters


Using explicit keys is important when you have multiple
similar widgets.

Example:

    st.text_input(
        "Name",
        key="username"
    )


Then:

    st.session_state.username


can be used to access its value.


------------------------------------------------------------
EPHEMERAL VALUES
------------------------------------------------------------

Some interaction values are temporary.

For example, button clicks are event-like.

    if st.button("Submit"):
        ...

The button is not permanently "True".

The click triggers a rerun where the button returns True.


============================================================
7. SESSION STATE
============================================================

Session State is used to persist information across
reruns for a user's Streamlit session.


------------------------------------------------------------
BASIC EXAMPLE
------------------------------------------------------------

    if "count" not in st.session_state:
        st.session_state.count = 0


    if st.button("Increment"):
        st.session_state.count += 1


    st.write(st.session_state.count)


Now:

    First click  → 1
    Second click → 2
    Third click  → 3


because the value survives reruns.


------------------------------------------------------------
NORMAL VARIABLE vs SESSION STATE
------------------------------------------------------------

Normal variable:

    count = 0

    ↓

    rerun

    ↓

    count = 0 again


Session State:

    st.session_state.count = 0

    ↓

    rerun

    ↓

    value persists


Think:

    Normal variable
          ↓
    current execution


    Session State
          ↓
    current user session


------------------------------------------------------------
DICTIONARY STYLE
------------------------------------------------------------

    st.session_state["count"]


Initialize:

    if "count" not in st.session_state:
        st.session_state["count"] = 0


Update:

    st.session_state["count"] += 1


------------------------------------------------------------
ATTRIBUTE STYLE
------------------------------------------------------------

    st.session_state.count


Both approaches are commonly used.


------------------------------------------------------------
INITIALIZATION PATTERN
------------------------------------------------------------

Always initialize state before using it.

    if "messages" not in st.session_state:
        st.session_state.messages = []


Then:

    st.session_state.messages.append(
        {"role": "user", "content": "Hello"}
    )


This pattern becomes extremely important for chatbots.


------------------------------------------------------------
DELETE STATE
------------------------------------------------------------

    del st.session_state["count"]


Clear all state:

    st.session_state.clear()


Use carefully.


------------------------------------------------------------
SESSION STATE + CHATBOT
------------------------------------------------------------

A chatbot commonly needs:

    st.session_state.messages


Example concept:

    if "messages" not in st.session_state:
        st.session_state.messages = []


When user sends a message:

    st.session_state.messages.append(
        {
            "role": "user",
            "content": user_message
        }
    )


Then append AI response:

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": response
        }
    )


Now the conversation survives reruns.


------------------------------------------------------------
SESSION STATE + MULTIPAGE APP
------------------------------------------------------------

Session State can also be used to share information
between pages of a Streamlit application.

Example:

    Page 1
       ↓
    user selects model
       ↓
    session_state
       ↓
    Page 2
       ↓
    uses selected model


============================================================
8. CALLBACKS
============================================================

Callbacks allow a function to execute when a widget
interaction occurs.


------------------------------------------------------------
on_click
------------------------------------------------------------

Used with button-like widgets.

Example:

    def submit():
        st.session_state.submitted = True


    st.button(
        "Submit",
        on_click=submit
    )


------------------------------------------------------------
on_change
------------------------------------------------------------

Used with many input widgets.

Example:

    def name_changed():
        print("Name changed")


    st.text_input(
        "Name",
        on_change=name_changed
    )


------------------------------------------------------------
CALLBACK EXECUTION ORDER
------------------------------------------------------------

Very important:

    User interaction
          ↓
    Callback
          ↓
    Full Streamlit rerun
          ↓
    Script executes top → bottom


------------------------------------------------------------
WHY CALLBACKS?
------------------------------------------------------------

Without callback:

    if st.button("Submit"):
        ...

With callback:

    def submit():
        ...


    st.button(
        "Submit",
        on_click=submit
    )


Callbacks become useful when application state needs
to be updated in a controlled way.


------------------------------------------------------------
CALLBACK + ARGUMENTS
------------------------------------------------------------

Callbacks can receive arguments using:

    args
    kwargs


Conceptually:

    def update_name(name):
        st.session_state.name = name


    st.button(
        "Save",
        on_click=update_name,
        args=("Manish",)
    )


============================================================
9. LAYOUT & UI DESIGN
============================================================

Once widgets are understood, learn how to design
professional interfaces.


------------------------------------------------------------
SIDEBAR
------------------------------------------------------------

    st.sidebar.title("Settings")

    model = st.sidebar.selectbox(
        "Model",
        ["Gemini", "GPT"]
    )


Good for:

    settings
    filters
    navigation
    configuration


------------------------------------------------------------
COLUMNS
------------------------------------------------------------

    col1, col2 = st.columns(2)


    with col1:
        st.write("Left")


    with col2:
        st.write("Right")


Useful for dashboards.


Example:

    col1, col2, col3 = st.columns(3)


Then:

    with col1:
        st.metric("Users", 1000)

    with col2:
        st.metric("Revenue", "$50K")

    with col3:
        st.metric("Accuracy", "94%")


------------------------------------------------------------
CONTAINER
------------------------------------------------------------

    with st.container():
        st.write("Inside container")


Containers help organize UI elements.


------------------------------------------------------------
EXPANDER
------------------------------------------------------------

    with st.expander("Show details"):
        st.write("Detailed information")


Useful for:

    logs
    explanations
    advanced settings
    long responses


------------------------------------------------------------
TABS
------------------------------------------------------------

    tab1, tab2 = st.tabs(
        ["Overview", "Details"]
    )


    with tab1:
        st.write("Overview")


    with tab2:
        st.write("Details")


Useful for dashboards and multi-section applications.


------------------------------------------------------------
EMPTY
------------------------------------------------------------

    placeholder = st.empty()


Later:

    placeholder.write("Loading...")


Then:

    placeholder.write("Completed!")


Useful for dynamic UI updates.


------------------------------------------------------------
POPOVER
------------------------------------------------------------

Useful when you want a small temporary UI panel.

Example concept:

    with st.popover("Settings"):
        st.checkbox("Enable feature")


------------------------------------------------------------
DIALOG
------------------------------------------------------------

Used for modal-style interactions.

Useful for:

    confirmations
    forms
    detailed information
    editing


------------------------------------------------------------
UI DESIGN MENTAL MODEL
------------------------------------------------------------

    Layout
       ↓
    Container
       ↓
    Widget
       ↓
    User interaction
       ↓
    State
       ↓
    Backend logic
       ↓
    Updated UI


============================================================
10. FORMS
============================================================

Forms are extremely important.


Normally:

    User changes widget
          ↓
    Streamlit reruns


Imagine a registration form:

    Name
    Email
    Age
    Country


Without form, interactions can cause repeated reruns.


With form:

    User fills fields
          ↓
    No immediate processing
          ↓
    User clicks Submit
          ↓
    Form data submitted together
          ↓
    Process data


------------------------------------------------------------
BASIC FORM
------------------------------------------------------------

    with st.form("my_form"):

        name = st.text_input("Name")

        email = st.text_input("Email")

        age = st.number_input("Age")

        submitted = st.form_submit_button("Submit")


        if submitted:
            st.write(name)
            st.write(email)
            st.write(age)


------------------------------------------------------------
WHY FORMS?
------------------------------------------------------------

Use forms when you want to collect multiple inputs
before executing expensive logic.

Examples:

    Search form
    Login form
    Registration form
    ML prediction form
    Configuration form
    Database filter form


------------------------------------------------------------
IMPORTANT
------------------------------------------------------------

A form needs:

    st.form_submit_button()


to submit its values.


============================================================
11. DATA HANDLING
============================================================

Very important for AI/ML applications.


Streamlit + Python data ecosystem:

    Streamlit
        ↓
    Pandas
        ↓
    NumPy
        ↓
    Visualization
        ↓
    ML
        ↓
    Deployment


------------------------------------------------------------
st.dataframe()
------------------------------------------------------------

Interactive DataFrame display.

    st.dataframe(df)


Good for:

    filtering
    sorting
    inspecting data


------------------------------------------------------------
st.table()
------------------------------------------------------------

Static table.

    st.table(df)


Useful when you don't need interactive behavior.


------------------------------------------------------------
st.data_editor()
------------------------------------------------------------

Allows users to edit tabular data.

    edited_df = st.data_editor(df)


Useful for:

    CRUD-style interfaces
    manual data cleaning
    configuration
    dataset editing


------------------------------------------------------------
PANDAS
------------------------------------------------------------

Example:

    import pandas as pd

    df = pd.read_csv("data.csv")

    st.dataframe(df)


Then:

    st.write(df.shape)

    st.write(df.describe())


------------------------------------------------------------
CSV
------------------------------------------------------------

Upload:

    file = st.file_uploader(
        "Upload CSV",
        type=["csv"]
    )


Then:

    if file:
        df = pd.read_csv(file)
        st.dataframe(df)


------------------------------------------------------------
JSON
------------------------------------------------------------

Python:

    import json

    data = json.load(file)


Can then display:

    st.json(data)


------------------------------------------------------------
EXCEL
------------------------------------------------------------

With Pandas:

    df = pd.read_excel(file)

    st.dataframe(df)


------------------------------------------------------------
PARQUET
------------------------------------------------------------

For large analytical datasets:

    df = pd.read_parquet(file)


------------------------------------------------------------
PROJECT — CSV DATA EXPLORER
------------------------------------------------------------

Build:

    CSV Data Explorer


Flow:

    Upload CSV
        ↓
    Read with Pandas
        ↓
    Display dataframe
        ↓
    Show shape
        ↓
    Show statistics
        ↓
    Filters
        ↓
    Charts
        ↓
    Download filtered data


This project teaches:

    Streamlit
    Pandas
    File handling
    State
    Visualization
    Download


============================================================
12. CHARTS & VISUALIZATION
============================================================

Streamlit provides native chart functions.


------------------------------------------------------------
LINE CHART
------------------------------------------------------------

    st.line_chart(data)


Useful for:

    time series
    trends


------------------------------------------------------------
BAR CHART
------------------------------------------------------------

    st.bar_chart(data)


Useful for:

    category comparison


------------------------------------------------------------
AREA CHART
------------------------------------------------------------

    st.area_chart(data)


------------------------------------------------------------
SCATTER CHART
------------------------------------------------------------

    st.scatter_chart(data)


Useful for:

    relationships
    ML datasets


------------------------------------------------------------
MATPLOTLIB
------------------------------------------------------------

    import matplotlib.pyplot as plt

    fig, ax = plt.subplots()

    ax.plot(x, y)

    st.pyplot(fig)


Useful when you need custom Python plotting.


------------------------------------------------------------
PLOTLY
------------------------------------------------------------

Very important for modern dashboards.

Example:

    import plotly.express as px

    fig = px.scatter(
        df,
        x="age",
        y="salary"
    )

    st.plotly_chart(fig)


Plotly is highly useful for:

    dashboards
    analytics
    ML visualization
    interactive charts


------------------------------------------------------------
ALTAIR
------------------------------------------------------------

Declarative visualization library.

Useful for analytical dashboards.


------------------------------------------------------------
PYDECK
------------------------------------------------------------

Useful for geospatial and map-based visualizations.


------------------------------------------------------------
AI/ML PRIORITY
------------------------------------------------------------

For your career:

    Streamlit
        ↓
    Pandas
        ↓
    NumPy
        ↓
    Plotly
        ↓
    ML visualization
        ↓
    AI application


============================================================
13. FILE UPLOAD & DOWNLOAD
============================================================

Extremely important for AI applications.


------------------------------------------------------------
FILE UPLOADER
------------------------------------------------------------

    uploaded_file = st.file_uploader(
        "Upload document"
    )


Check:

    if uploaded_file:
        st.write(uploaded_file.name)


You can restrict file types:

    type=["pdf"]


or:

    type=["csv", "xlsx"]


------------------------------------------------------------
MULTIPLE FILES
------------------------------------------------------------

Conceptually:

    st.file_uploader(
        "Upload files",
        accept_multiple_files=True
    )


Then process each file.


------------------------------------------------------------
DOWNLOAD
------------------------------------------------------------

    st.download_button(
        "Download result",
        data=result,
        file_name="result.txt"
    )


------------------------------------------------------------
PROJECT — DOCUMENT ANALYZER
------------------------------------------------------------

Build:

    Document Analyzer


Flow:

    Upload PDF
        ↓
    Extract text
        ↓
    Clean text
        ↓
    Send to LLM
        ↓
    Generate summary
        ↓
    Display result
        ↓
    Download result


Later this can evolve into:

    RAG Application


Flow:

    PDF
      ↓
    Text extraction
      ↓
    Chunking
      ↓
    Embeddings
      ↓
    Vector database
      ↓
    Retrieval
      ↓
    LLM
      ↓
    Streamlit UI


This is highly relevant to AI/ML projects.


============================================================
14. CONFIGURATION & SECRETS
============================================================

VERY IMPORTANT FOR COMPANY PROJECTS.


Never hard-code secrets.


BAD:

    API_KEY = "sk-xxxxxxxx"


This can expose your credentials through:

    GitHub
    logs
    screenshots
    source code


------------------------------------------------------------
STREAMLIT DIRECTORY
------------------------------------------------------------

Create:

    .streamlit/


Inside:

    config.toml
    secrets.toml


------------------------------------------------------------
CONFIG.TOML
------------------------------------------------------------

Used for application configuration.

Conceptually:

    .streamlit/
        config.toml


Can contain settings related to:

    theme
    server
    UI behavior


------------------------------------------------------------
SECRETS.TOML
------------------------------------------------------------

Example:

    .streamlit/secrets.toml


Contains:

    API_KEY = "your-secret"


Then Python:

    api_key = st.secrets["API_KEY"]


------------------------------------------------------------
IMPORTANT
------------------------------------------------------------

Never commit secrets.toml to GitHub.

Add:

    .streamlit/secrets.toml


to:

    .gitignore


------------------------------------------------------------
COMPANY MENTAL MODEL
------------------------------------------------------------

Code:

    GitHub

Secrets:

    Secret manager / environment / deployment secrets


For example:

    AWS Secrets Manager
    environment variables
    CI/CD secret store
    Streamlit secrets


The exact mechanism depends on the deployment environment.


============================================================
15. CACHING
============================================================

Caching is one of the MOST IMPORTANT Streamlit concepts
for production applications.


Why?

Suppose you have:

    expensive ML model loading

or:

    expensive database query

or:

    expensive API operation


If Streamlit reruns the script repeatedly, doing that
expensive work every time is inefficient.


Caching helps.


------------------------------------------------------------
st.cache_data
------------------------------------------------------------

Use for data-returning computations.


Example:

    @st.cache_data
    def load_data():
        return pd.read_csv("data.csv")


Then:

    df = load_data()


Streamlit can reuse the cached result instead of
recomputing unnecessarily.


Good use cases:

    CSV loading
    database query results
    API responses
    data transformations
    preprocessing results


------------------------------------------------------------
st.cache_resource
------------------------------------------------------------

Use for expensive resources that should be reused.


Examples:

    ML model
    database connection
    LLM client
    embedding model


Example concept:

    @st.cache_resource
    def load_model():
        model = ...
        return model


Then:

    model = load_model()


------------------------------------------------------------
CACHE DATA vs CACHE RESOURCE
------------------------------------------------------------

VERY IMPORTANT.


st.cache_data:

    Function
       ↓
    Data/result
       ↓
    Cache


Examples:

    DataFrame
    transformed data
    API response


st.cache_resource:

    Function
       ↓
    Resource/object
       ↓
    Reuse


Examples:

    ML model
    database connection
    LLM client


------------------------------------------------------------
SESSION STATE vs CACHE
------------------------------------------------------------

This distinction is extremely important.


SESSION STATE:

    User-specific state


Example:

    chat history
    selected model
    current user settings
    form state


CACHE DATA:

    Reusable computed data


Example:

    processed CSV
    API result
    database query result


CACHE RESOURCE:

    Reusable expensive resource


Example:

    ML model
    database connection
    LLM client


Think:

    Session State
        ↓
    "What belongs to THIS USER?"


    cache_data
        ↓
    "What expensive DATA can I reuse?"


    cache_resource
        ↓
    "What expensive RESOURCE can I reuse?"


------------------------------------------------------------
AI PROJECT EXAMPLE
------------------------------------------------------------

Suppose we build an AI chatbot.

We might have:

    st.session_state.messages

for:

    chat history


Then:

    @st.cache_resource
    def create_llm_client():
        return ...


for:

    LLM client


And:

    @st.cache_data
    def process_document(file):
        return ...


for:

    processed document data


This combination is extremely common in serious
Streamlit AI applications.


============================================================
16. QUERY PARAMETERS & URL STATE
============================================================

Streamlit applications can use query parameters
inside the browser URL.


Example:

    localhost:8501/?user=manish


Here:

    user=manish


is a query parameter.


------------------------------------------------------------
MENTAL MODEL
------------------------------------------------------------

    Browser URL
          ↓
    Query parameters
          ↓
    Streamlit application
          ↓
    Application behavior


------------------------------------------------------------
st.query_params
------------------------------------------------------------

Current Streamlit API:

    st.query_params


Example concept:

    user = st.query_params.get("user")


If URL is:

    ?user=manish


then:

    user

can contain:

    "manish"


------------------------------------------------------------
SETTING QUERY PARAMETERS
------------------------------------------------------------

Conceptually:

    st.query_params["user"] = "manish"


URL can then represent application state.


------------------------------------------------------------
WHY USE QUERY PARAMETERS?
------------------------------------------------------------

Useful for:

    shareable URLs
    filters
    selected pages
    search state
    dashboard state
    deep linking


Example:

    /?page=analytics

or:

    /?user=manish


This allows application state to be represented
in the URL.


============================================================
17. ADVANCED STREAMLIT — NEXT LEVEL
============================================================

After mastering the above 16 topics, continue with:


------------------------------------------------------------
MULTIPAGE APPLICATIONS
------------------------------------------------------------

Learn how to create applications with multiple pages.

Example:

    app/
    │
    ├── app.py
    │
    └── pages/
        ├── dashboard.py
        ├── analytics.py
        └── settings.py


Example application:

    AI Platform
        │
        ├── Chat
        ├── Documents
        ├── Analytics
        └── Settings


------------------------------------------------------------
CUSTOM COMPONENTS
------------------------------------------------------------

Learn how Streamlit can interact with custom frontend
components when built-in components aren't enough.


Useful when:

    Streamlit built-in UI
        ↓
    is insufficient
        ↓
    custom frontend component


This is advanced.


------------------------------------------------------------
SESSION MANAGEMENT
------------------------------------------------------------

Understand:

    user session
    session state
    multiple users
    state isolation


Important for production.


------------------------------------------------------------
ERROR HANDLING
------------------------------------------------------------

Learn:

    try
    except
    finally


Combined with:

    st.error()
    st.warning()
    st.exception()


Example:

    try:
        result = expensive_operation()

    except Exception as e:
        st.error("Operation failed.")
        st.exception(e)


Never expose sensitive internal information
in production errors.


------------------------------------------------------------
LOADING STATES
------------------------------------------------------------

For expensive operations:

    with st.spinner("Processing..."):
        result = process_data()


Useful for:

    LLM calls
    database queries
    ML inference
    document processing


------------------------------------------------------------
PROGRESS
------------------------------------------------------------

For long-running operations:

    progress = st.progress(0)

    progress.progress(50)

    progress.progress(100)


Useful for:

    file processing
    batch jobs
    ML pipelines


------------------------------------------------------------
STATUS / LOGGING
------------------------------------------------------------

For advanced applications, understand:

    logging
    application status
    errors
    debugging


Do not rely only on:

    print()


Production applications need structured logging
and proper observability.


============================================================
18. STREAMLIT + APIs
============================================================

This is especially important for your AI/ML direction.


Architecture:

    Streamlit
        ↓
    Python service layer
        ↓
    External API
        ↓
    Response
        ↓
    Streamlit UI


Example:

    User enters prompt
          ↓
    Streamlit
          ↓
    Gemini API
          ↓
    Response
          ↓
    st.markdown()


Do NOT put all business logic directly inside app.py
when the application becomes large.


Better:

    app.py
       ↓
    service
       ↓
    API client


Example:

    src/
    │
    ├── app.py
    │
    ├── services/
    │   └── gemini_service.py
    │
    ├── clients/
    │   └── gemini_client.py
    │
    └── utils/
        └── helpers.py


============================================================
19. STREAMLIT + DATABASE
============================================================

Learn how Streamlit communicates with databases.


Architecture:

    Streamlit
        ↓
    Database layer
        ↓
    PostgreSQL / MySQL / SQLite
        ↓
    Data
        ↓
    Streamlit


Important concepts:

    database connection
    SQL queries
    connection pooling
    caching
    transactions
    error handling


For expensive/reusable connections:

    @st.cache_resource


can be useful.


============================================================
20. STREAMLIT + MACHINE LEARNING
============================================================

Very important for AI/ML projects.


Typical architecture:

    User
      ↓
    Streamlit UI
      ↓
    Input preprocessing
      ↓
    ML model
      ↓
    Prediction
      ↓
    Visualization


Example:

    Age
    Salary
    Experience
        ↓
    ML Model
        ↓
    Prediction


The model should generally be loaded efficiently,
rather than reloaded unnecessarily on every rerun.


Typical concept:

    @st.cache_resource
    def load_model():
        return trained_model


============================================================
21. STREAMLIT + LLM
============================================================

This is directly relevant to AI applications.


Architecture:

    User
      ↓
    Streamlit
      ↓
    Prompt
      ↓
    LLM Client
      ↓
    Gemini / OpenAI / other model
      ↓
    Response
      ↓
    Streamlit


Important concepts:

    prompt input
    chat history
    session state
    streaming response
    error handling
    API secrets
    caching
    token/cost awareness
    model configuration


------------------------------------------------------------
CHAT APPLICATION
------------------------------------------------------------

Important Streamlit concepts:

    st.chat_message()

    st.chat_input()


Example architecture:

    if "messages" not in st.session_state:
        st.session_state.messages = []


User:

    st.chat_input()


Then:

    user message
        ↓
    session state
        ↓
    LLM
        ↓
    assistant response
        ↓
    session state


This is where everything you've learned starts
coming together.


============================================================
22. STREAMLIT + RAG
============================================================

A very important AI project architecture.


    Upload PDF
        ↓
    Extract text
        ↓
    Split into chunks
        ↓
    Generate embeddings
        ↓
    Vector database
        ↓
    Retrieve relevant chunks
        ↓
    LLM
        ↓
    Answer
        ↓
    Streamlit


Streamlit handles:

    UI
    uploads
    chat
    settings
    results
    citations
    downloads


Backend handles:

    document processing
    embeddings
    vector search
    LLM calls


============================================================
23. PRODUCTION PROJECT STRUCTURE
============================================================

A larger Streamlit AI project might look like:


    ai_application/
    │
    ├── .streamlit/
    │   ├── config.toml
    │   └── secrets.toml
    │
    ├── src/
    │   ├── app.py
    │   │
    │   ├── pages/
    │   │   ├── chat.py
    │   │   ├── documents.py
    │   │   └── analytics.py
    │   │
    │   ├── services/
    │   │   ├── llm_service.py
    │   │   ├── rag_service.py
    │   │   └── document_service.py
    │   │
    │   ├── clients/
    │   │   ├── llm_client.py
    │   │   └── db_client.py
    │   │
    │   └── utils/
    │       ├── helpers.py
    │       └── validators.py
    │
    ├── tests/
    │
    ├── requirements.txt
    ├── .gitignore
    └── README.md


Goal:

    UI code
       ↓
    Service layer
       ↓
    External systems


Keep responsibilities separated.


============================================================
24. STREAMLIT PROJECT DEVELOPMENT WORKFLOW
============================================================

When starting a new project:
python -m venv .venv
source .venv/bin/activate
which python
which pip
python -m pip install streamlit


STEP 1

Create environment.

    python -m venv .venv


STEP 2

Install dependencies.

    pip install streamlit


STEP 3

Create:

    app.py


STEP 4

Build basic UI.

    st.title()
    st.write()


STEP 5

Add widgets.

    st.text_input()
    st.selectbox()
    st.button()


STEP 6

Understand reruns.


STEP 7

Add Session State.


STEP 8

Add callbacks where appropriate.


STEP 9

Add forms.


STEP 10

Design layout.

    sidebar
    columns
    tabs
    containers


STEP 11

Add data handling.


STEP 12

Add visualization.


STEP 13

Add API/backend logic.


STEP 14

Add caching.


STEP 15

Add secrets/configuration.


STEP 16

Add error handling.


STEP 17

Add tests.


STEP 18

Create requirements.txt.


STEP 19

Git/GitHub.


STEP 20

Deploy.


============================================================
25. MOST IMPORTANT STREAMLIT CONCEPTS TO MASTER
============================================================

Do NOT just memorize functions.

You should deeply understand:


LEVEL 1 — BASIC

    st.write()
    st.title()
    st.header()
    st.text()
    st.markdown()

    st.text_input()
    st.text_area()
    st.number_input()
    st.slider()

    st.selectbox()
    st.multiselect()
    st.radio()
    st.checkbox()

    st.button()


LEVEL 2 — INTERACTION

    reruns
    widget state
    execution order
    callbacks


LEVEL 3 — STATE

    st.session_state


LEVEL 4 — UI

    sidebar
    columns
    containers
    tabs
    expanders
    popovers
    dialogs


LEVEL 5 — FORMS

    st.form()
    st.form_submit_button()


LEVEL 6 — DATA

    st.dataframe()
    st.data_editor()
    st.table()

    Pandas
    NumPy


LEVEL 7 — FILES

    st.file_uploader()
    st.download_button()


LEVEL 8 — VISUALIZATION

    native charts
    Matplotlib
    Plotly
    Altair
    PyDeck


LEVEL 9 — CONFIGURATION

    config.toml
    secrets.toml
    st.secrets


LEVEL 10 — PERFORMANCE

    st.cache_data
    st.cache_resource


LEVEL 11 — URL STATE

    st.query_params


LEVEL 12 — AI/ML

    ML models
    APIs
    LLMs
    chat
    RAG
    embeddings
    vector databases


LEVEL 13 — PRODUCTION

    project structure
    error handling
    logging
    testing
    security
    deployment
    scalability


============================================================
26. THE 3 MOST IMPORTANT CONCEPTS
============================================================

If you remember only three things initially:


1. RERUN

    User interaction
          ↓
    Script reruns
          ↓
    Top → Bottom


2. SESSION STATE

    Data that belongs to the current user session.


3. CACHE

    Reuse expensive computations/resources.


And remember:


    Session State
        =
    User-specific state


    cache_data
        =
    Reusable computed DATA


    cache_resource
        =
    Reusable expensive RESOURCE


============================================================
27. STREAMLIT LEARNING PROJECTS
============================================================

Do not learn Streamlit only through theory.

Build projects.


------------------------------------------------------------
PROJECT 1 — Hello Streamlit
------------------------------------------------------------

Learn:

    title
    text
    markdown


------------------------------------------------------------
PROJECT 2 — Personal Profile
------------------------------------------------------------

Learn:

    inputs
    buttons
    layout


------------------------------------------------------------
PROJECT 3 — Calculator
------------------------------------------------------------

Learn:

    number_input
    selectbox
    button
    conditions


------------------------------------------------------------
PROJECT 4 — CSV DATA EXPLORER
------------------------------------------------------------

Learn:

    file_uploader
    Pandas
    dataframe
    filters
    charts
    download


------------------------------------------------------------
PROJECT 5 — ML PREDICTION APP
------------------------------------------------------------

Learn:

    model loading
    input widgets
    prediction
    caching
    visualization


------------------------------------------------------------
PROJECT 6 — DOCUMENT ANALYZER
------------------------------------------------------------

Learn:

    file upload
    PDF processing
    LLM
    session state
    download


------------------------------------------------------------
PROJECT 7 — AI CHATBOT
------------------------------------------------------------

Learn:

    st.chat_input()
    st.chat_message()
    Session State
    LLM API
    secrets
    error handling


------------------------------------------------------------
PROJECT 8 — RAG CHATBOT
------------------------------------------------------------

Learn:

    PDF upload
    chunking
    embeddings
    vector database
    retrieval
    LLM
    Streamlit


------------------------------------------------------------
PROJECT 9 — AI/ML DASHBOARD
------------------------------------------------------------

Learn:

    sidebar
    filters
    tabs
    columns
    Plotly
    Pandas
    caching


============================================================
28. FINAL STREAMLIT ARCHITECTURE
============================================================

Eventually you should be able to understand this:


                         USER
                          │
                          ↓
                  STREAMLIT FRONTEND
                          │
          ┌───────────────┼────────────────┐
          │               │                │
       Widgets         Layout          Chat UI
          │               │                │
          └───────────────┼────────────────┘
                          ↓
                   SESSION STATE
                          │
                          ↓
                    Python Logic
                          │
             ┌────────────┼────────────┐
             │            │            │
            API        Database       ML
             │            │            │
             └────────────┼────────────┘
                          ↓
                         LLM
                          │
                          ↓
                       Response
                          │
                          ↓
                    Streamlit UI


And for performance:


                    STREAMLIT
                        │
             ┌──────────┴──────────┐
             │                     │
       st.cache_data        st.cache_resource
             │                     │
       Cached DATA            Cached RESOURCE


And for persistence:


                    USER SESSION
                         │
                         ↓
                  st.session_state


And for configuration:


                    APPLICATION
                         │
             ┌───────────┴───────────┐
             │                       │
       config.toml              secrets.toml
                                     │
                                     ↓
                                st.secrets


============================================================
29. COMPANY-READY STREAMLIT CHECKLIST
============================================================

Before saying:

    "I know Streamlit"


You should be comfortable with:


BASICS
    [ ] Installation
    [ ] streamlit run
    [ ] Project structure
    [ ] requirements.txt


DISPLAY
    [ ] write
    [ ] text
    [ ] markdown
    [ ] title
    [ ] header
    [ ] subheader
    [ ] caption
    [ ] code
    [ ] latex


WIDGETS
    [ ] text_input
    [ ] text_area
    [ ] number_input
    [ ] slider
    [ ] select_slider
    [ ] selectbox
    [ ] multiselect
    [ ] radio
    [ ] checkbox
    [ ] toggle
    [ ] date_input
    [ ] time_input
    [ ] file_uploader
    [ ] color_picker
    [ ] feedback


INTERACTION
    [ ] button
    [ ] download_button
    [ ] link_button
    [ ] form_submit_button


EXECUTION
    [ ] rerun model
    [ ] execution order
    [ ] widget identity
    [ ] callbacks
    [ ] ephemeral widgets


STATE
    [ ] session_state
    [ ] initialization
    [ ] reading
    [ ] updating
    [ ] deleting
    [ ] widget keys
    [ ] callbacks + state


LAYOUT
    [ ] sidebar
    [ ] columns
    [ ] container
    [ ] expander
    [ ] tabs
    [ ] empty
    [ ] popover
    [ ] dialog


FORMS
    [ ] st.form
    [ ] st.form_submit_button


DATA
    [ ] dataframe
    [ ] table
    [ ] data_editor
    [ ] Pandas
    [ ] NumPy
    [ ] CSV
    [ ] JSON
    [ ] Excel
    [ ] Parquet


VISUALIZATION
    [ ] line_chart
    [ ] bar_chart
    [ ] area_chart
    [ ] scatter_chart
    [ ] Matplotlib
    [ ] Plotly
    [ ] Altair
    [ ] PyDeck


FILES
    [ ] upload
    [ ] download
    [ ] multiple files


CONFIGURATION
    [ ] config.toml
    [ ] secrets.toml
    [ ] st.secrets
    [ ] .gitignore


PERFORMANCE
    [ ] cache_data
    [ ] cache_resource
    [ ] state vs cache


URL
    [ ] query_params


ADVANCED
    [ ] multipage apps
    [ ] custom components
    [ ] loading states
    [ ] progress
    [ ] error handling
    [ ] logging
    [ ] testing


AI/ML
    [ ] ML model integration
    [ ] API integration
    [ ] LLM integration
    [ ] Chatbot
    [ ] RAG
    [ ] document processing
    [ ] embeddings
    [ ] vector database


PRODUCTION
    [ ] clean architecture
    [ ] security
    [ ] secrets management
    [ ] requirements
    [ ] Git/GitHub
    [ ] deployment
    [ ] monitoring


============================================================
30. YOUR LEARNING ORDER
============================================================

Do NOT try to learn everything simultaneously.

Follow this exact order:


PHASE 1 — BASICS

    Installation
        ↓
    Display elements
        ↓
    Input widgets
        ↓
    Buttons


PHASE 2 — STREAMLIT FUNDAMENTALS

    Rerun model
        ↓
    Widget state
        ↓
    Execution order
        ↓
    Callbacks


PHASE 3 — STATE

    st.session_state
        ↓
    Initialization
        ↓
    Updating
        ↓
    Widget keys
        ↓
    Chat history


PHASE 4 — UI

    Sidebar
        ↓
    Columns
        ↓
    Containers
        ↓
    Expander
        ↓
    Tabs
        ↓
    Popover/Dialog


PHASE 5 — FORMS

    st.form
        ↓
    st.form_submit_button


PHASE 6 — DATA

    Pandas
        ↓
    CSV
        ↓
    DataFrame
        ↓
    Filtering
        ↓
    Data editor


PHASE 7 — VISUALIZATION

    Native charts
        ↓
    Matplotlib
        ↓
    Plotly


PHASE 8 — FILES

    Upload
        ↓
    Process
        ↓
    Display
        ↓
    Download


PHASE 9 — CONFIGURATION

    config.toml
        ↓
    secrets.toml
        ↓
    st.secrets
        ↓
    Environment configuration


PHASE 10 — PERFORMANCE

    cache_data
        ↓
    cache_resource
        ↓
    Session State vs Cache


PHASE 11 — URL STATE

    st.query_params


PHASE 12 — AI/ML

    ML model
        ↓
    API
        ↓
    LLM
        ↓
    Chatbot
        ↓
    RAG


PHASE 13 — PRODUCTION

    Clean architecture
        ↓
    Error handling
        ↓
    Logging
        ↓
    Testing
        ↓
    Security
        ↓
    Deployment


============================================================
FINAL GOAL
============================================================

The goal is NOT:

    "I know Streamlit functions."


The goal is:

    "I can take a Python/AI/ML backend and build
     a professional interactive application around it."


For example:


    GEMINI API
        +
    Python
        +
    Streamlit
        +
    Session State
        +
    File Upload
        +
    Chat UI
        +
    Caching
        +
    Secrets
        +
    Error Handling
        +
    Clean Project Structure
        +
    Deployment

                ↓

          COMPANY-READY
           AI APPLICATION


============================================================
'''