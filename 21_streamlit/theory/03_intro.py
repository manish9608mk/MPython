'''
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

'''