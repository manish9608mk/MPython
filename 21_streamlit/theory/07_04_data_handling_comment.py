import streamlit as st
import pandas as pd


# ============================================================
# 1. PAGE CONFIGURATION
# ============================================================
# Configure the basic settings of our Streamlit application.
#
# page_title → Name shown in the browser tab
# page_icon  → Icon shown in the browser tab
# layout     → "wide" gives us more horizontal space
# ============================================================

st.set_page_config(
    page_title="Job Hunt Command Center",
    page_icon="💼",
    layout="wide"
)


# ============================================================
# 2. LOAD DATA
# ============================================================
# Read our CSV file using Pandas.
#
# CSV
#  ↓
# pd.read_csv()
#  ↓
# Pandas DataFrame
#
# The DataFrame 'df' now contains all job applications.
# ============================================================

df = pd.read_csv("04_job_applications.csv")


# ============================================================
# 3. HEADER
# ============================================================
# Display the main title and a short description
# at the top of the dashboard.
# ============================================================

st.title("💼 Job Hunt Command Center")

st.caption(
    "Track, analyze and manage your job applications."
)


# ============================================================
# 4. SIDEBAR
# ============================================================
# The sidebar contains controls that allow the user
# to filter the job application data.
#
# We currently have two filters:
#
# 1. Role
# 2. Status
#
# Example:
# Role   → Cloud Engineer
# Status → Applied
#
# This means:
# "Show me only Cloud Engineer jobs that I applied for."
# ============================================================

with st.sidebar:

    st.header("⚙️ Dashboard Settings")


    # --------------------------------------------------------
    # Filter 1: Job Role
    # --------------------------------------------------------
    # Get all unique roles from the DataFrame.
    #
    # unique()
    #    ↓
    # Unique roles
    #
    # tolist()
    #    ↓
    # Convert them into a Python list
    #
    # sorted()
    #    ↓
    # Sort the roles alphabetically
    #
    # ["All"] + ...
    #    ↓
    # Add "All" as the first option
    # --------------------------------------------------------

    role = st.selectbox(
        "Filter by Role",
        ["All"] + sorted(df["Role"].unique().tolist())
    )


    # --------------------------------------------------------
    # Filter 2: Application Status
    # --------------------------------------------------------
    # Same idea as the Role filter.
    #
    # Example statuses:
    # Applied
    # Interview
    # Rejected
    # Selected
    # --------------------------------------------------------

    status = st.selectbox(
        "Filter by Status",
        ["All"] + sorted(df["Status"].unique().tolist())
    )


# ============================================================
# 5. FILTER DATA
# ============================================================
# First create a copy of the complete DataFrame.
#
# Why copy?
# We don't want to modify the original 'df'.
#
# df
# ↓
# Complete original data
#
# filtered_df
# ↓
# Data after applying user's filters
# ============================================================

filtered_df = df.copy()


# ------------------------------------------------------------
# Apply Role Filter
# ------------------------------------------------------------
# If the user selects a specific role,
# keep only rows having that role.
#
# Example:
#
# role = "Cloud Engineer"
#
# df["Role"] == "Cloud Engineer"
#              ↓
#       True / False values
#
# Then DataFrame filtering keeps only True rows.
# ------------------------------------------------------------

if role != "All":

    filtered_df = filtered_df[
        filtered_df["Role"] == role
    ]


# ------------------------------------------------------------
# Apply Status Filter
# ------------------------------------------------------------
# If the user selects a specific status,
# keep only rows having that status.
#
# Example:
#
# status = "Applied"
#
# Only applications with Status == "Applied"
# will remain in filtered_df.
# ------------------------------------------------------------

if status != "All":

    filtered_df = filtered_df[
        filtered_df["Status"] == status
    ]


# ============================================================
# 6. APPLICATION METRICS
# ============================================================
# Display important numbers at the top of the dashboard.
#
# These metrics are calculated from filtered_df,
# NOT from the original df.
#
# Therefore, when the user changes a filter,
# these numbers automatically change.
# ============================================================

st.subheader("📊 Application Overview")


# Create 4 columns so that the metrics appear
# horizontally next to each other.
# ============================================================

