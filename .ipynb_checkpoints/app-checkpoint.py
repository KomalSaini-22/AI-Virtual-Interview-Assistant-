# import streamlit as st

# st.set_page_config(
#     page_title="AI Virtual Interview Assistant",
#     page_icon="🤖",
#     layout="wide"
# )

# st.title("🤖 AI Virtual Interview Assistant")

# st.write("Welcome to AI Interview Assistant")

import streamlit as st

st.set_page_config(
    page_title="AI Virtual Interview Assistant",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 AI Virtual Interview Assistant")

st.write("Welcome to AI Virtual Interview Assistant")

st.markdown("---")

name = st.text_input("Enter Your Name")

interview_type = st.selectbox(
    "Select Interview Type",
    ["HR Interview", "Technical Interview", "Mixed Interview"]
)

difficulty = st.selectbox(
    "Select Difficulty",
    ["Easy", "Medium", "Hard"]
)

if st.button("Start Interview"):
    st.success(f"Welcome {name}")
    st.write(f"Interview Type : {interview_type}")
    st.write(f"Difficulty : {difficulty}")