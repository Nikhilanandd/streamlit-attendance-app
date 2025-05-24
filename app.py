import streamlit as st
import pandas as pd
import os
import matplotlib.pyplot as plt

# Load college list
college_file = 'colleges.csv'
college_df = pd.read_csv(college_file)
colleges = college_df['College Name'].tolist()
colleges.append("Other")

# Attendance file
attendance_file = "attendance.csv"
if not os.path.exists(attendance_file):
    pd.DataFrame(columns=["Name", "Email", "College"]).to_csv(attendance_file, index=False)

st.title("📋 Tech-Leads Training Day Attendance")

# --- Form for Attendance ---
st.header("Mark Your Attendance")

with st.form("attendance_form"):
    name = st.text_input("Your Name")
    email = st.text_input("Email ID")

    college_choice = st.selectbox("Select Your College", colleges)
    
    # If "Other" is selected, show separate input box
    if college_choice == "Other":
        college_name = st.text_input("Enter Your College Name (if not in the list)")
    else:
        college_name = college_choice

    submitted = st.form_submit_button("Submit")

    if submitted:
        if not name or not email or not college_name:
            st.error("Please fill in all fields.")
        else:
            new_data = pd.DataFrame([[name, email, college_name]], columns=["Name", "Email", "College"])
            new_data.to_csv(attendance_file, mode='a', index=False, header=False)
            st.success("✅ Attendance Recorded Successfully!")

# --- Visualization Section ---
st.header("📊 College-wise Attendance Stats")

if os.path.exists(attendance_file):
    df = pd.read_csv(attendance_file)
    college_counts = df['College'].value_counts()

    st.bar_chart(college_counts)
