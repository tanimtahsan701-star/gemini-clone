import streamlit as st
import requests

# ১. অ্যাপের ব্রাউজার নাম ও লোগো সেট করা
st.set_page_config(page_title="Tanim Gemini 2.0", layout="centered", page_icon="✨")

# ২. মেইন স্ক্রিনে আপনার পছন্দের নাম
st.title("✦ Tanim 2.0")
st.caption("Your personalized ultra-smart AI Assistant")

# ৩. ফ্রি এআই মডেল লিংক
API_URL = "https://huggingface.co"

if "messages" not in st.session_state:
    st.session_state.messages = []

# চ্যাট মেসেজ হিস্ট্রি স্ক্রিনে দেখানো
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# ইউজার ইনপুট ও এআই রেসপন্স প্রসেস
if prompt := st.chat_input("Ask Tanim Gemini anything..."):
    st.chat_message("user").markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    payload = {"inputs": prompt, "parameters": {"max_new_tokens": 500}}
    
    try:
        res = requests.post(API_URL, json=payload)
        if res.status_code == 200:
            response_json = res.json()
            if isinstance(response_json, list):
                reply = response_json[0]['generated_text'].replace(prompt, "").strip()
            else:
                reply = response_json['generated_text'].replace(prompt, "").strip()
        else:
            reply = "এআই সার্ভারটি এই মুহূর্তে কিছুটা ব্যস্ত। দয়া করে ১ সেকেন্ড পর আবার মেসেজ দিন।"
    except:
        reply = "অপেক্ষা করার জন্য ধন্যবাদ! দয়া করে আপনার প্রশ্নটি আবার টাইপ করুন।"
        
    with st.chat_message("assistant"):
        st.markdown(reply)
    st.session_state.messages.append({"role": "assistant", "content": reply})



