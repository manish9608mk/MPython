'''
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

'''