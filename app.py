

import streamlit as st

# --- NEXUS // OMEGA: CARBON COPY ARCHITECTURE ---
st.set_page_config(page_title="Nexus // Emergent", layout="wide", initial_sidebar_state="collapsed")

# 💠 THE INVISIBLE ENGINE: 1:1 PIXEL MATCHING
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700;900&family=JetBrains+Mono:wght@500&display=swap');
    
    /* Global Reset to Absolute Black */
    .stApp { background-color: #000000 !important; color: #FFFFFF !important; font-family: 'Inter', sans-serif !important; }
    header, footer, #MainMenu { visibility: hidden !important; }
    .block-container { padding: 0 !important; max-width: 100% !important; }

    /* Top Navigation: Match Icon Spacing from Video */
    .nav-bar {
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 15px 25px;
        background: #000;
        border-bottom: 1px solid #111;
        position: sticky;
        top: 0;
        z-index: 999;
    }
    .nav-logo { background: #CDFF00; color: #000; font-weight: 900; padding: 2px 10px; font-size: 16px; border-radius: 2px; }
    
    /* Hero Section: Exact Typography Weights */
    .hero { padding: 50px 25px 20px 25px; }
    .session-tag { color: #333; font-family: 'JetBrains Mono'; font-size: 11px; letter-spacing: 3px; margin-bottom: 15px; }
    .title { font-size: 48px; font-weight: 900; line-height: 1.0; letter-spacing: -2px; margin: 0; }
    .highlight { color: #CDFF00; }
    .subtitle { color: #888; font-size: 16px; margin-top: 20px; line-height: 1.4; max-width: 90%; }

    /* Module Grid: Border-Collapse Style */
    .grid { display: grid; grid-template-columns: 1fr 1fr; gap: 1px; background: #111; border-top: 1px solid #111; border-bottom: 1px solid #111; margin-top: 30px; }
    .module-box { background: #000; padding: 30px 20px; transition: 0.2s; cursor: pointer; }
    .module-box:active { background: #050505; }
    .mod-label { color: #CDFF00; font-family: 'JetBrains Mono'; font-size: 9px; letter-spacing: 1px; text-transform: uppercase; margin-bottom: 15px; display: block; }
    .mod-title { font-size: 22px; font-weight: 800; margin: 0; letter-spacing: -0.5px; }

    /* Live Tactical Clock */
    #live-clock { position: fixed; bottom: 25px; right: 25px; font-family: 'JetBrains Mono'; color: #CDFF00; font-weight: 700; font-size: 14px; z-index: 1000; text-shadow: 0 0 10px rgba(205, 255, 0, 0.3); }

    /* Override Streamlit Buttons to be Transparent Icons */
    .stButton>button {
        background: transparent !important;
        border: none !important;
        color: #333 !important;
        font-size: 22px !important;
        padding: 0 !important;
        transition: 0.3s !important;
    }
    .stButton>button:hover { color: #CDFF00 !important; }
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

# --- NAVIGATION STATE ---
if 'page' not in st.session_state:
    st.session_state.page = "HOME"

# --- TOP NAVIGATION BAR ---
cols = st.columns([1, 1, 1, 1, 1])
with cols[0]: 
    if st.button("N"): st.session_state.page = "HOME"
with cols[1]: 
    if st.button("👁️"): st.session_state.page = "VISION"
with cols[2]: 
    if st.button("🎙️"): st.session_state.page = "VOICE"
with cols[3]: 
    if st.button(">_"): st.session_state.page = "DEV"
with cols[4]: 
    if st.button("↺"): st.session_state.page = "HISTORY"

# --- ROUTING LOGIC ---
if st.session_state.page == "HOME":
    # Hero Section
    st.markdown("""
        <div class="hero">
            <div class="session-tag">—— SESSION // 000</div>
            <h1 class="title">Your <span class="highlight">academic<br>weapon</span>, compiled<br>and armed.</h1>
            <p class="subtitle">One tap to solve doubts with vision, voice, and a full developer console. No distractions. Just answers.</p>
        </div>
    """, unsafe_allow_html=True)

    # Tactical Module Selection (Matches the bottom grid in the video)
    st.markdown('<div class="grid">', unsafe_allow_html=True)
    c1, c2 = st.columns(2)
    with c1:
        st.markdown('<div class="module-box"><span class="mod-label">SNAP IT. SOLVE IT.</span><h3 class="mod-title">Vision</h3></div>', unsafe_allow_html=True)
    with c2:
        st.markdown('<div class="module-box"><span class="mod-label">ASK OUT LOUD.</span><h3 class="mod-title">Voice</h3></div>', unsafe_allow_html=True)
    
    c3, c4 = st.columns(2)
    with c3:
        st.markdown('<div class="module-box"><span class="mod-label">DEBUG. EXPLAIN.</span><h3 class="mod-title">Dev Mode</h3></div>', unsafe_allow_html=True)
    with c4:
        st.markdown('<div class="module-box"><span class="mod-label">VIEW HISTORY.</span><h3 class="mod-title">Archive</h3></div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

elif st.session_state.page == "VISION":
    st.markdown('<div class="hero"><h3>VISION SCANNER</h3></div>', unsafe_allow_html=True)
    st.camera_input("SCANNER", label_visibility="collapsed")
    st.button("SOLVE WITH NEXUS")

elif st.session_state.page == "VOICE":
    st.markdown('<div class="hero"><h3>VOICE COMMAND</h3></div>', unsafe_allow_html=True)
    st.markdown('<div style="height:300px; display:flex; align-items:center; justify-content:center; border:1px solid #111; color:#CDFF00; font-size:40px;">🎙️</div>', unsafe_allow_html=True)

elif st.session_state.page == "DEV":
    st.markdown('<div class="hero"><h3>DEV CONSOLE</h3></div>', unsafe_allow_html=True)
    st.code("// Nexus Scripting Engine Ready\n\n", language='javascript')
