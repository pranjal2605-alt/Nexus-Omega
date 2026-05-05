import streamlit as st
from datetime import datetime
import time

# --- OS CONFIG ---
st.set_page_config(page_title="Nexus // Emergent", layout="wide", initial_sidebar_state="collapsed")

# Persistent System States
if 'page' not in st.session_state: st.session_state.page = 'home'

# --- THE PURE-BLACK TECH UI CSS ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@900&family=JetBrains+Mono:wght@500;800&display=swap');
    
    :root { --volt: #CDFF00; --bg: #000000; --nav-border: #1A1A1A; --text-dim: #444; }

    /* ABSOLUTE DARK MODE - NO WHITE/GRAY ALLOWED */
    [data-testid="stAppViewContainer"], .stApp { background-color: #000 !important; }
    header, footer, .stDeployButton { display: none !important; }
    [data-testid="stMainViewContainer"] > section > div { max-width: 100vw !important; padding: 0 !important; }

    /* NAV BAR WRAPPER */
    .top-nav-container {
        display: flex; justify-content: space-between; align-items: center;
        padding: 15px 40px; background: #000; position: sticky; top: 0; z-index: 999;
    }

    /* THE 'DII' STYLE NAV ICONS (SVG-Based for Precision) */
    .nav-box {
        width: 42px; height: 42px; border: 1px solid var(--nav-border);
        display: flex; align-items: center; justify-content: center;
        cursor: pointer; transition: 0.2s; background: transparent;
    }
    .nav-box:hover { border-color: var(--volt); }
    .nav-box.active { border-color: var(--volt); background: rgba(205, 255, 0, 0.05); }
    
    .icon-svg { width: 20px; height: 20px; fill: var(--text-dim); }
    .active .icon-svg { fill: var(--volt); filter: drop-shadow(0 0 5px var(--volt)); }

    .sys-clock { font-family: 'JetBrains Mono'; color: var(--volt); font-size: 14px; letter-spacing: 2px; font-weight: 800; }

    /* HEADLINE STYLING */
    .headline {
        font-family: 'Inter'; font-size: clamp(40px, 8vw, 90px); font-weight: 900; 
        line-height: 0.85; letter-spacing: -0.06em; color: #FFF; padding: 60px 40px 20px 40px; margin: 0;
    }
    .headline span { color: var(--volt); }

    /* ASK NEXUS - VISIBLE TERMINAL TEXT */
    .terminal-input-container { padding: 0 40px 60px 40px; }
    div[data-baseweb="input"] { 
        background-color: transparent !important; 
        border: none !important; 
        border-bottom: 2px solid #111 !important; 
    }
    input { 
        color: var(--volt) !important; 
        font-family: 'JetBrains Mono' !important; 
        font-size: 24px !important; 
        font-weight: 800 !important;
        letter-spacing: -1px;
    }
    input::placeholder { color: #222 !important; }

    /* MODULES GRID */
    .grid-container { display: grid; grid-template-columns: 1fr 1fr; background: #111; gap: 1px; border-top: 1px solid #111; }
    .card { background: #000; padding: 80px 40px; position: relative; height: 300px; display: flex; flex-direction: column; justify-content: flex-end; }
    .card-tag { font-family: 'JetBrains Mono'; font-size: 11px; letter-spacing: 4px; color: var(--text-dim); text-transform: uppercase; margin-bottom: 15px; }
    .card-title { font-size: 52px; font-weight: 900; color: #FFF; margin: 0; letter-spacing: -2px; }

    /* HIDDEN NAVIGATION TRIGGERS */
    .stButton > button {
        background: transparent !important; border: none !important; color: transparent !important;
        position: absolute; top: 0; left: 0; width: 100%; height: 100%; z-index: 10;
    }
    </style>
    """, unsafe_allow_html=True)

# --- NAVIGATION LOGIC & RENDER ---
def render_nav():
    cols = st.columns([0.5, 0.5, 0.5, 0.5, 0.5, 2])
    pages = ['home', 'vision', 'voice', 'dev', 'archive']
    
    # Icons derived from the visual language in 1000244729_4.mp4
    icons = [
        '<rect x="3" y="3" width="18" height="18" rx="2"/>', # Home
        '<circle cx="12" cy="12" r="3"/><path d="M3 12h3m12 0h3M12 3v3m0 12v3"/>', # Vision
        '<path d="M12 1a3 3 0 0 0-3 3v8a3 3 0 0 0 6 0V4a3 3 0 0 0-3-3z"/><path d="M19 10v2a7 7 0 0 1-14 0v-2"/>', # Voice
        '<polyline points="16 18 22 12 16 6"/><polyline points="8 6 2 12 8 18"/>', # Dev
        '<circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14"/>' # Archive
    ]

    for i, p in enumerate(pages):
        with cols[i]:
            active_class = "active" if st.session_state.page == p else ""
            st.markdown(f'''
                <div class="nav-box {active_class}">
                    <svg class="icon-svg" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2" fill="none" stroke-linecap="round" stroke-linejoin="round">
                        {icons[i]}
                    </svg>
                </div>
            ''', unsafe_allow_html=True)
            if st.button(f"nav_{p}", key=f"btn_{p}"):
                st.session_state.page = p
                st.rerun()

    with cols[5]:
        st.markdown(f'<div class="sys-clock" style="text-align:right;">{datetime.now().strftime("%H:%M:%S")}</div>', unsafe_allow_html=True)

# --- PAGE RENDERING ---
render_nav()

if st.session_state.page == 'home':
    st.markdown('<h1 class="headline">Your <span>academic<br>weapon</span>, compiled<br>and armed._</h1>', unsafe_allow_html=True)
    
    st.markdown('<div class="terminal-input-container">', unsafe_allow_html=True)
    query = st.text_input("QUERY", placeholder="TYPE TO ANALYZE...", label_visibility="collapsed")
    st.markdown('</div>', unsafe_allow_html=True)

    # QUAD GRID - FROM VIDEO
    st.markdown('<div class="grid-container">', unsafe_allow_html=True)
    c1, c2 = st.columns(2)
    with c1:
        st.markdown('<div class="card"><span class="card-tag">Vision-to-Solution</span><h2 class="card-title">Vision</h2></div>', unsafe_allow_html=True)
        if st.button("go_vision"): st.session_state.page = 'vision'
    with c2:
        st.markdown('<div class="card"><span class="card-tag">Voice-to-Knowledge</span><h2 class="card-title">Voice</h2></div>', unsafe_allow_html=True)
        if st.button("go_voice"): st.session_state.page = 'voice'
    
    c3, c4 = st.columns(2)
    with c3:
        st.markdown('<div class="card"><span class="card-tag">CIDES-to-Script</span><h2 class="card-title">Dev Mode</h2></div>', unsafe_allow_html=True)
        if st.button("go_dev"): st.session_state.page = 'dev'
    with c4:
        st.markdown('<div class="card"><span class="card-tag">Doubt-History</span><h2 class="card-title">Archive</h2></div>', unsafe_allow_html=True)
        if st.button("go_archive"): st.session_state.page = 'archive'
    st.markdown('</div>', unsafe_allow_html=True)

# Auto-update clock frequency
time.sleep(1)
st.rerun()
