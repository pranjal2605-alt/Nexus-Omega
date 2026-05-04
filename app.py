

import streamlit as st

# --- NEXUS // OMEGA: TOTAL RESTORATION ---
st.set_page_config(page_title="Nexus // Emergent", layout="wide", initial_sidebar_state="collapsed")

# 💠 THE INVISIBLE ENGINE: 1:1 REPLICATION
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@900&family=JetBrains+Mono:wght@700&display=swap');
    
    .stApp { background-color: #000000 !important; color: #FFFFFF !important; font-family: 'Inter', sans-serif !important; }
    header, footer, #MainMenu { visibility: hidden !important; }
    .block-container { padding: 0 !important; max-width: 100% !important; }

    /* THE LOGO: Glowing & Large */
    .logo-container { padding: 40px 25px 10px 25px; }
    .nav-logo { 
        background: #CDFF00; 
        color: #000; 
        font-weight: 900; 
        padding: 10px 22px; 
        font-size: 32px; 
        display: inline-block;
        line-height: 1;
        box-shadow: 0 0 25px #CDFF00;
        border-radius: 0px;
    }

    /* Hero Text: Aggressive & Tight */
    .hero { padding: 20px 25px; }
    .session-tag { color: #333; font-family: 'JetBrains Mono'; font-size: 10px; letter-spacing: 4px; margin-bottom: 10px; }
    .title { font-size: 60px; font-weight: 900; line-height: 0.85; letter-spacing: -4px; margin: 0; text-transform: lowercase; }
    .highlight { color: #CDFF00; }

    /* Tactical Navigation Icons */
    .stButton>button {
        background: transparent !important;
        border: none !important;
        color: #333333 !important;
        font-size: 24px !important;
        padding: 15px !important;
        transition: 0.2s ease !important;
    }
    .stButton>button:hover { color: #CDFF00 !important; }

    /* The Tactical Grid (Restored) */
    .grid { display: grid; grid-template-columns: 1fr 1fr; gap: 1px; background: #111; border-top: 1px solid #111; border-bottom: 1px solid #111; margin-top: 40px; }
    .module-box { background: #000; padding: 45px 25px; min-height: 150px; }
    .mod-label { color: #CDFF00; font-family: 'JetBrains Mono'; font-size: 9px; letter-spacing: 2px; text-transform: uppercase; margin-bottom: 12px; display: block; opacity: 0.7; }
    .mod-title { font-size: 26px; font-weight: 800; margin: 0; letter-spacing: -1px; color: #FFF; }

    /* Live Clock */
    #live-clock { position: fixed; bottom: 30px; right: 30px; font-family: 'JetBrains Mono'; color: #CDFF00; font-weight: 700; font-size: 15px; z-index: 9999; opacity: 0.5; }
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

# --- MAIN INTERFACE ---
if st.session_state.nav == "HOME":
    st.markdown("""
        <div class="logo-container"><div class="nav-logo">N</div></div>
        <div class="hero">
            <div class="session-tag">—— SESSION // 000</div>
            <h1 class="title">academic<br><span class="highlight">weapon</span></h1>
        </div>
        
        <div class="grid">
    """, unsafe_allow_html=True)
    
    # Bottom Grid from Video
    col1, col2 = st.columns(2)
    with col1:
        st.markdown('<div class="module-box"><span class="mod-label">SNAP IT. SOLVE IT.</span><h3 class="mod-title">Vision</h3></div>', unsafe_allow_html=True)
    with col2:
        st.markdown('<div class="module-box" style="border-left:1px solid #111;"><span class="mod-label">ASK OUT LOUD.</span><h3 class="mod-title">Voice</h3></div>', unsafe_allow_html=True)
    
    col3, col4 = st.columns(2)
    with col3:
        st.markdown('<div class="module-box" style="border-top:1px solid #111;"><span class="mod-label">DEBUG MODE.</span><h3 class="mod-title">Dev</h3></div>', unsafe_allow_html=True)
    with col4:
        st.markdown('<div class="module-box" style="border-top:1px solid #111; border-left:1px solid #111;"><span class="mod-label">ARCHIVE.</span><h3 class="mod-title">History</h3></div>', unsafe_allow_html=True)
    
    st.markdown('</div>', unsafe_allow_html=True)

elif st.session_state.nav == "VISION":
    st.markdown('<div class="logo-container"><div class="nav-logo">N</div></div>', unsafe_allow_html=True)
    st.camera_input("SCANNER", label_visibility="collapsed")

elif st.session_state.nav == "VOICE":
    st.markdown('<div class="logo-container"><div class="nav-logo">N</div></div>', unsafe_allow_html=True)
    st.markdown('<div style="height:300px; display:flex; align-items:center; justify-content:center; color:#CDFF00; font-family:JetBrains Mono; font-size:24px;">[ LISTENING ]</div>', unsafe_allow_html=True)
