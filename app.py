import streamlit as st
from datetime import datetime
import time

# --- NEXUS // OMEGA: PIXEL-PERFECT MASTER BUILD ---
st.set_page_config(page_title="Nexus // Emergent", layout="wide", initial_sidebar_state="collapsed")

# 1. LIVE SYSTEM ENGINE (Clock & Navigation)
if 'page' not in st.session_state:
    st.session_state.page = 'home'

# Live Ticking Clock Logic
curr_time = datetime.now().strftime("%H:%M:%S")

st.markdown(f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@900&family=JetBrains+Mono:wght@500;800&display=swap');
    
    :root {{ --volt: #CDFF00; --bg: #000000; --dark-grey: #111111; }}

    /* GLOBAL DOM RESET */
    [data-testid="stAppViewContainer"] {{ background-color: var(--bg) !important; }}
    [data-testid="stMainViewContainer"] > section > div {{ max-width: 100vw !important; padding: 0 !important; }}
    header, footer, .stDeployButton, [data-testid="stToolbar"] {{ display: none !important; }}

    /* TOP UTILITY: STATUS & TICKING CLOCK */
    .top-utility-bar {{
        display: flex; justify-content: space-between; align-items: center;
        padding: 15px 50px; background: var(--bg); border-bottom: 1px solid var(--dark-grey);
    }}
    .sys-clock {{ font-family: 'JetBrains Mono'; color: var(--volt); font-size: 13px; letter-spacing: 4px; }}
    
    /* TOP RIGHT ICONS: Tactical Geometry */
    .nav-icons-right {{ display: flex; gap: 25px; align-items: center; }}
    .t-icon {{ width: 20px; height: 20px; border: 1.5px solid #222; border-radius: 2px; }}
    .t-icon.active {{ border-color: var(--volt); background: var(--volt); box-shadow: 0 0 10px var(--volt); }}

    /* LOGO & NAV */
    .nav-wrapper {{ display: flex; justify-content: space-between; padding: 40px 50px 20px 50px; }}
    .n-logo {{
        background: var(--volt); color: #000; font-family: 'Inter'; font-weight: 900;
        font-size: 32px; width: 60px; height: 60px; display: flex; align-items: center; justify-content: center;
    }}

    /* SEARCH BAR: ASK NEXUS */
    .nexus-search-container {{ padding: 0 50px 40px 50px; }}
    .nexus-input {{
        background: #080808; border: 1px solid #151515; color: #555;
        font-family: 'JetBrains Mono'; padding: 20px; width: 100%;
        font-size: 14px; letter-spacing: 2px; outline: none;
    }}

    /* THE HEADLINE: MAXIMUM SQUASH */
    .main-headline {{
        font-family: 'Inter'; font-size: clamp(60px, 9vw, 130px); font-weight: 900;
        line-height: 0.76; letter-spacing: -0.07em; color: #FFF; padding: 0 50px 60px 50px;
    }}
    .main-headline span {{ color: var(--volt); }}

    /* THE GRID */
    .grid-container {{ 
        display: grid; grid-template-columns: 1fr 1fr; background: var(--dark-grey); gap: 1px;
        width: 100%; border-top: 1px solid var(--dark-grey);
    }}
    .grid-item {{ background: var(--bg); padding: 80px 50px; position: relative; transition: 0.3s; }}
    .item-title {{ font-size: 50px; font-weight: 900; letter-spacing: -3px; color: #FFF; }}
    .tag-mono {{ font-family: 'JetBrains Mono'; font-size: 11px; letter-spacing: 6px; color: #333; }}
    
    /* BUTTON OVERLAY (HIDDEN STREAMLIT BUTTONS) */
    .stButton > button {{
        background: transparent !important; border: none !important; color: transparent !important;
        position: absolute; width: 100%; height: 100%; top: 0; left: 0; z-index: 10;
    }}
    </style>
    """, unsafe_allow_html=True)

# 2. TOP BAR
st.markdown(f"""
    <div class="top-utility-bar">
        <div style="display:flex; gap:10px;">
            <div style="width:8px; height:8px; border-radius:50%; background:var(--volt);"></div>
            <div style="width:8px; height:8px; border-radius:50%; background:#222;"></div>
        </div>
        <div class="sys-clock" id="clock">{curr_time}</div>
        <div class="nav-icons-right">
            <div class="t-icon active"></div>
            <div class="t-icon"></div>
            <div class="t-icon"></div>
        </div>
    </div>
""", unsafe_allow_html=True)

# 3. PAGE ROUTING
if st.session_state.page == 'home':
    st.markdown("""<div class="nav-wrapper"><div class="n-logo">N</div></div>""", unsafe_allow_html=True)
    st.markdown("""<h1 class="main-headline">Your <span>academic<br>weapon</span>, compiled<br>and armed._</h1>""", unsafe_allow_html=True)
    
    # ASK NEXUS SEARCH
    st.markdown('<div class="nexus-search-container">', unsafe_allow_html=True)
    query = st.text_input("ASK_NEXUS:", placeholder="INPUT QUERY OR PASTE CODE BLOCK...", label_visibility="collapsed")
    st.markdown('</div>', unsafe_allow_html=True)

    # QUAD GRID
    st.markdown('<div class="grid-container">', unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    with col1:
        st.markdown('<div class="grid-item"><span class="tag-mono">MODULE_01</span><h2 class="item-title">Vision</h2></div>', unsafe_allow_html=True)
        if st.button("v"): st.session_state.page = 'vision'
    with col2:
        st.markdown('<div class="grid-item"><span class="tag-mono">MODULE_02</span><h2 class="item-title">Voice</h2></div>', unsafe_allow_html=True)
        if st.button("vo"): st.session_state.page = 'voice'
    
    col3, col4 = st.columns(2)
    with col3:
        st.markdown('<div class="grid-item"><span class="tag-mono">MODULE_03</span><h2 class="item-title">Omega AI</h2></div>', unsafe_allow_html=True)
        if st.button("om"): st.session_state.page = 'omega'
    with col4:
        st.markdown('<div class="grid-item"><span class="tag-mono">MODULE_04</span><h2 class="item-title">Dev Terminal</h2></div>', unsafe_allow_html=True)
        if st.button("dev"): st.session_state.page = 'dev'
    st.markdown('</div>', unsafe_allow_html=True)

elif st.session_state.page == 'omega':
    st.markdown('<div style="padding:50px;">', unsafe_allow_html=True)
    if st.button("BACK"): st.session_state.page = 'home'
    st.markdown("<h1 style='color:var(--volt); font-family:Inter; font-weight:900; font-size:60px;'>OMEGA_AI // ACTIVE</h1>", unsafe_allow_html=True)
    st.write("---")
    # Chat logic here
    st.chat_input("Speak to Omega...")
    st.markdown('</div>', unsafe_allow_html=True)

# 4. TICKING SCRIPT (Forces the UI to refresh every second for the clock)
st.empty()
time.sleep(1)
st.rerun()
