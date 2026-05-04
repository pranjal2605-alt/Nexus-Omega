

import streamlit as st

# --- NEXUS // OMEGA: FINAL LOCKDOWN ---
st.set_page_config(page_title="Nexus // Emergent", layout="wide", initial_sidebar_state="collapsed")

# 💠 THE INVISIBLE ENGINE: 1:1 REPLICATION
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@900&family=JetBrains+Mono:wght@700&display=swap');
    
    /* Absolute Pitch Black */
    .stApp { background-color: #000000 !important; color: #FFFFFF !important; font-family: 'Inter', sans-serif !important; }
    header, footer, #MainMenu { visibility: hidden !important; }
    .block-container { padding: 0 !important; max-width: 100% !important; }

    /* THE LOGO: Exact Vid Scale + Neon Aura */
    .logo-container { padding: 45px 25px 15px 25px; }
    .nav-logo { 
        background: #CDFF00; 
        color: #000; 
        font-weight: 900; 
        padding: 12px 26px; 
        font-size: 36px; 
        display: inline-block;
        line-height: 1;
        box-shadow: 0 0 25px #CDFF00;
        border-radius: 0px;
    }

    /* Stealth Navigation Row */
    .stButton>button {
        background: transparent !important;
        border: none !important;
        color: #444444 !important;
        font-family: 'JetBrains Mono', monospace !important;
        font-size: 26px !important;
        font-weight: 700 !important;
        padding: 15px !important;
        transition: 0.2s ease !important;
    }
    .stButton>button:hover { color: #CDFF00 !important; text-shadow: 0 0 10px #CDFF00; }

    /* Hero Text: Aggressive Weight */
    .hero { padding: 25px 25px; }
    .title { font-size: 70px; font-weight: 900; line-height: 0.8; letter-spacing: -5px; margin: 0; }
    .highlight { color: #CDFF00; }

    /* The Tactical Grid */
    .grid { display: grid; grid-template-columns: 1fr 1fr; gap: 1px; background: #111; border-top: 1px solid #111; margin-top: 60px; }
    .module-box { background: #000; padding: 55px 25px; }
    .mod-label { color: #CDFF00; font-family: 'JetBrains Mono'; font-size: 10px; letter-spacing: 3px; text-transform: uppercase; margin-bottom: 15px; display: block; opacity: 0.7; }
    .mod-title { font-size: 32px; font-weight: 800; margin: 0; letter-spacing: -1.5px; }

    /* Live Clock */
    #live-clock { position: fixed; bottom: 35px; right: 35px; font-family: 'JetBrains Mono'; color: #CDFF00; font-weight: 700; font-size: 16px; z-index: 9999; opacity: 0.4; }
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

# --- NAV LOGIC ---
if 'nav' not in st.session_state: st.session_state.nav = "HOME"

cols = st.columns([1, 1, 1, 1, 1])
with cols[0]: 
    if st.button("●"): st.session_state.nav = "HOME"
with cols[1]: 
    if st.button("○"): st.session_state.nav = "VISION"
with cols[2]: 
    if st.button("▲"): st.session_state.nav = "VOICE"
with cols[3]: 
    if st.button("■"): st.session_state.nav = "DEV"
with cols[4]: 
    if st.button("☰"): st.session_state.nav = "ARCHIVE"

st.markdown("<hr style='border: 0; border-top: 1px solid #111; margin: 0;'>", unsafe_allow_html=True)

# --- THE SCREENS ---
if st.session_state.nav == "HOME":
    st.markdown("""
        <div class="logo-container"><div class="nav-logo">N</div></div>
        <div class="hero">
            <h1 class="title">academic<br><span class="highlight">weapon</span></h1>
        </div>
        <div class="grid">
    """, unsafe_allow_html=True)
    
    c1, c2 = st.columns(2)
    with c1: st.markdown('<div class="module-box"><span class="mod-label">OPTICAL SCAN</span><h3 class="mod-title">Vision</h3></div>', unsafe_allow_html=True)
    with c2: st.markdown('<div class="module-box"><span class="mod-label">SONIC INPUT</span><h3 class="mod-title">Voice</h3></div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

else:
    st.markdown('<div class="logo-container"><div class="nav-logo">N</div></div>', unsafe_allow_html=True)
    if st.session_state.nav == "VISION":
        st.camera_input("SCANNER", label_visibility="collapsed")
    elif st.session_state.nav == "VOICE":
        st.markdown('<div style="height:300px; display:flex; align-items:center; justify-content:center; color:#CDFF00; font-family:JetBrains Mono; font-size:24px;">[ LISTENING ]</div>', unsafe_allow_html=True)
