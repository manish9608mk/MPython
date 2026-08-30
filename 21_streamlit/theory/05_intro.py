'''
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

'''