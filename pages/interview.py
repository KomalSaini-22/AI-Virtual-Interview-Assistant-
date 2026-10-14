# import streamlit as st
# from utils.ai import get_questions

# st.title("💼 Interview")

# questions = get_questions()

# for i, question in enumerate(questions):
#     st.subheader(f"Question {i+1}")
#     st.write(question)

#     st.text_area(
#         "Your Answer",
#         key=f"answer_{i}"
#     )



##  if st.button("Submit Interview"):
##   st.success("Interview Submitted Successfully!")


# import streamlit as st

# from utils.ai import get_questions
# from utils.score import calculate_score
# from utils.db import save_answer

# st.title("💼 AI Interview")

# questions = get_questions()

# answers = []

# for i, question in enumerate(questions):

#     st.subheader(f"Question {i+1}")

#     st.write(question)

#     ans = st.text_area("Answer", key=i)

#     answers.append(ans)


# if st.button("Submit Interview"):

#     for q, a in zip(questions, answers):

#         score = calculate_score(a)

#         save_answer(q, a, score)

#     st.success("Interview Saved Successfully")



import streamlit as st
from utils.ai import get_questions, evaluate

st.title("💼 AI Interview")

questions = get_questions()

answers = []

for i, question in enumerate(questions):

    st.subheader(f"Question {i+1}")

    st.write(question)

    ans = st.text_area("Answer", key=i)

    answers.append(ans)

if st.button("Submit Interview"):

    st.success("Interview Submitted Successfully!")

    st.markdown("---")

    st.header("🤖 AI Feedback")

    for i, ans in enumerate(answers):

        st.subheader(f"Question {i+1}")

        if ans.strip() == "":
            st.warning("No Answer Given")
        else:
            feedback = evaluate(ans)

            st.write(feedback)