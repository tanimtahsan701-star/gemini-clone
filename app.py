
import streamlit as st
import requests

# ১. ব্রাউজারের ট্যাব নাম এবং আইকন (Gemini Style)
st.set_page_config(page_title="Tanim 2.0", layout="centered", page_icon="✨")

# ২. চ্যাটজিপিটি ও জেমিনাইয়ের মতো সুন্দর ডার্ক-মডার্ন ব্র্যান্ডিং ডিজাইন (CSS)
st.markdown("""
    <style>
    /* ব্যাকগ্রাউন্ড কালার পরিবর্তন */
    .stApp {
        background-color: #131314;
        color: #e3e3e3;
    }
    /* মেইন টাইটেল ও লোগো স্টাইল */
    .brand-title {
        font-size: 40px;
        font-weight: 700;
        background: linear-gradient(45deg, #4285F4, #9B51E0, #FF6B6B);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-align: center;
        margin-bottom: 5px;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }
    .brand-subtitle {
        text-align: center;
        color: #8e918f;
        font-size: 16px;
        margin-bottom: 40px;
    }
    /* ইনপুট বক্স ডিজাইন */
    .stChatInputContainer {
        border-radius: 28px !important;
        background-color: #1e1f20 !important;
        border: 1px solid #3c4043 !important;
    }
    </style>
""", unsafe_allowed_html=True)

# ৩. স্ক্রিনের মাঝখানে জেমিনাই স্টাইলে কাস্টম ব্র্যান্ড লোগো ও নাম
st.markdown('<div class="brand-title">✦ Tanim 2.0</div>', unsafe_allowed_html=True)
st.markdown('<div class="brand-subtitle">Your personalized ultra-smart AI Assistant</div>', unsafe_allowed_html=True)

API_URL = "https://huggingface.co"

if "messages" not in st.session_state:
    st.session_state.messages = []

# চ্যাট মেসেজ রেন্ডার করা
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# ইউজার ইনপুট ও এআই রেসপন্স
if prompt := st.chat_input("Ask Tanim 2.0 anything..."):
    st.chat_message("user").markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    payload = {"inputs": prompt, "parameters": {"max_new_tokens": 600}}
    
    try:
        res = requests.post(API_URL, json=payload)
        if res.status_code == 200:
            response_json = res.json()
            reply = response_json['generated_text'].replace(prompt, "").strip()
        else:
            reply = "এআই সার্ভারটি এই মুহূর্তে কিছুটা ব্যস্ত। দয়া করে ১ সেকেন্ড পর আবার মেসেজ দিন।"
    except:
        reply = "অপেক্ষা করার জন্য ধন্যবাদ! দয়া করে আপনার প্রশ্নটি আবার টাইপ করুন।"
        
    with st.chat_message("assistant"):
        st.markdown(reply)
    st.session_state.messages.append({"role": "assistant", "content": reply})
    




   

   


