import streamlit as st

# --- NEXUS // OMEGA: PIXEL-PERFECT FINAL ---
st.set_page_config(
    page_title="Nexus // Emergent", 
    layout="wide", 
    initial_sidebar_state="collapsed"
)

# Initialize Session State for Navigation
if 'page' not in st.session_state:
    st.session_state.page = 'home'

# --- THE SUPREME CSS OVERRIDE ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@900&family=JetBrains+Mono:wght@800&display=swap');
    
    /* VOLT GREEN HEX MATCH: #CDFF00 */
    :root { --volt: #CDFF00; --bg: #000000; --dark-grey: #111111; }

    [data-testid="stAppViewContainer"] { background-color: var(--bg) !important; }
    [data-testid="stMainViewContainer"] > section > div { max-width: 100vw !important; padding: 0 !important; }
    header, footer, .stDeployButton, [data-testid="stToolbar"] { display: none !important; }

    /* NAV: PIXEL-PERFECT LOGO & ICONS */
    .nav-wrapper {
        display: flex; justify-content: space-between; align-items: center;
        padding: 45px 50px 25px 50px; background: var(--bg);
        width: 100%; box-sizing: border-box; border-bottom: 1px solid var(--dark-grey);
    }
    
    /* THE "N" LOGO: Precise Padding & Weight */
    .n-logo {
        background: var(--volt) !important; color: #000 !important;
        font-family: 'Inter', sans-serif !important; font-weight: 900 !important;
        font-size: 32px !important; width: 55px; height: 55px;
        display: flex; align-items: center; justify-content: center;
        line-height: 0 !important; cursor: pointer;
    }

    /* REACTIVE TOP ICONS */
    .nav-icons-right { display: flex; gap: 35px; align-items: center; }
    .t-icon { 
        width: 24px; height: 24px; fill: #222; 
        transition: all 0.2s cubic-bezier(0.4, 0, 0.2, 1); 
        cursor: pointer;
    }
    .t-icon:hover { fill: #555; transform: translateY(-2px); }
    .t-icon.active { 
        fill: var(--volt) !important; 
        filter: drop-shadow(0 0 12px rgba(205,255,0,0.6)); 
    }

    /* HERO: TYPOGRAPHY SQUASH */
    .hero-container { padding: 90px 50px; background: var(--bg); width: 100%; box-sizing: border-box; }
    .main-headline {
        font-family: 'Inter', sans-serif !important;
        font-size: clamp(70px, 9vw, 150px) !important; font-weight: 900 !important;
        line-height: 0.76 !important; letter-spacing: -0.07em !important;
        color: #FFFFFF !important; margin: 0 !important;
    }
    .main-headline span { color: var(--volt) !important; }

    /* THE GRID */
    .grid-container { 
        display: grid; grid-template-columns: 1fr 1fr; 
        background: var(--dark-grey) !important; gap: 1px !important;
        width: 100%; box-sizing: border-box; border-top: 1px solid var(--dark-grey);
    }
    .grid-item { 
        background: var(--bg) !important; padding: 100px 50px !important; 
        position: relative; transition: 0.3s; cursor: pointer;
    }
    .grid-item:hover { background: #050505 !important; }
    
    .item-title { 
        font-size: 58px !important; font-weight: 900 !important; 
        letter-spacing: -3px !important; color: #FFF !important; margin: 0 !important;
    }
    
    /* PAGE TRANSITION ELEMENT */
    .back-btn {
        color: var(--volt); font-family: 'JetBrains Mono';
        padding: 50px; cursor: pointer; font-size: 14px;
        letter-spacing: 5px;
    }
    </style>
    """, unsafe_allow_html=True)

# --- NAVIGATION LOGIC ---
def go_home(): st.session_state.page = 'home'
def go_vision(): st.session_state.page = 'vision'

# --- UI RENDER: HOME ---
if st.session_state.page == 'home':
    # Nav
    st.markdown(f"""
        <div class="nav-wrapper">
            <div class="n-logo">N</div>
            <div class="nav-icons-right">
                <svg class="t-icon active" viewBox="0 0 24 24"><path d="M2 4h20v16H2V4zm5 9l3-2-3-2m5 4h5"/></svg>
                <svg class="t-icon" viewBox="0 0 24 24"><path d="M12 7a5 5 0 100 10 5 5 0 000-10zm0 2a3 3 0 110 6 3 3 0 010-6z"/></svg>
                <svg class="t-icon" viewBox="0 0 24 24"><path d="M9 4h6v10H9V4zm-4 8v2a7 7 0 0014 0v-2"/></svg>
                <svg class="t-icon" viewBox="0 0 24 24"><path d="M13 7h-2v6h5v-2h-3V7zM4 4h16v16H4V4z"/></svg>
            </div>
        </div>
    """, unsafe_allow_html=True)

    st.markdown("""
        <div class="hero-container">
            <h1 class="main-headline">Your <span>academic<br>weapon</span>, compiled<br>and armed._</h1>
        </div>
    """, unsafe_allow_html=True)

    # Grid (Using Native Buttons disguised by CSS for navigation)
    st.markdown('<div class="grid-container">', unsafe_allow_html=True)
    c1, c2 = st.columns(2)
    with c1:
        if st.button("VISION", use_container_width=True): st.session_state.page = 'vision'
        st.markdown("""<div class="grid-item" style="pointer-events:none; margin-top:-70px;">
            <h2 class="item-title">Vision</h2>
        </div>""", unsafe_allow_html=True)
    with c2:
        if st.button("VOICE", use_container_width=True): st.session_state.page = 'voice'
        st.markdown("""<div class="grid-item" style="pointer-events:none; margin-top:-70px;">
            <h2 class="item-title">Voice</h2>
        </div>""", unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

# --- UI RENDER: VISION PAGE ---
elif st.session_state.page == 'vision':
    st.markdown('<div class="back-btn" onclick="window.location.reload()">← BACK_TO_TERMINAL</div>', unsafe_allow_html=True)
    if st.button("RETURN HOME"): st.session_state.page = 'home'
    
    st.markdown("""
        <div style="padding: 50px;">
            <h1 style="color:white; font-family:Inter; font-size:80px; font-weight:900;">VISION_MODULE</h1>
            <p style="color:#444; font-size:24px;">Initialize camera for spatial doubt resolution...</p>
        </div>
    """, unsafe_allow_html=True)