col1, col2, col3, col4 = st.columns(4)


# ------------------------------------------------------------
# Metric 1: Total Applications
# ------------------------------------------------------------
# len(filtered_df)
#     ↓
# Number of rows remaining after filtering
# ============================================================

with col1:

    st.metric(
        "Total Applications",
        len(filtered_df)
    )


# ------------------------------------------------------------
# Metric 2: Applied
# ------------------------------------------------------------
# First select rows where:
#
# Status == "Applied"
#
# Then len() counts those rows.
# ============================================================

with col2:

    st.metric(
        "Applied",
        len(
            filtered_df[
                filtered_df["Status"] == "Applied"
            ]
        )
    )


# ------------------------------------------------------------
# Metric 3: Interviews
# ------------------------------------------------------------
# Count applications whose status is "Interview".
# ============================================================

with col3:

    st.metric(
        "Interviews",
        len(
            filtered_df[
                filtered_df["Status"] == "Interview"
            ]
        )
    )


# ------------------------------------------------------------
# Metric 4: Selected
# ------------------------------------------------------------
# Count applications whose status is "Selected".
# ============================================================

with col4:

    st.metric(
        "Selected",
        len(
            filtered_df[
                filtered_df["Status"] == "Selected"
            ]
        )
    )


# ============================================================
# 7. DIVIDER
# ============================================================
# Visually separate the metrics section from the
# job application table.
# ============================================================

st.divider()


# ============================================================
# 8. JOB APPLICATION TABLE
# ============================================================
# Display the filtered DataFrame as an interactive table.
#
# The table automatically changes whenever the user
# changes Role or Status filters.
# ============================================================

st.subheader("📋 Job Applications")


st.dataframe(
    filtered_df,

    # Make the table use the available width.
    width="stretch",

    # Don't display Pandas row numbers.
    hide_index=True
)


# ============================================================
# 9. EXTRA INFORMATION
# ============================================================
# Display additional information about:
#
# 1. Companies
# 2. Locations
#
# We use two columns to show them side by side.
# ============================================================

st.divider()


col1, col2 = st.columns(2)


# ============================================================
# 10. COMPANY LIST
# ============================================================
# Get unique company names from filtered_df.
#
# unique()
#    ↓
# Removes duplicate company names
#
# Example:
#
# Amazon
# Amazon
# Google
# Microsoft
#
# becomes:
#
# Amazon
# Google
# Microsoft
# ============================================================

with col1:

    st.subheader("🏢 Companies")

    companies = filtered_df["Company"].unique()


    # Display each company as a bullet point.
    # ========================================================

    for company in companies:

        st.write(f"• {company}")


# ============================================================
# 11. LOCATION LIST
# ============================================================
# Get unique locations from the filtered DataFrame.
#
# Example:
#
# Bangalore
# Hyderabad
# Bangalore
# Pune
#
# becomes:
#
# Bangalore
# Hyderabad
# Pune
# ============================================================

with col2:

    st.subheader("📍 Locations")

    locations = filtered_df["Location"].unique()


    # Display each location as a bullet point.
    # ========================================================

    for location in locations:

        st.write(f"• {location}")


# ============================================================
# PROJECT ARCHITECTURE / LEARNING NOTES
# ============================================================
#
# These are ONLY comments for learning.
# Python will completely ignore them.
#
#
# CSV FILE
#    │
#    ▼
# pd.read_csv()
#    │
#    ▼
# Pandas DataFrame (df)
#    │
#    ▼
# Sidebar Filters
#    │
#    ├── Role
#    │
#    └── Status
#    │
#    ▼
# Filter Data
#    │
#    ▼
# filtered_df
#    │
#    ├───────────────┐
#    │               │
#    ▼               ▼
# Metrics          Applications
#    │               │
#    │               ▼
#    │           DataFrame Table
#    │
#    ▼
# Total / Applied / Interview / Selected
#
#
# ============================================================
# FUTURE PROJECT ROADMAP
# ============================================================
#
# Job Hunt Command Center
#         │
#         ├── 📊 Overview
#         │     ├── Total Applications
#         │     ├── Applied
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
#         │     ├── Software Engineer
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
#
# ============================================================