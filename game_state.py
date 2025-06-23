import streamlit as st

def init_state():
    if "score" not in st.session_state:
        st.session_state.score = {
            "duty": 0,
            "karma": 0,
            "virtue": 0,
            "truth": 0,
            "ego": 0,
            "utility": 0
        }

def update_score(values):
    for k, v in values.items():
        st.session_state.score[k] += v
