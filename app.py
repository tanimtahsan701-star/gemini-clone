import streamlit as st
import google.generativeai as genai

# এখানে আপনার আসল API KEY বসাবেন
genai.configure(api_key="AQ.Ab8RN6IgQ8_muycUXA1u3hCpSBmVaXmiF6HvdEcyvWrsxpfp3Q")
model = genai.GenerativeModel("gemini-1.5-flash")

st.set_page_config(page_title="Gemini Clone", layout="centered")
st.title("✦ Tanim 2.o")

if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

if prompt := st.chat_input("Ask Gemini anything..."):
    st.chat_message("user").markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    response = model.generate_content(prompt)
    
    with st.chat_message("assistant"):
        st.markdown(response.text)
    st.session_state.messages.append({"role": "assistant", "content": response.text})



   


