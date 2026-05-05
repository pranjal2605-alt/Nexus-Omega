import streamlit as st

# --- NEXUS // OMEGA: THE 100% BUILD ---
st.set_page_config(
    page_title="Nexus // Emergent", 
    layout="wide", 
    initial_sidebar_state="collapsed"
)

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@900&family=JetBrains+Mono:wght@800&display=swap');
    
    /* 1. DOM TAKEOVER & SCANLINE EFFECT */
    [data-testid="stAppViewContainer"] { 
        background-color: #000 !important; 
        overflow: hidden;
    }
    [data-testid="stMainViewContainer"] > section > div { 
        max-width: 100vw !important; padding: 0 !important; 
    }
    .stApp { background-color: #000 !important; }
    header, footer, .stDeployButton, [data-testid="stToolbar"] { display: none !important; }

    /* Subtle Scanline Texture */
    .stApp::before {
        content: " ";
        position: fixed; top: 0; left: 0; width: 100%; height: 100%;
        background: linear-gradient(rgba(18, 16, 16, 0) 50%, rgba(0, 0, 0, 0.1) 50%), 
                    linear-gradient(90deg, rgba(255, 0, 0, 0.02), rgba(0, 255, 0, 0.01), rgba(0, 0, 255, 0.02));
        background-size: 100% 3px, 3px 100%;
        z-index: 9999; pointer-events: none; opacity: 0.3;
    }

    /* 2. NAVIGATION & PULSE ANIMATION */
    @keyframes pulse-glow {
        0% { filter: drop-shadow(0 0 5px rgba(205,255,0,0.4)); opacity: 0.8; }
        50% { filter: drop-shadow(0 0 15px rgba(205,255,0,0.8)); opacity: 1; }
        100% { filter: drop-shadow(0 0 5px rgba(205,255,0,0.4)); opacity: 0.8; }
    }

    .nav-wrapper {
        display: flex; justify-content: space-between; align-items: center;
        padding: 55px 50px 25px 50px; background: #000;
        width: 100%; box-sizing: border-box; border-bottom: 1px solid #111;
    }
    .n-logo-box {
        background: #CDFF00 !important; color: #000 !important;
        font-family: 'Inter', sans-serif !important; font-weight: 900 !important;
        font-size: 28px !important; padding: 12px 22px !important;
        line-height: 0.8 !important;
    }
    .nav-icons-right { display: flex; gap: 32px; align-items: center; }
    .t-icon { width: 22px; height: 22px; fill: #1A1A1A; transition: 0.3s; }
    .t-icon.active { 
        fill: #CDFF00 !important; 
        animation: pulse-glow 2s infinite ease-in-out; 
    }

    /* 3. HERO SECTION: Aggressive Typography */
    .hero-container { padding: 80px 50px; background: #000; width: 100%; box-sizing: border-box; }
    .session-indicator { 
        font-family: 'JetBrains Mono' !important; color: #111 !important; 
        font-size: 13px !important; letter-spacing: 14px !important; margin-bottom: 25px;
    }
    .main-headline {
        font-family: 'Inter', sans-serif !important;
        font-size: clamp(60px, 8.5vw, 130px) !important; font-weight: 900 !important;
        line-height: 0.78 !important; letter-spacing: -0.08em !important;
        color: #FFFFFF !important; margin: 0 !important;
    }
    .main-headline span { color: #CDFF00 !important; }

    .sub-text { 
        color: #444 !important; font-size: 22px !important; font-weight: 600 !important;
        margin-top: 50px !important; max-width: 700px !important; line-height: 1.35 !important;
    }
    .v-block { background: #A855F7 !important; color: #FFF !important; padding: 0px 10px !important; }
    .vo-block { background: #EC4899 !important; color: #FFF !important; padding: 0px 10px !important; }

    /* 4. THE GRID: Interactive Modules */
    .grid-container { 
        display: grid; grid-template-columns: 1fr 1fr; 
        background: #111 !important; gap: 1px !important;
        width: 100%; box-sizing: border-box; border-top: 1px solid #111;
    }
    .grid-item { 
        background: #000 !important; padding: 90px 50px !important; 
        position: relative; transition: 0.4s; overflow: hidden;
    }
    .grid-item:hover { background: #050505 !important; }
    
    .tag-mono { 
        font-family: 'JetBrains Mono' !important; font-size: 11px !important; 
        letter-spacing: 7px !important; margin-bottom: 25px; display: block; font-weight: 800 !important;
    }
    .item-title { 
        font-size: 52px !important; font-weight: 900 !important; 
        letter-spacing: -4px !important; color: #FFF !important; margin: 0 !important;
    }
    .item-desc { 
        color: #2A2A2A !important; font-size: 19px !important; margin-top: 22px !important; 
        max-width: 85%; line-height: 1.4 !important; transition: 0.3s;
    }
    .grid-item:hover .item-desc { color: #555 !important; }
    
    /* CORNER BUTTON ANIMATION */
    .corner-btn {
        position: absolute; top: 90px; right: 50px;
        width: 55px; height: 55px; border: 1px solid #111;
        display: flex; align-items: center; justify-content: center; 
        color: #222; font-size: 26px; transition: 0.3s;
    }
    .grid-item:hover .corner-btn { 
        border-color: #CDFF00; color: #CDFF00; 
        transform: rotate(-45deg); 
    }
    </style>
    """, unsafe_allow_html=True)

# --- NAVIGATION RENDER ---
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
    <div class="hero-container">
        <div class="session-indicator">————— SESSION // <span style="color:#CDFF00">000</span></div>
        <h1 class="main-headline">Your <span>academic<br>weapon</span>, compiled<br>and armed._</h1>
        <p class="sub-text">One tap to solve doubts with <span class="v-block">vision</span>, <span class="vo-block">voice</span>, and a full developer console. No distractions. Just answers.</p>
    </div>
""", unsafe_allow_html=True)

# --- GRID RENDER ---
st.markdown('<div class="grid-container">', unsafe_allow_html=True)
c1, c2 = st.columns(2)
with c1:
    st.markdown("""<div class="grid-item"><span class="tag-mono" style="color:#A855F7">SNAP IT. SOLVE IT.</span><h2 class="item-title">Vision</h2><p class="item-desc">High-fidelity OCR and spatial reasoning for complex diagrams.</p><div class="corner-btn">→</div></div>""", unsafe_allow_html=True)
with c2:
    st.markdown("""<div class="grid-item"><span class="tag-mono" style="color:#EC4899">ASK OUT LOUD.</span><h2 class="item-title">Voice</h2><p class="item-desc">Low-latency natural language processing for hands-free queries.</p><div class="corner-btn">→</div></div>""", unsafe_allow_html=True)

c3, c4 = st.columns(2)
with c3:
    st.markdown("""<div class="grid-item"><span class="tag-mono" style="color:#06B6D4">DEBUG. EXPLAIN. BOILERPLATE.</span><h2 class="item-title">Dev Mode</h2><p class="item-desc">A sandbox for code execution, logic verification, and scaffolding.</p><div class="corner-btn">→</div></div>""", unsafe_allow_html=True)
with c4:
    st.markdown("""<div class="grid-item"><span class="tag-mono" style="color:#CDFF00">INTEL RUNBOOK</span><h2 class="item-title">History</h2><p class="item-desc">Immutable log of every query, solution, and generated artifact.</p><div class="corner-btn">→</div></div>""", unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)
