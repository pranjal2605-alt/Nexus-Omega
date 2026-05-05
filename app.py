import streamlit as st
from datetime import datetime

# --- NEXUS // OMEGA: PIXEL-PERFECT RECONSTRUCTION ---
st.set_page_config(
    page_title="Nexus // Emergent", 
    layout="wide", 
    initial_sidebar_state="collapsed"
)

# System Time for the Clock
curr_time = datetime.now().strftime("%H:%M:%S")

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@900&family=JetBrains+Mono:wght@500;800&display=swap');
    
    :root { --volt: #CDFF00; --bg: #000000; --dark-grey: #111111; }

    /* 1. THE NUCLEAR RESET: Edge-to-Edge Force */
    [data-testid="stAppViewContainer"] { background-color: var(--bg) !important; }
    [data-testid="stMainViewContainer"] > section > div { 
        max-width: 100vw !important; padding: 0 !important; 
    }
    .stApp { background-color: var(--bg) !important; }
    header, footer, .stDeployButton, [data-testid="stToolbar"] { display: none !important; }

    /* 2. TOP UTILITY BAR (Left Icons & Clock) */
    .top-utility-bar {
        display: flex; justify-content: space-between; align-items: center;
        padding: 20px 50px; background: var(--bg);
        border-bottom: 1px solid var(--dark-grey);
        width: 100%; box-sizing: border-box;
    }
    .left-icons { display: flex; gap: 15px; align-items: center; }
    .dot-icon { width: 10px; height: 10px; background: #222; border-radius: 50%; }
    .dot-icon.active { background: var(--volt); box-shadow: 0 0 8px var(--volt); }
    .sys-clock {
        font-family: 'JetBrains Mono', monospace; color: var(--volt);
        font-size: 13px; letter-spacing: 4px; margin-left: 20px;
    }

    /* 3. MAIN NAV: LOGO & SYSTEM ICONS */
    .nav-wrapper {
        display: flex; justify-content: space-between; align-items: center;
        padding: 40px 50px 20px 50px; width: 100%; box-sizing: border-box;
    }
    .n-logo-box {
        background: var(--volt) !important; color: #000 !important;
        font-family: 'Inter', sans-serif !important; font-weight: 900 !important;
        font-size: 32px !important; width: 55px; height: 55px;
        display: flex; align-items: center; justify-content: center;
        line-height: 0 !important;
    }
    .nav-icons-right { display: flex; gap: 35px; align-items: center; }
    .t-icon { width: 24px; height: 24px; fill: #1A1A1A; }
    .t-icon.active { fill: var(--volt) !important; filter: drop-shadow(0 0 12px rgba(205,255,0,0.5)); }

    /* 4. HERO: THE SQUASHED WEAPON LOOK */
    .hero-container { padding: 60px 50px; background: var(--bg); width: 100%; box-sizing: border-box; }
    .main-headline {
        font-family: 'Inter', sans-serif !important;
        font-size: clamp(60px, 9vw, 140px) !important; font-weight: 900 !important;
        line-height: 0.78 !important; letter-spacing: -0.08em !important;
        color: #FFFFFF !important; margin: 0 !important;
    }
    .main-headline span { color: var(--volt) !important; }

    .sub-text { 
        color: #444 !important; font-size: 22px !important; font-weight: 600 !important;
        margin-top: 45px !important; max-width: 700px !important; line-height: 1.35 !important;
    }
    .v-block { background: #A855F7 !important; color: #FFF !important; padding: 0 10px; }
    .vo-block { background: #EC4899 !important; color: #FFF !important; padding: 0 10px; }

    /* 5. TACTICAL GRID: LOCKED TO EDGES */
    .grid-container { 
        display: grid; grid-template-columns: 1fr 1fr; 
        background: var(--dark-grey) !important; gap: 1px !important;
        width: 100%; border-top: 1px solid var(--dark-grey);
    }
    .grid-item { background: var(--bg) !important; padding: 100px 50px !important; position: relative; }
    .tag-mono { 
        font-family: 'JetBrains Mono' !important; font-size: 11px !important; 
        letter-spacing: 8px !important; margin-bottom: 25px; display: block; font-weight: 800 !important;
    }
    .item-title { 
        font-size: 58px !important; font-weight: 900 !important; 
        letter-spacing: -4px !important; color: #FFF !important;
    }
    .corner-btn {
        position: absolute; top: 100px; right: 50px;
        width: 60px; height: 60px; border: 1px solid #111;
        display: flex; align-items: center; justify-content: center; color: var(--volt);
    }
    </style>
    """, unsafe_allow_html=True)

# --- TOP UTILITY BAR ---
st.markdown(f"""
    <div class="top-utility-bar">
        <div class="left-icons">
            <div class="dot-icon active"></div>
            <div class="dot-icon"></div>
            <div class="dot-icon"></div>
            <div class="sys-clock">{curr_time}</div>
        </div>
        <div style="color:#222; font-family:'JetBrains Mono'; font-size:11px; letter-spacing:2px;">CORE_V.2.0</div>
    </div>
""", unsafe_allow_html=True)

# --- MAIN NAVIGATION ---
st.markdown("""
    <div class="nav-wrapper">
        <div class="n-logo-box">N</div>
        <div class="nav-icons-right">
            <svg class="t-icon active" viewBox="0 0 24 24"><path d="M2 4h20v16H2V4zm5 9l3-2-3-2m5 4h5"/></svg>
            <svg class="t-icon" viewBox="0 0 24 24"><path d="M12 7a5 5 0 100 10 5 5 0 000-10zm0 2a3 3 0 110 6 3 3 0 010-6z"/></svg>
            <svg class="t-icon" viewBox="0 0 24 24"><path d="M9 4h6v10H9V4zm-4 8v2a7 7 0 0014 0v-2"/></svg>
            <svg class="t-icon" viewBox="0 0 24 24"><path d="M13 7h-2v6h5v-2h-3V7zM4 4h16v16H4V4z"/></svg>
        </div>
    </div>
""", unsafe_allow_html=True)

# --- HERO CONTENT ---
st.markdown("""
    <div class="hero-container">
        <h1 class="main-headline">Your <span>academic<br>weapon</span>, compiled<br>and armed._</h1>
        <p class="sub-text">One tap to solve doubts with <span class="v-block">vision</span>, <span class="vo-block">voice</span>, and a full developer console. No distractions. Just answers.</p>
    </div>
""", unsafe_allow_html=True)

# --- THE GRID ---
st.markdown('<div class="grid-container">', unsafe_allow_html=True)
c1, c2 = st.columns(2)
with c1:
    st.markdown("""<div class="grid-item"><span class="tag-mono" style="color:#A855F7">SNAP IT. SOLVE IT.</span><h2 class="item-title">Vision</h2><div class="corner-btn">→</div></div>""", unsafe_allow_html=True)
with c2:
    st.markdown("""<div class="grid-item"><span class="tag-mono" style="color:#EC4899">ASK OUT LOUD.</span><h2 class="item-title">Voice</h2><div class="corner-btn">→</div></div>""", unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)
