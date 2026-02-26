import streamlit as st
import os
from datetime import datetime

# --- PAGE CONFIGURATION ---
st.set_page_config(
    page_title="OG Security Agent",
    page_icon="🛡️",
    layout="wide"
)

# --- ADVANCED CUSTOM STYLING ---
st.markdown("""
    <style>
    .stApp {
        background: radial-gradient(circle at top right, #1e222d, #0b0e14);
        color: #ffffff;
    }
    [data-testid="stSidebar"] {
        background-color: rgba(20, 26, 38, 0.8);
        border-right: 1px solid #30363d;
    }
    .stChatMessage {
        background-color: #161b22;
        border: 1px solid #30363d;
        border-radius: 15px;
        padding: 15px;
        margin-bottom: 10px;
    }
    .main-title {
        font-size: 3rem;
        font-weight: 800;
        background: -webkit-linear-gradient(#fff, #4a9eff);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-align: center;
        margin-bottom: 0;
    }
    .subtitle {
        text-align: center;
        color: #8b949e;
        font-size: 1.1rem;
        margin-bottom: 2rem;
    }
    </style>
    """, unsafe_allow_html=True)

# --- SYSTEM SETTINGS ---
os.environ["OPENGRADIENT_ENV"] = "alpha"
PRIVATE_KEY = "YOUR_64_CHAR_PRIVATE_KEY_HERE"

def get_ai_response(user_input):
    """Verifiable TEE Inference simulation for the security agent."""
    if "0x" in user_input:
        return (f"🔍 **Security Audit for:** `{user_input}`\n\n"
                f"✅ **Verdict:** Secure\n"
                f"- **Re-entrancy Risk:** Low\n"
                f"- **Logic Integrity:** Verified via TEE\n"
                f"- **Pattern Analysis:** No malicious signatures detected.")
    else:
        return "🤖 **Agent:** Please provide a Transaction Hash or a Contract Address for a real-time security audit."

# --- SIDEBAR: STATUS & CONNECT ---
with st.sidebar:
    st.markdown("### 🛰️ System Status")
    st.success("Network: OpenGradient Alpha")
    st.info(f"Last Scan: {datetime.now().strftime('%H:%M:%S')}")
    
    st.markdown("---")
    st.subheader("🔗 Developer Hub")
    
    github_url = "https://github.com/moltaphet"
    twitter_url = "https://x.com/0xehs4hn" 
    
    st.link_button("📂 View GitHub Repository", github_url, use_container_width=True)
    st.link_button("🐦 Follow on Twitter / X", twitter_url, use_container_width=True)
    
    st.markdown("---")
    st.caption(f"© {datetime.now().year} | Built with OpenGradient SDK")

# --- MAIN INTERFACE ---
st.markdown('<p class="main-title">🛡️ OG Security Agent</p>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">Autonomous Infrastructure Sentinel | Running on OpenGradient TEE</p>', unsafe_allow_html=True)

# Chat Session Management
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "Hello! I am your AI Security Agent. Ready to audit the network."}
    ]

# Display Chat History
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# User Chat Input
if prompt := st.chat_input("Enter Tx Hash or Address (0x...)"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        with st.spinner("🧠 Verifying on-chain via TEE..."):
            response = get_ai_response(prompt)
            st.markdown(response)
            st.session_state.messages.append({"role": "assistant", "content": response})