import streamlit as st
from dilemmas import dilemmas
from philosophers import philosopher_prompts
from llama_groq import query_llama

st.set_page_config(page_title="Dharma Dilemma", layout="centered")

st.title("🧠 Dharma Dilemma: Ethical Philosophy Game")

# Step 1: Select a dilemma
selected = st.selectbox("Choose a Dilemma", [d['title'] for d in dilemmas])
dilemma = next(d for d in dilemmas if d['title'] == selected)

st.subheader(dilemma["title"])
st.write(dilemma["description"])

# Step 2: Make a choice
choice = st.radio("What will you do?", [c['text'] for c in dilemma['choices']])

# Step 3: Select a philosopher
philosopher = st.selectbox("Choose a philosopher", list(philosopher_prompts.keys()))

if st.button("Get Feedback"):
    full_prompt = (
        f"Scenario: {dilemma['description']}\n"
        f"Your choice: {choice}\n\n"
        f"{philosopher_prompts[philosopher]}"
    )
    with st.spinner("Summoning wisdom..."):
        response = query_llama(full_prompt)
    st.markdown("### 🧙 Philosopher's Response:")
    st.write(response)
