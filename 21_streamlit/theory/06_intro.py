'''
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

'''