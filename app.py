import streamlit as st
import requests

st.set_page_config(page_title="Tanim 2.0", layout="centered")
st.title("✦ Tanim 2.0")

# মেটার শক্তিশালী Llama-3 মডেল (সম্পূর্ণ ফ্রি এবং এপিআই কি ছাড়া চলবে)
API_URL = "https://huggingface.co"

if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

if prompt := st.chat_input("Ask Tanim 2.0 anything..."):
    st.chat_message("user").markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    # ফ্রি এআই রেসপন্স জেনারেট করা
    payload = {"inputs": prompt, "parameters": {"max_new_tokens": 1000}}
    response = requests.post(API_URL, json=payload).json()
    
    try:
        reply = response[0]['generated_text'].replace(prompt, "").strip()
    except:
        reply = "দুঃখিত, সার্ভার কিছুটা ব্যস্ত। দয়া করে আবার চেষ্টা করুন।"
        
    with st.chat_message("assistant"):
        st.markdown(reply)
    st.session_state.messages.append({"role": "assistant", "content": reply})

   

   


