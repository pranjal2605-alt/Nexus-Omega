

import streamlit as st

# --- NEXUS // OMEGA: FINAL NEON REFINEMENT ---
st.set_page_config(page_title="Nexus // Emergent", layout="wide", initial_sidebar_state="collapsed")

# 💠 THE TACTICAL ENGINE: NEON PHYSICS & DESATURATED UI
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700;900&family=JetBrains+Mono:wght@700&display=swap');
    
    /* Pitch Black Canvas */
    .stApp { background-color: #000000 !important; color: #FFFFFF !important; font-family: 'Inter', sans-serif !important; }
    header, footer, #MainMenu { visibility: hidden !important; }
    .block-container { padding: 0 !important; max-width: 100% !important; }

    /* NEON SHINE LOGO */
    .logo-container { padding: 30px 25px 10px 25px; }
    .nav-logo { 
        background: #CDFF00; 
        color: #000; 
        font-weight: 900; 
        padding: 12px 24px; 
        font-size: 34px; 
        display: inline-block;
        line-height: 1;
        /* The Shine Effect */
        box-shadow: 0 0 25px #CDFF00, 0 0 50px rgba(205, 255, 0, 0.4);
        border-radius: 1px;
    }

    /* Tactical Navigation (Carbon Copy Font & Color) */
    .stButton>button {
        background: transparent !important;
        border: none !important;
        color: #333333 !important; /* Specific Stealth Grey from vid */
        font-family: 'JetBrains Mono', monospace !important;
        font-size: 22px !important;
        font-weight: 700 !important;
        padding: 15px !important;
        transition: 0.3s ease !important;
        letter-spacing: -1px;
    }
    /* Active State Shine */
    .stButton>button:hover, .stButton>button:active { 
        color: #CDFF00 !important; 
        text-shadow: 0 0 15px #CDFF00;
    }

    /* Aggressive Hero Typography */
    .hero { padding: 30px 25px; }
    .title { 
        font-size: 68px; 
        font-weight: 900; 
        line-height: 0.82; 
        letter-spacing: -4.5px; 
        margin: 0; 
        text-transform: lowercase; /* Matches the "weapon" vibe */
    }
    .highlight { color: #CDFF00; }

    /* Module Grid */
    .grid { display: grid; grid-template-columns: 1fr 1fr; gap: 1px; background: #111; border-top: 1px solid #111; margin-top: 50px; }
    .module-box { background: #000; padding: 50px 25px; border-right: 1px solid #111; }
    .mod-label { color: #CDFF00; font-family: 'JetBrains Mono'; font-size: 9px; letter-spacing: 3px; text-transform: uppercase; margin-bottom: 15px; display: block; opacity: 0.6; }
    .mod-title { font-size: 30px; font-weight: 800; margin: 0; letter-spacing: -1.5px; color: #FFF; }

    /* Live Clock */
    #live-clock { position: fixed; bottom: 35px; right: 35px; font-family: 'JetBrains Mono'; color: #CDFF00; font-weight: 700; font-size: 15px; z-index: 9999; opacity: 0.4; }
    </style>

    <div id="live-clock">SYS_TIME: 00:00:00</div>
    <script>
        function updateClock() {
            const now = new Date();
            const time = now.getHours().toString().padStart(2, '0') + ":" + 
                         now.getMinutes().toString().padStart(2, '0') + ":" + 
                         now.getSeconds().toString().padStart(2, '0');
            document.getElementById('live-clock').innerText = "SYS_TIME: " + time;
        }
        setInterval(updateClock, 1000);
        updateClock();
    </script>
    """, unsafe_allow_html=True)

# --- NAVIGATION ENGINE ---
if 'nav' not in st.session_state: st.session_state.nav = "HOME"

# Navigation Row (Geometric Stealth Icons)
nav_cols = st.columns([1, 1, 1, 1, 1])
with nav_cols[0]: 
    if st.button("●"): st.session_state.nav = "HOME"
with nav_cols[1]: 
    if st.button("○"): st.session_state.nav = "VISION"
with nav_cols[2]: 
    if st.button("▲"): st.session_state.nav = "VOICE"
with nav_cols[3]: 
    if st.button("■"): st.session_state.nav = "DEV"
with nav_cols[4]: 
    if st.button("☰"): st.session_state.nav = "ARCHIVE"

st.markdown("<hr style='border: 0; border-top: 1px solid #111; margin: 0;'>", unsafe_allow_html=True)

# --- THE INTERFACE ---
if st.session_state.nav == "HOME":
    st.markdown("""
        <div class="logo-container"><div class="nav-logo">N</div></div>
        <div class="hero">
            <h1 class="title">academic<br><span class="highlight">weapon</span></h1>
            <p style="color:#444; font-size:15px; margin-top:35px; font-weight:500; max-width:80%;">Armed with Vision and Voice. Compiled for the 0.01%.</p>
        </div>
        <div class="grid">
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown('<div class="module-box"><span class="mod-label">OPTICAL SCAN</span><h3 class="mod-title">Vision</h3></div>', unsafe_allow_html=True)
    with col2:
        st.markdown('<div class="module-box" style="border:none;"><span class="mod-label">SONIC INPUT</span><h3 class="mod-title">Voice</h3></div>', unsafe_allow_html=True)
    
    st.markdown('</div>', unsafe_allow_html=True)

elif st.session_state.nav == "VISION":
    st.markdown('<div class="hero"><h1 class="title" style="font-size:40px;">vision system</h1></div>', unsafe_allow_html=True)
    st.camera_input("SCANNER", label_visibility="collapsed")

elif st.session_state.nav == "VOICE":
    st.markdown('<div class="hero"><h1 class="title" style="font-size:40px;">voice kernel</h1></div>', unsafe_allow_html=True)
    st.markdown('<div style="height:300px; display:flex; align-items:center; justify-content:center; border:1px solid #111; color:#CDFF00; font-family:JetBrains Mono; font-size:24px; text-shadow: 0 0 10px #CDFF00;">[ LISTENING ]</div>', unsafe_allow_html=True)

elif st.session_state.nav == "DEV":
    st.markdown('<div class="hero"><h1 class="title" style="font-size:40px;">dev console</h1></div>', unsafe_allow_html=True)
    st.code("// Terminal // 01\n\n", language='javascript')
