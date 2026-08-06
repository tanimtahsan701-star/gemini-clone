
import streamlit as st
import google.generativeai as genai

# আপনার কপি করা ফ্রি জেমিনাই এপিআই কি নিচের লাইনে বসান
genai.configure(api_key="import os
from google import genai

client = genai.Client(
    api_key=os.environ.get("GEMINI_API_KEY"),
)

tools = [
    {
        'type': 'google_search',
    },
]

generation_config = {
    'temperature': 1,
    'max_output_tokens': 65536,
    'top_p': 0.95,
    'thinking_level': 'high',
}

interaction = client.interactions.create(
    model='models/gemini-3-flash-preview',
    input='',
    tools=tools,
    generation_config=generation_config,
)

print(interaction.steps[-1])


")
model = genai.GenerativeModel("gemini-1.5-flash")

st.set_page_config(page_title="Gemini Clone", layout="centered")
st.title("✦ Gemini Official Clone")

if "messages" not in st.session_state:
    st.session_state.messages = []

# চ্যাট হিস্ট্রি রেন্ডার করা
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# ইউজার ইনপুট ও এআই রেসপন্স
if prompt := st.chat_input("Ask Gemini anything..."):
    st.chat_message("user").markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    # জেমিনাই মডেল থেকে রেসপন্স জেনারেট করা
    response = model.generate_content(prompt)
    
    with st.chat_message("assistant"):
        st.markdown(response.text)
    st.session_state.messages.append({"role": "assistant", "content": response.text})



