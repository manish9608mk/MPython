'''
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

'''