

import streamlit as st

# --- NEXUS // OMEGA: HARD-CODED VISUAL LOCK ---
st.set_page_config(page_title="Nexus // Emergent", layout="wide", initial_sidebar_state="collapsed")

# 💠 THE ENGINE: FORCED VISIBILITY & NEON PHYSICS
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@900&family=JetBrains+Mono:wght@700&display=swap');
    
    /* Global Reset */
    .stApp { background-color: #000000 !important; color: #FFFFFF !important; font-family: 'Inter', sans-serif !important; }
    header, footer, #MainMenu { visibility: hidden !important; height: 0; }
    .block-container { padding: 0 !important; max-width: 100% !important; display: block !important; }

    /* THE LOGO: Match Vid Glow & Size */
    .logo-container { padding: 40px 25px 5px 25px; margin-top: 20px; }
    .nav-logo { 
        background: #CDFF00; 
        color: #000; 
        font-weight: 900; 
        padding: 10px 22px; 
        font-size: 32px; 
        display: inline-block;
        box-shadow: 0 0 30px #CDFF00;
        border-radius: 0px;
        line-height: 1;
    }

    /* Top Navigation: Stealth Desaturated */
    .nav-row { display: flex; justify-content: space-between; padding: 10px 25px; border-bottom: 1px solid #111; }
    .stButton>button {
        background: transparent !important;
        border: none !important;
        color: #333333 !important;
        font-size: 26px !important;
        font-family: 'JetBrains Mono' !important;
        transition: 0.3s;
    }
    .stButton>button:hover { color: #CDFF00 !important; text-shadow: 0 0 10px #CDFF00; }

    /* Hero: The "Academic Weapon" Core */
    .hero { padding: 30px 25px; }
    .title { 
        font-size: 70px; 
        font-weight: 900; 
        line-height: 0.82; 
        letter-spacing: -5px; 
        margin: 0; 
        text-transform: lowercase;
        color: #FFFFFF;
    }
    .highlight { color: #CDFF00; }

    /* Module Grid: 1:1 with Vid */
    .grid-container { display: grid; grid-template-columns: 1fr 1fr; gap: 1px; background: #111; border-top: 1px solid #111; margin-top: 40px; }
    .module-box { background: #000; padding: 50px 25px; min-height: 160px; }
    .mod-label { color: #CDFF00; font-family: 'JetBrains Mono'; font-size: 10px; letter-spacing: 3px; text-transform: uppercase; margin-bottom: 15px; display: block; opacity: 0.6; }
    .mod-title { font-size: 30px; font-weight: 800; color: #FFF; margin: 0; letter-spacing: -1.5px; }

    /* System Clock */
    #sys-clock { position: fixed; bottom: 30px; right: 30px; font-family: 'JetBrains Mono'; color: #CDFF00; font-weight: 700; font-size: 14px; opacity: 0.5; z-index: 1000; }
    </style>

    <div id="sys-clock">SYS_TIME: 00:00:00</div>
    <script>
        function updateClock() {
            const now = new Date();
            const time = now.getHours().toString().padStart(2, '0') + ":" + 
                         now.getMinutes().toString().padStart(2, '0') + ":" + 
                         now.getSeconds().toString().padStart(2, '0');
            document.getElementById('sys-clock').innerText = "SYS_TIME: " + time;
        }
        setInterval(updateClock, 1000); updateClock();
    </script>
    """, unsafe_allow_html=True)

# --- NAV ENGINE ---
if 'nav' not in st.session_state: st.session_state.nav = "HOME"

# Navigation Header (Fixed Row)
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
    if st.button("☰"): st.session_state.nav = "MENU"

# --- CONTENT ROUTER ---
if st.session_state.nav == "HOME":
    # Logo & Hero
    st.markdown("""
        <div class="logo-container"><div class="nav-logo">N</div></div>
        <div class="hero">
            <h1 class="title">academic<br><span class="highlight">weapon</span></h1>
        </div>
    """, unsafe_allow_html=True)

    # Tactical Grid (Force rendered via Columns to ensure Streamlit visibility)
    st.markdown('<div class="grid-container">', unsafe_allow_html=True)
    row1_left, row1_right = st.columns(2)
    with row1_left:
        st.markdown('<div class="module-box"><span class="mod-label">OPTICAL SCAN</span><h3 class="mod-title">Vision</h3></div>', unsafe_allow_html=True)
    with row1_right:
        st.markdown('<div class="module-box"><span class="mod-label">SONIC INPUT</span><h3 class="mod-title">Voice</h3></div>', unsafe_allow_html=True)
    
    row2_left, row2_right = st.columns(2)
    with row2_left:
        st.markdown('<div class="module-box" style="border-top:1px solid #111;"><span class="mod-label">KERNEL</span><h3 class="mod-title">Dev</h3></div>', unsafe_allow_html=True)
    with row2_right:
        st.markdown('<div class="module-box" style="border-top:1px solid #111;"><span class="mod-label">LOGS</span><h3 class="mod-title">History</h3></div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

elif st.session_state.nav == "VISION":
    st.markdown('<div class="logo-container"><div class="nav-logo">N</div></div>', unsafe_allow_html=True)
    st.camera_input("SCANNER", label_visibility="collapsed")
