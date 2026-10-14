# import streamlit as st

# st.title("📜 History")

# st.write("Previous Interviews")


import streamlit as st

from utils.db import get_all_data

st.title("Interview History")

data = get_all_data()

for row in data:

    st.write("-------------------------")

    st.write("Question :", row[1])

    st.write("Answer :", row[2])

    st.write("Score :", row[3])