import streamlit as st
from datetime import datetime
import time

# --- OS CONFIG ---
st.set_page_config(page_title="Nexus // Emergent", layout="wide", initial_sidebar_state="collapsed")

# --- THE TACTICAL PALETTE ---
# Vision: #A855F7 (Violet)
# Voice: #EC4899 (Magenta)
# Action/Volt: #CDFF00 (Green)
# Background: #000000 (Pure Black)

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@900&family=JetBrains+Mono:wght@500;800&display=swap');
    
    :root { --volt: #CDFF00; --vision: #A855F7; --voice: #EC4899; --dev: #FACC15; }

    [data-testid="stAppViewContainer"] { background-color: #000 !important; }
    header, footer { display: none !important; }

    /* TACTICAL NAVIGATION BAR */
    .nav-bar {
        display: flex; gap: 15px; padding: 20px 40px; background: #000; border-bottom: 1px solid #111;
    }
    .nav-btn {
        width: 45px; height: 45px; border: 1.5px solid #222; display: flex; 
        align-items: center; justify-content: center; transition: 0.3s;
    }
    .nav-btn.active { border-color: var(--volt); box-shadow: 0 0 15px rgba(205, 255, 0, 0.2); }
    .nav-btn svg { width: 22px; height: 22px; fill: #444; }
    .nav-btn.active svg { fill: var(--volt); }

    /* HEADLINE - MATCHING VIDEO TYPOGRAPHY */
    .hero-text {
        font-family: 'Inter'; font-size: 80px; font-weight: 900; line-height: 0.85;
        letter-spacing: -0.05em; color: #FFF; padding: 60px 40px 10px 40px;
    }
    .hero-text span { color: var(--volt); }
    .sub-text { font-family: 'Inter'; color: #666; font-size: 18px; padding-left: 40px; margin-bottom: 40px; max-width: 500px; }
    .sub-text b { color: #FFF; }

    /* MODULE CARDS - COLOR CODED */
    .module-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 1px; background: #111; border-top: 1px solid #111; }
    .mod-card { 
        background: #000; padding: 60px 40px; position: relative; overflow: hidden; height: 320px;
        display: flex; flex-direction: column; justify-content: flex-end;
    }
    .mod-tag { font-family: 'JetBrains Mono'; font-size: 11px; letter-spacing: 3px; color: #444; margin-bottom: 10px; }
    .mod-title { font-family: 'Inter'; font-size: 50px; font-weight: 900; color: #FFF; margin: 0; letter-spacing: -2px; }
    
    /* NEON ACCENT LINES */
    .accent-vision { border-left: 4px solid var(--vision); }
    .accent-voice { border-left: 4px solid var(--voice); }
    .accent-dev { border-left: 4px solid var(--dev); }
    
    /* TERMINAL INPUT */
    .stTextInput input {
        background-color: transparent !important; border: none !important;
        border-bottom: 2px solid #222 !important; color: var(--volt) !important;
        font-family: 'JetBrains Mono' !important; font-size: 28px !important; border-radius: 0 !important;
    }
    </style>
    """, unsafe_allow_html=True)

# --- GLOBAL NAV ---
st.markdown(f'''
    <div class="nav-bar">
        <div class="nav-btn active"><svg viewBox="0 0 24 24"><path d="M3 3h18v18H3z"/></svg></div>
        <div class="nav-btn"><svg viewBox="0 0 24 24"><path d="M12 2l10 10-10 10L2 12z"/></svg></div>
        <div class="nav-btn"><svg viewBox="0 0 24 24"><circle cx="12" cy="12" r="8"/></svg></div>
        <div class="nav-btn"><svg viewBox="0 0 24 24"><path d="M2 12h20M12 2v20"/></svg></div>
    </div>
''', unsafe_allow_html=True)

# --- HERO SECTION ---
st.markdown('<div class="hero-text">Your <span>academic<br>weapon</span>, compiled<br>and armed._</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-text">One tap to solve doubts with <b>vision</b>, <b>voice</b>, and a full developer console. No distractions. Just answers.</div>', unsafe_allow_html=True)

# --- TERMINAL INPUT ---
st.markdown('<div style="padding: 0 40px 60px 40px;">', unsafe_allow_html=True)
st.text_input("QUERY", placeholder="_", label_visibility="collapsed")
st.markdown('</div>', unsafe_allow_html=True)

# --- MODULE GRID ---
c1, c2 = st.columns(2)
with c1:
    st.markdown('''<div class="mod-card accent-vision">
        <span class="mod-tag">SNAP IT. SOLVE IT.</span>
        <h2 class="mod-title" style="color:var(--vision)">Vision</h2>
    </div>''', unsafe_allow_html=True)

with c2:
    st.markdown('''<div class="mod-card accent-voice">
        <span class="mod-tag">ASK OUT LOUD.</span>
        <h2 class="mod-title" style="color:var(--voice)">Voice</h2>
    </div>''', unsafe_allow_html=True)

c3, c4 = st.columns(2)
with c3:
    st.markdown('''<div class="mod-card accent-dev">
        <span class="mod-tag">DEBUG. EXPLAIN. BOILERPLATE.</span>
        <h2 class="mod-title" style="color:var(--dev)">Dev Mode</h2>
    </div>''', unsafe_allow_html=True)

with c4:
    st.markdown('''<div class="mod-card">
        <span class="mod-tag">ARCHIVE // DOUBT HISTORY</span>
        <h2 class="mod-title">History</h2>
    </div>''', unsafe_allow_html=True)
