'''
STREAMLIT LAYOUT

sidebar
    → left-side controls and settings
    → st.sidebar

columns
    → arrange content side-by-side
    → st.columns()

container
    → group related content together
    → st.container()

tabs
    → divide content into separate sections
    → st.tabs()

expander
    → hide/show additional content
    → st.expander()

divider
    → visually separate sections
    → st.divider()


STREAMLIT DISPLAY & UI COMPONENTS

image
    → display images
    → st.image()

metric
    → display important numbers or statistics
    → st.metric()

progress
    → display progress/status
    → st.progress()

empty
    → create a placeholder that can be updated later
    → st.empty()

markdown
    → display formatted text using Markdown
    → st.markdown()


PAGE CONFIGURATION

st.set_page_config()
    → configure page title, icon, layout, etc.


IMPORTANT LAYOUT CONCEPT

with st.sidebar:
    → content goes inside the sidebar

with st.container():
    → content is grouped inside a container

with tab1:
    → content appears inside that tab

with st.expander():
    → content can be expanded/collapsed

with col1:
    → content appears inside that column
----------------------------------------------------------
LAYOUT
├── sidebar
├── columns
├── container
├── tabs
├── expander
└── divider

DISPLAY / UI
├── image
├── metric
├── progress
├── empty
└── markdown

PAGE
└── set_page_config()
'''

import streamlit as st


# PAGE CONFIGURATION
st.set_page_config(
    page_title="Cloud Engineer Command Center",
    page_icon="☁️",
    layout="wide"
)


# MAIN TITLE
st.title("☁️ Cloud Engineer Command Center")
st.caption("A personal dashboard for tracking cloud engineering progress.")


# SIDEBAR
with st.sidebar:

    st.header("⚙️ Dashboard Settings")

    role = st.selectbox(
        "Choose your role:",
        [
            "Cloud Engineer",
            "DevOps Engineer",
            "Platform Engineer",
            "SRE"
        ]
    )

    experience = st.slider(
        "Years of Experience:",
        min_value=0,
        max_value=10,
        value=2
    )

    show_details = st.checkbox(
        "Show detailed information"
    )

    st.divider()

    st.write("### 🎯 Current Focus")

    focus = st.radio(
        "Choose your focus:",
        [
            "AWS",
            "Docker",
            "Kubernetes",
            "Terraform"
        ]
    )



# IMAGE
st.image(
    "https://images.unsplash.com/photo-1451187580459-43490279c0fa",
    caption="Cloud Engineering",
    width="stretch"
)


# CONTAINER
with st.container(border=True):

    st.subheader("📊 Cloud Engineering Overview")

    # COLUMNS
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric(
            "AWS Services",
            12,
            "+4"
        )

    with col2:
        st.metric(
            "Projects",
            5,
            "+1"
        )

    with col3:
        st.metric(
            "Certifications",
            3,
            "+1"
        )

    with col4:
        st.metric(
            "Experience",
            f"{experience} Years"
        )



# DIVIDER
st.divider()


# PROGRESS
st.subheader("🚀 Learning Progress")

progress = {
    "Python": 95,
    "AWS": 70,
    "Docker": 60,
    "Kubernetes": 40,
    "Terraform": 30
}

for skill, value in progress.items():

    st.write(f"**{skill} — {value}%**")

    st.progress(value / 100)


# TABS
st.divider()

tab1, tab2, tab3 = st.tabs(
    [
        "👨‍💻 Profile",
        "🛠️ Skills",
        "🚀 Projects"
    ]
)


# PROFILE TAB
with tab1:

    st.header("👨‍💻 Profile")

    col1, col2 = st.columns(2)

    with col1:

        st.write(f"**Role:** {role}")
        st.write(f"**Experience:** {experience} years")
        st.write(f"**Current Focus:** {focus}")

    with col2:

        if show_details:

            st.info(
                "Interested in building scalable cloud "
                "infrastructure, automation and reliable systems."
            )

        else:

            st.write(
                "Enable detailed information from the sidebar."
            )


# SKILLS TAB
with tab2:

    st.header("🛠️ Technical Skills")

    col1, col2, col3 = st.columns(3)

    with col1:

        st.write("🐍 Python")
        st.write("🐧 Linux")

    with col2:

        st.write("☁️ AWS")
        st.write("🐳 Docker")

    with col3:

        st.write("☸️ Kubernetes")
        st.write("🔧 Terraform")



# PROJECTS TAB
with tab3:

    st.header("🚀 Projects")

    # Container 1
    with st.container(border=True):

        st.subheader("☁️ AWS Cloud Deployment")

        st.write(
            "Deploy a Python application on AWS "
            "using cloud infrastructure."
        )

        st.progress(0.75)

    # Container 2
    with st.container(border=True):

        st.subheader("🐳 Dockerized Application")

        st.write(
            "Containerize a Python application "
            "using Docker."
        )

        st.progress(0.60)

    # Container 3
    with st.container(border=True):

        st.subheader("☸️ Kubernetes Deployment")

        st.write(
            "Deploy and manage containers using Kubernetes."
        )

        st.progress(0.40)


# EXPANDER
st.divider()

with st.expander("📚 About this dashboard"):

    st.write(
        "This dashboard demonstrates important "
        "Streamlit layout and UI components."
    )

    st.write(
        "It uses sidebar, columns, containers, tabs, "
        "expanders, dividers, images, metrics and progress bars."
    )


# EMPTY
st.divider()

status = st.empty()

if show_details:

    status.success(
        f"Dashboard configured for {role}."
    )

else:

    status.info(
        "Enable detailed information from the sidebar."
    )