import streamlit as st
from datetime import datetime

# --- SYSTEM CONFIG ---
st.set_page_config(
    page_title="Nexus // Emergent", 
    layout="wide", 
    initial_sidebar_state="collapsed"
)

# Initialize Session State for Multi-Page Logic
if 'page' not in st.session_state:
    st.session_state.page = 'home'
if 'status' not in st.session_state:
    st.session_state.status = 'active'

# Dynamic Clock
curr_time = datetime.now().strftime("%H:%M:%S")

# --- THE ABSOLUTE OVERRIDE CSS ---
st.markdown(f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@900&family=JetBrains+Mono:wght@500;800&display=swap');
    
    :root {{ 
        --volt: #CDFF00; 
        --bg: #000000; 
        --vision: #A855F7;
        --voice: #EC4899;
        --omega: #FFFFFF;
    }}

    /* FORCE BLACK BACKGROUND */
    [data-testid="stAppViewContainer"], [data-testid="stMainViewContainer"], .stApp {{
        background-color: var(--bg) !important;
    }}
    [data-testid="stHeader"], [data-testid="stToolbar"] {{ display: none !important; }}
    [data-testid="stMainViewContainer"] > section > div {{ max-width: 100vw !important; padding: 0 !important; }}

    /* TOP BAR & TICKING CLOCK */
    .top-utility {{
        display: flex; justify-content: space-between; align-items: center;
        padding: 20px 50px; border-bottom: 1px solid #111; width: 100%; box-sizing: border-box;
    }}
    .sys-clock {{ font-family: 'JetBrains Mono'; color: var(--volt); font-size: 14px; letter-spacing: 4px; }}
    
    /* TOP RIGHT ICONS (Status Toggles) */
    .nav-icons-right {{ display: flex; gap: 15px; }}
    .t-icon {{ 
        width: 16px; height: 16px; border: 1.5px solid #222; cursor: pointer;
        display: flex; align-items: center; justify-content: center;
    }}
    .t-icon.active {{ border-color: var(--volt); box-shadow: 0 0 10px var(--volt); }}

    /* LOGO & WEAPON HEADLINE */
    .nav-wrapper {{ padding: 40px 50px 10px 50px; }}
    .n-logo {{
        background: var(--volt); color: #000; font-family: 'Inter'; font-weight: 900;
        font-size: 32px; width: 60px; height: 60px; display: flex; align-items: center; justify-content: center;
    }}
    .main-headline {{
        font-family: 'Inter'; font-size: clamp(50px, 8vw, 120px); font-weight: 900;
        line-height: 0.76; letter-spacing: -0.07em; color: #FFF; padding: 20px 50px; margin: 0;
    }}
    .main-headline span {{ color: var(--volt); }}

    /* ASK NEXUS: DARK OVERRIDE */
    div[data-testid="stTextInput"] {{
        padding: 0 50px 40px 50px !important;
    }}
    div[data-baseweb="input"] {{
        background-color: #0A0A0A !important;
        border: 1px solid #1A1A1A !important;
        border-radius: 0px !important;
    }}
    input {{
        color: #FFF !important;
        font-family: 'JetBrains Mono' !important;
        padding: 15px !important;
    }}

    /* QUAD GRID SYSTEM */
    .grid-container {{ 
        display: grid; grid-template-columns: 1fr 1fr; background: #111; gap: 1px; width: 100%;
    }}
    .grid-item {{ 
        background: var(--bg); padding: 80px 50px; position: relative; 
        border: 1px solid transparent; transition: 0.2s;
    }}
    .grid-item:hover {{ border: 1px solid #222; }}
    .item-title {{ font-size: 48px; font-weight: 900; letter-spacing: -3px; color: #FFF; margin: 0; }}
    .tag-mono {{ font-family: 'JetBrains Mono'; font-size: 11px; letter-spacing: 5px; margin-bottom: 10px; display: block; }}

    /* HIDDEN BUTTON OVERLAY */
    .stButton > button {{
        background: transparent !important; border: none !important; color: transparent !important;
        height: 200px !important; width: 100% !important; position: absolute; z-index: 10; top: 0; left: 0;
    }}
    </style>
    """, unsafe_allow_html=True)

# --- TOP UTILITY BAR ---
st.markdown(f"""
    <div class="top-utility">
        <div style="display:flex; gap:12px; align-items:center;">
            <div style="width:10px; height:10px; background:var(--volt); border-radius:2px;"></div>
            <div class="sys-clock">{curr_time}</div>
        </div>
        <div class="nav-icons-right">
            <div class="t-icon active"><div style="width:6px; height:6px; background:var(--volt);"></div></div>
            <div class="t-icon"></div>
            <div class="t-icon"></div>
        </div>
    </div>
""", unsafe_allow_html=True)

# --- PAGE ROUTING SYSTEM ---

# HOME PAGE
if st.session_state.page == 'home':
    st.markdown('<div class="nav-wrapper"><div class="n-logo">N</div></div>', unsafe_allow_html=True)
    st.markdown('<h1 class="main-headline">Your <span>academic<br>weapon</span>, compiled<br>and armed._</h1>', unsafe_allow_html=True)
    
    # ASK NEXUS
    st.text_input("Ask Nexus", placeholder="ASK NEXUS // INPUT QUERY...", label_visibility="collapsed")

    # GRID
    st.markdown('<div class="grid-container">', unsafe_allow_html=True)
    c1, c2 = st.columns(2)
    with c1:
        st.markdown(f'<div class="grid-item"><span class="tag-mono" style="color:var(--vision)">MODULE_01</span><h2 class="item-title">Vision</h2></div>', unsafe_allow_html=True)
        if st.button("V", key="v"): st.session_state.page = 'vision'
    with c2:
        st.markdown(f'<div class="grid-item"><span class="tag-mono" style="color:var(--voice)">MODULE_02</span><h2 class="item-title">Voice</h2></div>', unsafe_allow_html=True)
        if st.button("VO", key="vo"): st.session_state.page = 'voice'
    
    c3, c4 = st.columns(2)
    with c3:
        st.markdown(f'<div class="grid-item"><span class="tag-mono" style="color:var(--omega)">COMPANION_03</span><h2 class="item-title">Omega AI</h2></div>', unsafe_allow_html=True)
        if st.button("OM", key="om"): st.session_state.page = 'omega'
    with c4:
        st.markdown(f'<div class="grid-item"><span class="tag-mono" style="color:var(--volt)">TERMINAL_04</span><h2 class="item-title">Dev Mode</h2></div>', unsafe_allow_html=True)
        if st.button("DEV", key="dev"): st.session_state.page = 'dev'
    st.markdown('</div>', unsafe_allow_html=True)

# OMEGA AI PAGE
elif st.session_state.page == 'omega':
    st.markdown('<div style="padding:50px;">', unsafe_allow_html=True)
    if st.button("← BACK"): st.session_state.page = 'home'
    st.markdown("<h1 style='color:var(--volt); font-family:Inter; font-weight:900; font-size:70px;'>OMEGA_CHAT</h1>", unsafe_allow_html=True)
    st.write("### Systems nominal. I'm Omega—your witty, grounded AI collaborator.")
    st.chat_input("Ask Omega anything...")

# VISION PAGE
elif st.session_state.page == 'vision':
    st.markdown('<div style="padding:50px;">', unsafe_allow_html=True)
    if st.button("← BACK"): st.session_state.page = 'home'
    st.markdown("<h1 style='color:var(--vision); font-family:Inter; font-weight:900; font-size:70px;'>VISION_SCAN</h1>", unsafe_allow_html=True)
    st.camera_input("SCAN YOUR ASSIGNMENT")

# DEV MODE PAGE
elif st.session_state.page == 'dev':
    st.markdown('<div style="padding:50px;">', unsafe_allow_html=True)
    if st.button("← BACK"): st.session_state.page = 'home'
    st.markdown("<h1 style='color:var(--volt); font-family:Inter; font-weight:900; font-size:70px;'>DEV_TERMINAL</h1>", unsafe_allow_html=True)
    st.code("# INITIALIZING NEON HEIST: SYNDICATE...\nimport ursina\n\napp = Ursina()", language="python")
