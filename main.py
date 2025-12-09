import streamlit as st
import streamlit.components.v1 as components

st.title("Open ChatGPT from Streamlit")

chat_text = "hi how are you today"
url = f"https://chat.openai.com/?q={chat_text}"

if st.button("Open ChatGPT Window"):
    components.html(
        f"""
        <script>
            window.open("{url}", "_blank");
        </script>
        """,
        height=0,
    )
