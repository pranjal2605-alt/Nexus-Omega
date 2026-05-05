import streamlit as st
import time

# --- CONFIG ---
st.set_page_config(page_title="Nexus", layout="wide", initial_sidebar_state="collapsed")

# --- CSS: THE "EMERGENT" SPEC ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@900&family=JetBrains+Mono:wght@700&display=swap');
    
    :root { --volt: #CDFF00; --bg: #000; --border: #1A1A1A; --gray: #888; }

    /* PURE BLACK CANVAS */
    [data-testid="stAppViewContainer"], .stApp { background-color: #000 !important; }
    header, footer, [data-testid="stHeader"] { display: none !important; }

    /* PULSING SESSION LINE */
    .session-container { padding: 40px 40px 10px 40px; }
    .session-line { 
        width: 60px; height: 3px; background: var(--volt); 
        margin-bottom: 10px; box-shadow: 0 0 10px var(--volt);
        animation: pulse 2s infinite;
    }
    @keyframes pulse { 0% { opacity: 0.5; } 50% { opacity: 1; } 100% { opacity: 0.5; } }
    .session-id { font-family: 'JetBrains Mono'; color: var(--gray); font-size: 14px; letter-spacing: 3px; }

    /* HEADLINE TYPOGRAPHY */
    .headline {
        font-family: 'Inter'; font-size: 72px; font-weight: 900; 
        line-height: 0.85; letter-spacing: -4px; color: #FFF; 
        padding: 10px 40px; margin-bottom: 30px;
    }
    .headline span { color: var(--volt); }

    /* SUB-DESCRIPTION */
    .description { font-family: 'Inter'; color: #888; font-size: 18px; padding: 0 40px; max-width: 600px; line-height: 1.4; }
    .description b { color: #FFF; }
    .highlight-v { color: #A855F7; } .highlight-vo { color: #EC4899; }

    /* TACTICAL GRID BOXES */
    .stat-grid { 
        display: grid; grid-template-columns: 1fr 1fr; gap: 1px; 
        background: var(--border); border: 1px solid var(--border);
        margin: 40px 40px 20px 40px; 
    }
    .stat-box { background: #000; padding: 30px; }
    .stat-label { font-family: 'JetBrains Mono'; color: #444; font-size: 12px; letter-spacing: 2px; text-transform: uppercase; }
    .stat-value { font-family: 'Inter'; color: #FFF; font-size: 48px; font-weight: 900; margin-top: 10px; }

    /* THE YELLOW START BUTTON */
    .stButton > button {
        background-color: var(--volt) !important;
        color: #000 !important;
        font-family: 'Inter' !important;
        font-weight: 900 !important;
        font-size: 20px !important;
        letter-spacing: 2px !important;
        width: 100% !important;
        height: 60px !important;
        border: none !important;
        border-radius: 0 !important;
        margin: 0 40px;
    }
    .stButton { padding: 0 40px; }

    /* INPUT LINE */
    .stTextInput input {
        background-color: transparent !important; border: none !important;
        border-bottom: 2px solid var(--border) !important; color: var(--volt) !important;
        font-family: 'JetBrains Mono' !important; font-size: 24px !important; border-radius: 0 !important;
    }
    </style>
    """, unsafe_allow_html=True)

# --- LAYOUT ---

# Top Meta
st.markdown('''
    <div class="session-container">
        <div class="session-line"></div>
        <div class="session-id">SESSION // 000</div>
    </div>
''', unsafe_allow_html=True)

# Main Title
st.markdown('''
    <h1 class="headline">
        Your <span>academic<br>weapon</span>, compiled<br>and armed._
    </h1>
''', unsafe_allow_html=True)

# Description
st.markdown('''
    <div class="description">
        One tap to solve doubts with <b class="highlight-v">vision</b>, <b class="highlight-vo">voice</b>, 
        and a full developer console. No distractions. Just answers.
    </div>
''', unsafe_allow_html=True)

# Stats Grid (The 2x2 from the video)
st.markdown('''
    <div class="stat-grid">
        <div class="stat-box">
            <div class="stat-label">Total Doubts</div>
            <div class="stat-value">00</div>
        </div>
        <div class="stat-box">
            <div class="stat-label">Vision</div>
            <div class="stat-value">00</div>
        </div>
        <div class="stat-box">
            <div class="stat-label">Voice</div>
            <div class="stat-value">00</div>
        </div>
        <div class="stat-box">
            <div class="stat-label">Code</div>
            <div class="stat-value">00</div>
        </div>
    </div>
''', unsafe_allow_html=True)

# Tactical Action Button
if st.button("✨ START SOLVING"):
    st.balloons()

# Input Bar
st.markdown('<div style="padding: 20px 40px;">', unsafe_allow_html=True)
query = st.text_input("QUERY", placeholder="_", label_visibility="collapsed")
st.markdown('</div>', unsafe_allow_html=True)
