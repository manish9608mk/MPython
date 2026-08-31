import streamlit as st
import pandas as pd


# PAGE CONFIGURATION
st.set_page_config(
    page_title="Job Hunt Command Center",
    page_icon="💼",
    layout="wide"
)


# LOAD DATA
df = pd.read_csv("04_job_applications.csv")


# HEADER
st.title("💼 Job Hunt Command Center")
st.caption("Track, analyze and manage your job applications.")


# SIDEBAR
with st.sidebar:

    st.header("⚙️ Dashboard Settings")

    role = st.selectbox(
        "Filter by Role",
        ["All"] + sorted(df["Role"].unique().tolist())
    )

    status = st.selectbox(
        "Filter by Status",
        ["All"] + sorted(df["Status"].unique().tolist())
    )


# FILTER DATA
filtered_df = df.copy()

if role != "All":
    filtered_df = filtered_df[
        filtered_df["Role"] == role
    ]

if status != "All":
    filtered_df = filtered_df[
        filtered_df["Status"] == status
    ]


# METRICS
st.subheader("📊 Application Overview")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "Total Applications",
        len(filtered_df)
    )

with col2:
    st.metric(
        "Applied",
        len(filtered_df[filtered_df["Status"] == "Applied"])
    )

with col3:
    st.metric(
        "Interviews",
        len(filtered_df[filtered_df["Status"] == "Interview"])
    )

with col4:
    st.metric(
        "Selected",
        len(filtered_df[filtered_df["Status"] == "Selected"])
    )


# DIVIDER
st.divider()


# DATA TABLE
st.subheader("📋 Job Applications")

st.dataframe(
    filtered_df,
    width="stretch",
    hide_index=True
)


# EXTRA INFORMATION
st.divider()

col1, col2 = st.columns(2)

with col1:

    st.subheader("🏢 Companies")

    companies = filtered_df["Company"].unique()

    for company in companies:
        st.write(f"• {company}")


with col2:

    st.subheader("📍 Locations")

    locations = filtered_df["Location"].unique()

    for location in locations:
        st.write(f"• {location}")





# Your CSV:
# 04_job_applications.csv
#         ↓
# pd.read_csv()
#         ↓
# DataFrame
#         ↓
# filter
#         ↓
# Streamlit
#         ↓
# Dashboard


# We're actually solving a real problem:

#                     JOB HUNT COMMAND CENTER
#                               │
#              ┌────────────────┴────────────────┐
#              │                                 │
#           SIDEBAR                           DATA
#              │                                 │
#        Role / Status                    Pandas DataFrame
#              │                                 │
#              └────────────────┬────────────────┘
#                               ↓
#                          FILTER DATA
#                               ↓
#                      ┌────────┴────────┐
#                      ↓                 ↓
#                   METRICS          APPLICATIONS
#                      │                 │
#                Total / Applied      DataFrame
#                Interview / Selected

               


# Application Tracker
#         │
#         ├── 📊 Overview
#         │     ├── Total Applications
#         │     ├── Interviews
#         │     ├── Selections
#         │     └── Rejections
#         │
#         ├── 🏢 Company Analysis
#         │     ├── Companies Applied
#         │     ├── Highest Paying Companies
#         │     └── Selection Rate
#         │
#         ├── 💼 Role Analysis
#         │     ├── SDE
#         │     ├── Cloud Engineer
#         │     └── DevOps Engineer
#         │
#         ├── 📍 Location Analysis
#         │     ├── Bangalore
#         │     ├── Hyderabad
#         │     ├── Pune
#         │     └── Delhi
#         │
#         └── 💰 Salary Analysis
#               ├── Average Salary
#               ├── Highest Salary
#               └── Salary by Role               
