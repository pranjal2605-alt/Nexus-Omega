import streamlit as st

# --- NEXUS // OMEGA: PIXEL-PERFECT GEOMETRY ---
st.set_page_config(page_title="Nexus // Emergent", layout="wide", initial_sidebar_state="collapsed")

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@900&family=JetBrains+Mono:wght@500;800&display=swap');
    
    /* NUCLEAR THEME OVERRIDE */
    .stApp { background-color: #000000 !important; }
    header, footer, .stDeployButton, [data-testid="stToolbar"] { display: none !important; }
    .block-container { padding: 0 !important; margin: 0 !important; max-width: 100% !important; }

    /* TOP NAV: SHARP GEOMETRY */
    .nav-wrapper {
        display: flex; justify-content: space-between; align-items: center;
        padding: 55px 45px 25px 45px; background: #000;
    }
    .n-logo-box {
        background: #CDFF00 !important; color: #000 !important;
        font-family: 'Inter', sans-serif !important; font-weight: 900 !important;
        font-size: 28px !important; padding: 12px 22px !important;
        line-height: 0.8 !important; border-radius: 0px !important; /* Sharp corners */
    }
    .nav-icons-right { display: flex; gap: 32px; align-items: center; }
    
    /* CUSTOM ICON SHAPES: Matching the "Flashy" but colorless requirement */
    .t-icon { width: 20px; height: 20px; fill: #222; transition: 0.2s; }
    .t-icon.active { fill: #CDFF00 !important; filter: drop-shadow(0 0 8px rgba(205,255,0,0.5)); }

    /* HERO: MAXIMUM COMPRESSION */
    .hero-container { padding: 70px 45px; background: #000; }
    .session-indicator { 
        font-family: 'JetBrains Mono' !important; color: #1A1A1A !important; 
        font-size: 11px !important; letter-spacing: 10px !important; margin-bottom: 20px;
    }

    .main-headline {
        font-family: 'Inter', sans-serif !important;
        font-size: 92px !important; font-weight: 900 !important;
        line-height: 0.78 !important; letter-spacing: -8px !important;
        color: #FFFFFF !important; margin: 0 !important;
    }
    .main-headline span { color: #CDFF00 !important; }

    /* SUBHEAD BLOCK HIGHLIGHTS */
    .sub-text { 
        color: #555 !important; font-size: 20px !important; font-weight: 500 !important;
        margin-top: 45px !important; max-width: 620px !important; line-height: 1.3 !important;
        letter-spacing: -0.5px !important;
    }
    .v-block { background: #A855F7 !important; color: #FFF !important; padding: 0px 8px !important; font-weight: 800 !important; }
    .vo-block { background: #EC4899 !important; color: #FFF !important; padding: 0px 8px !important; font-weight: 800 !important; }

    /* TACTICAL GRID: ZERO RADIUS */
    .grid-container { 
        display: grid; grid-template-columns: 1fr 1fr; 
        background: #0A0A0A !important; gap: 1px !important; border-top: 1px solid #111 !important;
    }
    .grid-item { background: #000 !important; padding: 75px 45px !important; position: relative; }
    
    .tag-mono { 
        font-family: 'JetBrains Mono' !important; font-size: 10px !important; 
        letter-spacing: 5px !important; margin-bottom: 25px; display: block; font-weight: 800 !important;
    }
    .item-title { 
        font-size: 44px !important; font-weight: 900 !important; 
        letter-spacing: -3px !important; color: #FFF !important; margin: 0 !important;
    }
    .item-desc { 
        color: #333 !important; font-size: 17px !important; margin-top: 18px !important; 
        max-width: 85%; line-height: 1.4 !important; letter-spacing: -0.2px !important;
    }
    
    /* SQUARE INTERACTION BOX */
    .corner-btn {
        position: absolute; top: 75px; right: 45px;
        width: 52px; height: 52px; border: 1px solid #111;
        display: flex; align-items: center; justify-content: center; color: #CDFF00;
        font-size: 24px; font-weight: 100;
    }
    </style>
    """, unsafe_allow_html=True)

# --- NAV ---
st.markdown("""
    <div class="nav-wrapper">
        <div class="n-logo-box">N</div>
        <div class="nav-icons-right">
            <!-- Terminal (Active) -->
            <svg class="t-icon active" viewBox="0 0 24 24"><rect x="2" y="4" width="20" height="16" rx="0" stroke="currentColor" fill="none" stroke-width="2"/><path d="M7 14l3-2-3-2M12 14h5" stroke="currentColor" stroke-width="2" fill="none"/></svg>
            <!-- Vision -->
            <svg class="t-icon" viewBox="0 0 24 24"><path d="M12 5C7 5 2.73 8.11 1 12c1.73 3.89 6 7 11 7s9.27-3.11 11-7c-1.73-3.89-6-7-11-7zm0 11.5c-2.48 0-4.5-2.02-4.5-4.5S9.52 7.5 12 7.5s4.5 2.02 4.5 4.5-2.02 4.5-4.5 4.5z" fill="currentColor"/></svg>
            <!-- Voice -->
            <svg class="t-icon" viewBox="0 0 24 24"><rect x="9" y="2" width="6" height="12" fill="currentColor"/><path d="M19 10v2a7 7 0 01-14 0v-2M12 19v3" stroke="currentColor" stroke-width="2"/></svg>
            <!-- History -->
            <svg class="t-icon" viewBox="0 0 24 24"><path d="M13 3a9 9 0 109 9" stroke="currentColor" stroke-width="2" fill="none"/><path d="M12 7v5l3 2" stroke="currentColor" stroke-width="2"/></svg>
        </div>
    </div>
""", unsafe_allow_html=True)

# --- HERO ---
st.markdown("""
    <div class="hero-container">
        <div class="session-indicator">————— SESSION // <span>000</span></div>
        <h1 class="main-headline">Your <span>academic<br>weapon</span>, compiled<br>and armed._</h1>
        <p class="sub-text">One tap to solve doubts with <span class="v-block">vision</span>, <span class="vo-block">voice</span>, and a full developer console. No distractions. Just answers.</p>
    </div>
""", unsafe_allow_html=True)

# --- GRID ---
st.markdown('<div class="grid-container">', unsafe_allow_html=True)

col1, col2 = st.columns(2)
with col1:
    st.markdown("""<div class="grid-item">
        <span class="tag-mono" style="color:#A855F7">SNAP IT. SOLVE IT.</span>
        <h2 class="item-title">Vision</h2>
        <p class="item-desc">High-fidelity OCR and spatial reasoning for complex diagrams and text.</p>
        <div class="corner-btn">→</div>
    </div>""", unsafe_allow_html=True)
with col2:
    st.markdown("""<div class="grid-item">
        <span class="tag-mono" style="color:#EC4899">ASK OUT LOUD.</span>
        <h2 class="item-title">Voice</h2>
        <p class="item-desc">Low-latency natural language processing for hands-free intellectual queries.</p>
        <div class="corner-btn">→</div>
    </div>""", unsafe_allow_html=True)

col3, col4 = st.columns(2)
with col3:
    st.markdown("""<div class="grid-item">
        <span class="tag-mono" style="color:#06B6D4">DEBUG. EXPLAIN. BOILERPLATE.</span>
        <h2 class="item-title">Dev Mode</h2>
        <p class="item-desc">A sandbox for code execution, logic verification, and script scaffolding.</p>
        <div class="corner-btn">→</div>
    </div>""", unsafe_allow_html=True)
with col4:
    st.markdown("""<div class="grid-item">
        <span class="tag-mono" style="color:#CDFF00">INTEL RUNBOOK</span>
        <h2 class="item-title">History</h2>
        <p class="item-desc">Immutable log of every query, solution, and generated artifact.</p>
        <div class="corner-btn">→</div>
    </div>""", unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)
