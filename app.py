import streamlit as st
from datetime import datetime

# --- NEXUS // OMEGA: THE 100% ACCURACY BUILD ---
st.set_page_config(
    page_title="Nexus // Emergent", 
    layout="wide", 
    initial_sidebar_state="collapsed"
)

# 💠 THE INVISIBLE ENGINE: DIRECT CSS & JS INJECTION
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;800&family=JetBrains+Mono:wght@400;700&display=swap');
    
    /* 100% Pitch Black Background */
    .stApp { 
        background-color: #000000 !important; 
        color: #FFFFFF !important; 
        font-family: 'Inter', sans-serif !important; 
    }

    /* Hide Streamlit Branding */
    header, footer, #MainMenu { visibility: hidden !important; }
    .block-container { padding: 0 !important; max-width: 100% !important; }

    /* Tactical Top Nav */
    .nav {
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 20px 25px;
        border-bottom: 1px solid #111;
    }
    .nav-logo { 
        background: #CDFF00; 
        color: black; 
        font-weight: 800; 
        padding: 4px 10px; 
        font-size: 18px;
    }

    /* Hero Typography */
    .hero { padding: 40px 25px 20px 25px; }
    .session { color: #333; font-family: 'JetBrains Mono'; font-size: 11px; letter-spacing: 2px; margin-bottom: 10px; }
    .title { font-size: 42px; font-weight: 800; line-height: 1; letter-spacing: -1.5px; margin: 0; }
    .neon-text { color: #CDFF00; }
    .sub { color: #888; font-size: 15px; margin-top: 15px; line-height: 1.4; }

    /* Module Grids */
    .grid-container { display: grid; grid-template-columns: 1fr 1fr; gap: 1px; background: #111; border-top: 1px solid #111; border-bottom: 1px solid #111; }
    .card { background: #000; padding: 25px; min-height: 150px; position: relative; }
    .label { color: #CDFF00; font-family: 'JetBrains Mono'; font-size: 9px; text-transform: uppercase; margin-bottom: 10px; display: block; }
    .card-title { font-size: 20px; font-weight: 700; margin: 0; }
    
    /* Action Button */
    .stButton>button {
        width: 100% !important;
        background: #CDFF00 !important;
        color: black !important;
        border: none !important;
        border-radius: 0 !important;
        font-weight: 800 !important;
        height: 65px !important;
        font-size: 16px !important;
        text-transform: uppercase !important;
        transition: 0.2s !important;
    }
    .stButton>button:active { transform: scale(0.98); }

    /* Live Clock Styling */
    #live-clock {
        position: fixed;
        bottom: 25px;
        right: 25px;
        font-family: 'JetBrains Mono';
        color: #CDFF00;
        font-weight: 700;
        font-size: 18px;
        letter-spacing: 1px;
    }
    </style>

    <!-- JS for the Moving Clock -->
    <div id="live-clock">00:00:00</div>
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

# --- THE UI FRAMEWORK ---

# 1. Navigation
st.markdown('<div class="nav"><div class="nav-logo">N</div><div style="color:#333; font-size:20px;">○ ◬ □</div></div>', unsafe_allow_html=True)

# 2. Hero
st.markdown("""
    <div class="hero">
        <div class="session">SESSION // 001</div>
        <h1 class="title">Your <span class="neon-text">academic<br>weapon</span>, compiled<br>and armed.</h1>
        <p class="sub">One tap to solve doubts with vision, voice, and dev console. No distractions. Just answers.</p>
    </div>
    """, unsafe_allow_html=True)

# 3. Tactical Modules
col1, col2 = st.columns(2)
with col1:
    st.markdown('<div class="card"><span class="label">MODULE 01 // VISION</span><h3 class="card-title">Snap it.</h3></div>', unsafe_allow_html=True)
    st.camera_input("SCAN", label_visibility="collapsed")
with col2:
    st.markdown('<div class="card"><span class="label">MODULE 02 // VOICE</span><h3 class="card-title">Ask it.</h3></div>', unsafe_allow_html=True)
    st.markdown('<div style="height:100px; display:flex; align-items:center; justify-content:center; border:1px solid #111;">🎙️</div>', unsafe_allow_html=True)

# 4. Global Stats Area
st.markdown('<div class="grid-container">', unsafe_allow_html=True)
s1, s2, s3, s4 = st.columns(4)
stats = [("Total Doubts", "00"), ("Vision", "00"), ("Voice", "00"), ("Code", "00")]
for col, (lbl, val) in zip([s1, s2, s3, s4], stats):
    with col:
        st.markdown(f'<div style="padding:20px; border:1px solid #111;"><span style="color:#444; font-size:9px; text-transform:uppercase;">{lbl}</span><br><span style="font-size:24px; font-weight:700;">{val}</span></div>', unsafe_allow_html=True)

# 5. The Trigger
st.markdown("<br>", unsafe_allow_html=True)
if st.button("Start Solving"):
    st.balloons()


