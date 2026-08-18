def create_prompt(task, text, option, word_limit):

    if task == "📝 Summarize":
        return f"""
Summarize the following text in maximum {word_limit} words.
Use concise bullet points.

Text:
{text}
"""

    elif task == "🌍 Translate":
        return f"""
Translate the following text to {option}.

Text:
{text}
"""

    elif task == "💡 Explain":
        return f"""
Explain the following topic using beginner-friendly language.

Topic:
{text}
"""

    elif task == "✉️ Generate Email":
        return f"""
Generate a professional email.

Purpose:
{text}
"""

    elif task == "✍️ Rewrite":
        return f"""
Rewrite the following content in a professional tone.

Text:
{text}
"""