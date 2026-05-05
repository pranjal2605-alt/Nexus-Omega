import streamlit as st

# --- NEXUS // OMEGA: PIXEL-PERFECT RECONSTRUCTION ---
st.set_page_config(page_title="Nexus // Emergent", layout="wide", initial_sidebar_state="collapsed")

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@900&family=JetBrains+Mono:wght@800&display=swap');
    
    /* 1. THE VOID: Total DOM takeover */
    [data-testid="stAppViewContainer"] { background-color: #000 !important; }
    [data-testid="stMainViewContainer"] > section > div { 
        max-width: 100vw !important; padding: 0 !important; 
    }
    .stApp { background-color: #000 !important; }
    header, footer, .stDeployButton, [data-testid="stToolbar"] { display: none !important; }

    /* 2. TOP NAV: Geometric Precision */
    .nav-wrapper {
        display: flex; justify-content: space-between; align-items: center;
        padding: 55px 45px 25px 45px; background: #000;
        width: 100%; box-sizing: border-box;
    }
    .n-logo-box {
        background: #CDFF00 !important; color: #000 !important;
        font-family: 'Inter', sans-serif !important; font-weight: 900 !important;
        font-size: 28px !important; padding: 12px 22px !important;
        line-height: 0.8 !important; border-radius: 0px !important;
    }
    .nav-icons-right { display: flex; gap: 32px; align-items: center; }
    .t-icon { width: 22px; height: 22px; fill: #1A1A1A; stroke: none; }
    .t-icon.active { fill: #CDFF00 !important; filter: drop-shadow(0 0 12px rgba(205,255,0,0.5)); }

    /* 3. HERO: "Academic Weapon" Font Physics */
    .hero-container { padding: 70px 45px; background: #000; width: 100%; box-sizing: border-box; }
    .session-indicator { 
        font-family: 'JetBrains Mono' !important; color: #111 !important; 
        font-size: 12px !important; letter-spacing: 12px !important; margin-bottom: 25px;
    }
    .main-headline {
        font-family: 'Inter', sans-serif !important;
        font-size: 92px !important; font-weight: 900 !important;
        line-height: 0.78 !important; letter-spacing: -8px !important;
        color: #FFFFFF !important; margin: 0 !important; text-transform: none;
    }
    .main-headline span { color: #CDFF00 !important; }

    /* SUBHEAD HIGHLIGHTS: Solid color blocks from the video */
    .sub-text { 
        color: #444 !important; font-size: 21px !important; font-weight: 600 !important;
        margin-top: 45px !important; max-width: 650px !important; line-height: 1.35 !important;
    }
    .v-block { background: #A855F7 !important; color: #FFF !important; padding: 0px 8px !important; font-weight: 800 !important; }
    .vo-block { background: #EC4899 !important; color: #FFF !important; padding: 0px 8px !important; font-weight: 800 !important; }

    /* 4. THE GRID: Mosaic Layout */
    .grid-container { 
        display: grid; grid-template-columns: 1fr 1fr; 
        background: #0D0D0D !important; gap: 1px !important; border-top: 1px solid #111 !important;
        width: 100%; box-sizing: border-box;
    }
    .grid-item { background: #000 !important; padding: 80px 45px !important; position: relative; }
    
    .tag-mono { 
        font-family: 'JetBrains Mono' !important; font-size: 11px !important; 
        letter-spacing: 6px !important; margin-bottom: 25px; display: block; font-weight: 800 !important;
    }
    .item-title { 
        font-size: 46px !important; font-weight: 900 !important; 
        letter-spacing: -4px !important; color: #FFF !important; margin: 0 !important;
    }
    .item-desc { 
        color: #2A2A2A !important; font-size: 18px !important; margin-top: 20px !important; 
        max-width: 85%; line-height: 1.4 !important; letter-spacing: -0.4px !important;
    }
    
    /* THE CORNER ARROW BOX */
    .corner-btn {
        position: absolute; top: 80px; right: 45px;
        width: 55px; height: 55px; border: 1px solid #111;
        display: flex; align-items: center; justify-content: center; color: #CDFF00;
        font-size: 26px; font-weight: 100;
    }
    </style>
    """, unsafe_allow_html=True)

# --- UI CONTENT ---

# Nav
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

# Grid
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
