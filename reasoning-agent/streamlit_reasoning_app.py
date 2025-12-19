import streamlit as st
from agent import ReasoningAgent
import time

st.set_page_config(
    page_title="Multi-Reasoning Step Agent",
    layout="centered"
)

# HEADER
st.title("🧠 Multi-Reasoning Step Agent")

st.markdown(
    "Ask **any reasoning-based question**. "
    "The agent plans, executes, verifies — and returns a clean final answer."
)

st.divider()

# INPUT
question = st.text_input(
    "Enter your question",
    placeholder="e.g., Alice has 3 red apples and twice as many green apples..."
)

run_btn = st.button("Generate Answer")

# STATE
if "status_message" not in st.session_state:
    st.session_state.status_message = ""

if "result" not in st.session_state:
    st.session_state.result = None

# ACTION
if run_btn:
    if not question.strip():
        st.warning("Please enter a question.")
    else:
        st.session_state.status_message = "Thinking (Planning → Executing → Verifying…)"
        st.session_state.result = None
        # show spinner while agent is working
        with st.spinner(st.session_state.status_message):
            agent = ReasoningAgent()
            result = agent.run(question)
            st.session_state.result = result
            # small delay to show spinner effect
            time.sleep(0.5)
        st.session_state.status_message = "Reasoning Complete"

# STATUS MESSAGE
if st.session_state.status_message:
    st.info(st.session_state.status_message)

# OUTPUT
if st.session_state.result:
    result = st.session_state.result
    answer = result["answer"]
    reasoning = result["reasoning_visible_to_user"]

    # Display answer on its own line
    st.success(f"Answer: {answer}")

    # Display reasoning in paragraph below
    st.markdown(reasoning)

    # Interpretations & Debug Data Tab
    with st.expander("📊 Interpretations & Debug Data"):
        st.json(result)