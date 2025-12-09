import streamlit as st

st.title("Open ChatGPT From Streamlit")

# JavaScript trick to open new tab
chat_text = "hi how are you today"
url = f"https://chat.openai.com/?q={chat_text}"

if st.button("Open ChatGPT Window"):
    js = f"window.open('{url}', '_blank').focus();"
    st.markdown(f"<script>{js}</script>", unsafe_allow_html=True)
