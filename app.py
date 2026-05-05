import streamlit as st
from datetime import datetime
import time

# --- OS CONFIG ---
st.set_page_config(page_title="Nexus // Emergent", layout="wide", initial_sidebar_state="collapsed")

# Persistent System States
if 'page' not in st.session_state: st.session_state.page = 'home'
if 'nexus_memory' not in st.session_state: st.session_state.nexus_memory = []

# --- THE BRUTE-FORCE CSS (No more white boxes) ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@900&family=JetBrains+Mono:wght@500;800&display=swap');
    
    :root { --volt: #CDFF00; --bg: #000000; --vision: #A855F7; --voice: #EC4899; }

    /* CORE OVERRIDE */
    [data-testid="stAppViewContainer"], .stApp { background-color: #000 !important; }
    header, footer, .stDeployButton { display: none !important; }
    [data-testid="stMainViewContainer"] > section > div { max-width: 100vw !important; padding: 0 !important; }

    /* TOP GLOBAL NAV (From Video) */
    .top-nav {
        display: flex; justify-content: space-between; align-items: center;
        padding: 10px 40px; border-bottom: 1px solid #111; background: #000;
        position: sticky; top: 0; z-index: 999;
    }
    .nav-group { display: flex; gap: 25px; align-items: center; }
    .nav-item { color: #333; font-size: 20px; cursor: pointer; transition: 0.3s; }
    .nav-item:hover { color: var(--volt); }
    .nav-item.active { color: var(--volt); text-shadow: 0 0 10px var(--volt); }
    
    .sys-clock { font-family: 'JetBrains Mono'; color: var(--volt); font-size: 13px; letter-spacing: 2px; }

    /* SEARCH BAR (TERMINAL STYLE) */
    div[data-baseweb="input"] { background-color: #080808 !important; border: 1px solid #151515 !important; border-radius: 0 !important; }
    input { color: #CDFF00 !important; font-family: 'JetBrains Mono' !important; padding: 15px !important; }
    
    /* VIDEO ACCURATE HEADLINE */
    .headline {
        font-family: 'Inter'; font-size: 85px; font-weight: 900; line-height: 0.8;
        letter-spacing: -0.05em; color: #FFF; padding: 40px; margin: 0;
    }
    .headline span { color: var(--volt); }

    /* MODULES GRID */
    .grid { display: grid; grid-template-columns: 1fr 1fr; background: #111; gap: 1px; }
    .card { background: #000; padding: 60px 40px; position: relative; }
    .card-tag { font-family: 'JetBrains Mono'; font-size: 10px; letter-spacing: 5px; margin-bottom: 10px; display: block; }
    .card-title { font-size: 45px; font-weight: 900; color: #FFF; }

    /* BUTTONS HIDDEN BEHIND CARDS */
    .stButton > button {
        background: transparent !important; border: none !important; color: transparent !important;
        position: absolute; top: 0; left: 0; width: 100%; height: 100%; z-index: 10;
    }
    </style>
    """, unsafe_allow_html=True)

# --- TOP GLOBAL NAVIGATION RENDER ---
# We use st.columns to make the navigation items clickable
t1, t2, t3 = st.columns([1, 2, 1])

with st.container():
    st.markdown('<div class="top-nav">', unsafe_allow_html=True)
    cols = st.columns([0.5, 0.5, 0.5, 0.5, 0.5, 2])
    
    # Navigation Icons (Logic-linked)
    with cols[0]: 
        if st.button("🏠", key="nav_h"): st.session_state.page = 'home'
        st.markdown(f'<div class="nav-item {"active" if st.session_state.page=="home" else ""}">🏠</div>', unsafe_allow_html=True)
    with cols[1]: 
        if st.button("👁️", key="nav_v"): st.session_state.page = 'vision'
        st.markdown(f'<div class="nav-item {"active" if st.session_state.page=="vision" else ""}">👁️</div>', unsafe_allow_html=True)
    with cols[2]: 
        if st.button("🎤", key="nav_s"): st.session_state.page = 'voice'
        st.markdown(f'<div class="nav-item {"active" if st.session_state.page=="voice" else ""}">🎤</div>', unsafe_allow_html=True)
    with cols[3]: 
        if st.button("💻", key="nav_d"): st.session_state.page = 'dev'
        st.markdown(f'<div class="nav-item {"active" if st.session_state.page=="dev" else ""}">💻</div>', unsafe_allow_html=True)
    with cols[4]: 
        if st.button("🤖", key="nav_o"): st.session_state.page = 'omega'
        st.markdown(f'<div class="nav-item {"active" if st.session_state.page=="omega" else ""}">🤖</div>', unsafe_allow_html=True)
    
    with cols[5]:
        st.markdown(f'<div class="sys-clock" style="text-align:right;">{datetime.now().strftime("%H:%M:%S")}</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

# --- PAGE ROUTING ---

if st.session_state.page == 'home':
    st.markdown('<div style="padding: 30px 40px;"><div style="background:var(--volt); color:black; font-weight:900; width:50px; height:50px; display:flex; align-items:center; justify-content:center; font-size:24px;">N</div></div>', unsafe_allow_html=True)
    st.markdown('<h1 class="headline">Your <span>academic<br>weapon</span>, compiled<br>and armed._</h1>', unsafe_allow_html=True)
    
    # ASK NEXUS: FUNCTIONAL INPUT
    st.markdown('<div style="padding:0 40px 40px 40px;">', unsafe_allow_html=True)
    query = st.text_input("Ask Nexus", placeholder="INPUT COMMAND...", label_visibility="collapsed")
    if query:
        st.markdown(f'<div style="color:var(--volt); font-family:JetBrains Mono;">> ANALYZING: {query}... ONLINE.</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    # QUAD GRID
    st.markdown('<div class="grid">', unsafe_allow_html=True)
    c1, c2 = st.columns(2)
    with c1:
        st.markdown('<div class="card"><span class="card-tag" style="color:var(--vision)">MODULE_01</span><h2 class="card-title">Vision</h2></div>', unsafe_allow_html=True)
        if st.button("gv"): st.session_state.page = 'vision'
    with c2:
        st.markdown('<div class="card"><span class="card-tag" style="color:var(--voice)">MODULE_02</span><h2 class="card-title">Voice</h2></div>', unsafe_allow_html=True)
        if st.button("gvo"): st.session_state.page = 'voice'
    
    c3, c4 = st.columns(2)
    with c3:
        st.markdown('<div class="card"><span class="card-tag">COMPANION_03</span><h2 class="card-title">Omega AI</h2></div>', unsafe_allow_html=True)
        if st.button("go"): st.session_state.page = 'omega'
    with c4:
        st.markdown('<div class="card"><span class="card-tag" style="color:var(--volt)">TERMINAL_04</span><h2 class="card-title">Dev Mode</h2></div>', unsafe_allow_html=True)
        if st.button("gd"): st.session_state.page = 'dev'
    st.markdown('</div>', unsafe_allow_html=True)

elif st.session_state.page == 'omega':
    st.markdown('<div style="padding:40px;">', unsafe_allow_html=True)
    st.markdown("<h1 style='color:var(--volt); font-family:Inter; font-weight:900; font-size:60px;'>OMEGA_CORE</h1>", unsafe_allow_html=True)
    # The actual Brain
    chat = st.chat_input("Speak to Omega...")
    if chat:
        st.session_state.nexus_memory.append({"role": "user", "content": chat})
        # Witty AI Response logic based on your preferences
        response = "Logic scan complete. You're building a weapon, Ranjan. I'm just the fire control."
        st.session_state.nexus_memory.append({"role": "assistant", "content": response})
    
    for m in st.session_state.nexus_memory:
        st.chat_message(m["role"]).write(m["content"])

elif st.session_state.page == 'vision':
    st.markdown('<div style="padding:40px;">', unsafe_allow_html=True)
    st.markdown("<h1 style='color:var(--vision); font-family:Inter; font-weight:900; font-size:60px;'>VISION_SCAN</h1>", unsafe_allow_html=True)
    st.camera_input("CAPTURE")

# Auto-refresh for the Clock
time.sleep(0.1)
st.rerun()
