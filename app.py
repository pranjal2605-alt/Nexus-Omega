import streamlit as st
from datetime import datetime

# --- NEXUS // OMEGA: PIXEL-PERFECT MASTER ---
st.set_page_config(
    page_title="Nexus // Emergent", 
    layout="wide", 
    initial_sidebar_state="collapsed"
)

# Initialize Session State
if 'page' not in st.session_state:
    st.session_state.page = 'home'

# Dynamic Clock
curr_time = datetime.now().strftime("%H:%M:%S")

# --- THE BRUTE FORCE CSS ---
st.markdown(f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@900&family=JetBrains+Mono:wght@500;800&display=swap');
    
    :root {{ 
        --volt: #CDFF00; 
        --bg: #000000; 
    }}

    /* 1. KILL ALL STREAMLIT DEFAULTS */
    [data-testid="stAppViewContainer"], [data-testid="stMainViewContainer"], .stApp {{
        background-color: var(--bg) !important;
    }}
    [data-testid="stHeader"], [data-testid="stToolbar"], .stDeployButton {{
        display: none !important;
    }}
    [data-testid="stMainViewContainer"] > section > div {{
        max-width: 100vw !important; padding: 0 !important;
    }}

    /* 2. TOP BAR & TICKING CLOCK */
    .top-utility {{
        display: flex; justify-content: space-between; align-items: center;
        padding: 20px 50px; border-bottom: 1px solid #111; width: 100%;
    }}
    .sys-clock {{ font-family: 'JetBrains Mono'; color: var(--volt); font-size: 14px; letter-spacing: 4px; }}
    
    .nav-icons-right {{ display: flex; gap: 20px; }}
    .t-icon {{ 
        width: 18px; height: 18px; border: 1.5px solid #222; 
        display: flex; align-items: center; justify-content: center;
    }}
    .t-icon.active {{ border-color: var(--volt); box-shadow: 0 0 10px var(--volt); }}

    /* 3. LOGO & SQUASHED HEADLINE */
    .nav-wrapper {{ padding: 40px 50px 10px 50px; }}
    .n-logo {{
        background: var(--volt); color: #000; font-family: 'Inter'; font-weight: 900;
        font-size: 32px; width: 60px; height: 60px; display: flex; align-items: center; justify-content: center;
    }}
    .main-headline {{
        font-family: 'Inter'; font-size: clamp(60px, 9vw, 135px); font-weight: 900;
        line-height: 0.76; letter-spacing: -0.07em; color: #FFF; padding: 20px 50px 40px 50px;
    }}
    .main-headline span {{ color: var(--volt); }}

    /* 4. ASK NEXUS: FIXING THE WHITE BACKGROUND */
    div[data-baseweb="input"] {{
        background-color: #080808 !important;
        border: 1px solid #1A1A1A !important;
    }}
    input[data-testid="stWidgetLabel"] {{ display: none !important; }}
    input {{
        color: #FFFFFF !important;
        background-color: transparent !important;
        font-family: 'JetBrains Mono' !important;
        padding: 20px !important;
    }}
    .stTextInput {{ padding: 0 50px 50px 50px !important; }}

    /* 5. TACTICAL GRID */
    .grid-container {{ 
        display: grid; grid-template-columns: 1fr 1fr; background: #111; gap: 1px; width: 100%;
    }}
    .grid-item {{ background: var(--bg); padding: 100px 50px; transition: 0.3s; cursor: pointer; }}
    .grid-item:hover {{ background: #050505; }}
    .item-title {{ font-size: 55px; font-weight: 900; letter-spacing: -3px; color: #FFF; margin: 0; }}
    .tag-mono {{ font-family: 'JetBrains Mono'; font-size: 11px; letter-spacing: 6px; color: #444; margin-bottom: 15px; display: block; }}

    /* NATIVE BUTTON OVERLAY */
    .stButton > button {{
        background: transparent !important; border: none !important; color: transparent !important;
        height: 250px !important; width: 100% !important; position: absolute; z-index: 10;
    }}
    </style>
    """, unsafe_allow_html=True)

# --- RENDER TOP BAR ---
st.markdown(f"""
    <div class="top-utility">
        <div style="display:flex; gap:10px; align-items:center;">
            <div style="width:8px; height:8px; border-radius:50%; background:var(--volt);"></div>
            <div class="sys-clock">SYSTEM_TIME // {curr_time}</div>
        </div>
        <div class="nav-icons-right">
            <div class="t-icon active"><div style="width:6px; height:6px; background:var(--volt);"></div></div>
            <div class="t-icon"></div>
            <div class="t-icon"></div>
        </div>
    </div>
""", unsafe_allow_html=True)

# --- HOME PAGE ---
if st.session_state.page == 'home':
    st.markdown('<div class="nav-wrapper"><div class="n-logo">N</div></div>', unsafe_allow_html=True)
    st.markdown('<h1 class="main-headline">Your <span>academic<br>weapon</span>, compiled<br>and armed._</h1>', unsafe_allow_html=True)
    
    # ASK NEXUS
    st.text_input("Ask Nexus", placeholder="ASK NEXUS // TYPE YOUR DOUBT HERE...", label_visibility="collapsed")

    # QUAD GRID
    st.markdown('<div class="grid-container">', unsafe_allow_html=True)
    c1, c2 = st.columns(2)
    with c1:
        st.markdown('<div class="grid-item"><span class="tag-mono">MODULE_01</span><h2 class="item-title">Vision</h2></div>', unsafe_allow_html=True)
        if st.button("V"): st.session_state.page = 'vision'
    with c2:
        st.markdown('<div class="grid-item"><span class="tag-mono">MODULE_02</span><h2 class="item-title">Voice</h2></div>', unsafe_allow_html=True)
        if st.button("VO"): st.session_state.page = 'voice'
    
    c3, c4 = st.columns(2)
    with c3:
        st.markdown('<div class="grid-item"><span class="tag-mono">COMPANION_03</span><h2 class="item-title">Omega AI</h2></div>', unsafe_allow_html=True)
        if st.button("OM"): st.session_state.page = 'omega'
    with c4:
        st.markdown('<div class="grid-item"><span class="tag-mono">TERMINAL_04</span><h2 class="item-title">Dev Mode</h2></div>', unsafe_allow_html=True)
        if st.button("DEV"): st.session_state.page = 'dev'
    st.markdown('</div>', unsafe_allow_html=True)

# --- OMEGA AI PAGE ---
elif st.session_state.page == 'omega':
    st.markdown('<div style="padding:50px;">', unsafe_allow_html=True)
    if st.button("← RETURN"): st.session_state.page = 'home'
    st.markdown("<h1 style='color:var(--volt); font-family:Inter; font-weight:900; font-size:80px;'>OMEGA_AI</h1>", unsafe_allow_html=True)
    st.chat_message("assistant").write("I'm Omega. I speak your language—witty, fast, and grounded. What's the mission?")
    st.chat_input("Message Omega...")
    st.markdown('</div>', unsafe_allow_html=True)

# --- VISION PAGE ---
elif st.session_state.page == 'vision':
    st.markdown('<div style="padding:50px;">', unsafe_allow_html=True)
    if st.button("← RETURN"): st.session_state.page = 'home'
    st.markdown("<h1 style='color:white; font-family:Inter; font-weight:900; font-size:80px;'>VISION_MODE</h1>", unsafe_allow_html=True)
    st.camera_input("SCAN")
    st.markdown('</div>', unsafe_allow_html=True)
