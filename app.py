import streamlit as st
from prompts import create_prompt
from backend import generate_output


# Initialize prompt history
if "history" not in st.session_state:
    st.session_state.history = []


# App title
st.title("Universal AI Utility 🤖")


# Select task
task = st.selectbox(
    "Select Task",
    [
        "📝 Summarize",
        "🌍 Translate",
        "💡 Explain",
        "✉️ Generate Email",
        "✍️ Rewrite"
    ]
)


# User input
text = st.text_area("Enter Input")


# Word limit
word_limit = st.slider(
    "Word Limit",
    min_value=50,
    max_value=500,
    value=150,
    step=50
)


# Translation language
option = ""

if task == "🌍 Translate":
    option = st.selectbox(
        "Language",
        [
            "French",
            "Hindi",
            "Spanish"
        ]
    )


# Generate button
if st.button("Generate"):

    if text:

        # Create prompt
        prompt = create_prompt(
            task,
            text,
            option,
            word_limit
        )

        # Display prompt
        st.subheader("Prompt")
        st.code(prompt)

        # Generate output
        output = generate_output(prompt)

        # Save to history
        st.session_state.history.append({
            "task": task,
            "prompt": prompt,
            "output": output
        })

        # Display output
        st.subheader("Output")
        st.write(output)

        # Download output
        st.download_button(
            label="⬇️ Download Output",
            data=output,
            file_name="ai_output.txt",
            mime="text/plain"
        )

    else:

        st.warning("Provide input")


# Prompt History
st.subheader("📜 Prompt History")


for item in st.session_state.history:

    st.write("Task:", item["task"])

    st.write("Prompt:")
    st.code(item["prompt"])

    st.write("Output:")
    st.write(item["output"])

    st.divider()


# Clear History button
if st.session_state.history:

    if st.button("🗑️ Clear History"):

        st.session_state.history = []

        st.rerun()