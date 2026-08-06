import streamlit as st
import requests

st.set_page_config(page_title="Tanim 2.0", layout="centered")
st.title("✦ Tanim 2.0")

# সম্পূর্ণ উন্মুক্ত ও শক্তিশালী Qwen মডেল (যা কোনো চাবি ছাড়াই আনলিমিটেড চলবে)
API_URL = "https://huggingface.co"

if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

if prompt := st.chat_input("Ask Tanim 2.0 anything..."):
    st.chat_message("user").markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    payload = {"inputs": prompt, "parameters": {"max_new_tokens": 500}}
    
    try:
        res = requests.post(API_URL, json=payload)
        # সার্ভার থেকে সঠিক উত্তরটি বের করা
        if res.status_code == 200:
            response_json = res.json()
            reply = response_json[0]['generated_text'].replace(prompt, "").strip()
        else:
            reply = "এআই সার্ভারটি এই মুহূর্তে কিছুটা ব্যস্ত। দয়া করে ১ সেকেন্ড পর আবার মেসেজ দিন।"
    except:
        reply = "অপেক্ষা করার জন্য ধন্যবাদ! দয়া করে আপনার প্রশ্নটি আবার টাইপ করুন।"
        
    with st.chat_message("assistant"):
        st.markdown(reply)
    st.session_state.messages.append({"role": "assistant", "content": reply})


   

   


