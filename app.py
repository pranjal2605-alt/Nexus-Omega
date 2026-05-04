import streamlit as st
import time
from datetime import datetime

# --- 💠 UNIVERSAL NEXUS ENGINE ---
st.set_page_config(page_title="NEXUS | ARMED", layout="wide")

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Space+Mono:wght@400;700&display=swap');
    .stApp { background-color: #0A0A0A; color: #FFFFFF; font-family: 'Space Mono', monospace; }
    
    .headline { font-size: 42px; font-weight: 700; color: #FFFFFF; line-height: 1.1; margin-top: 20px; }
    .neon-text { color: #CDFF00; text-shadow: 0 0 10px rgba(205, 255, 0, 0.5); }
    
    .stat-box { background-color: #111111; border: 1px solid #222222; padding: 15px; border-radius: 4px; }
    .stat-label { color: #666666; font-size: 10px; text-transform: uppercase; letter-spacing: 1px; }
    .stat-value { color: #FFFFFF; font-size: 28px; font-weight: bold; }

    .cyber-clock {
        font-size: 40px; font-weight: bold; color: #CDFF00;
        text-align: right; letter-spacing: 5px; text-shadow: 0 0 15px #CDFF00;
    }

    .stButton>button {
        background-color: #CDFF00; color: #000000; border-radius: 0px;
        width: 100%; font-weight: bold; text-transform: uppercase; border: none; height: 50px;
    }
    .stButton>button:hover { background-color: #FFFFFF; box-shadow: 0 0 30px #CDFF00; }
    header {visibility: hidden;}
    footer {visibility: hidden;}
    </style>
    """, unsafe_allow_html=True)

# --- 🧠 SESSION MEMORY ---
if 'start_time' not in st.session_state:
    st.session_state.start_time = time.time()
if 'last_milestone' not in st.session_state:
    st.session_state.last_milestone = 0

elapsed_seconds = int(time.time() - st.session_state.start_time)
current_hours = elapsed_seconds // 3600
current_time = datetime.now().strftime("%H:%M:%S")

# --- 🛰️ NAVIGATION & CLOCK ---
col_logo, col_clock = st.columns([1, 1])
with col_logo:
    st.markdown('<div style="background:#CDFF00; color:black; padding:5px 15px; font-weight:bold; width:fit-content; margin-top:10px;">NEXUS // OMEGA</div>', unsafe_allow_html=True)
with col_clock:
    st.markdown(f'<div class="cyber-clock">{current_time}</div>', unsafe_allow_html=True)

# --- 🎉 MILESTONE CELEBRATIONS ---
if current_hours > st.session_state.last_milestone:
    st.session_state.last_milestone = current_hours
    st.balloons()
    st.markdown(f"""
        <div style="background:rgba(205, 255, 0, 0.1); border:1px solid #CDFF00; padding:20px; text-align:center; margin:20px 0;">
            <h2 style="color:#CDFF00; margin:0;">SYSTEM MILESTONE REACHED</h2>
            <p style="color:white; margin:5px 0;">Productivity session: <b>{current_hours} hour(s)</b> active. Keep building.</p>
        </div>
    """, unsafe_allow_html=True)

# --- 🔥 HERO SECTION ---
st.markdown('<div class="headline">Your <span class="neon-text">INTELLIGENCE WEAPON</span>,<br>compiled and armed._</div>', unsafe_allow_html=True)
st.markdown('<p style="color:#888;">Universal Problem Solving. No distractions.</p>', unsafe_allow_html=True)

# --- 📊 ANALYTICS ---
c1, c2, c3, c4 = st.columns(4)
with c1: st.markdown(f'<div class="stat-box"><div class="stat-label">SESSION TIME</div><div class="stat-value">{current_hours}H {(elapsed_seconds % 3600) // 60}M</div></div>', unsafe_allow_html=True)
with c2: st.markdown('<div class="stat-box"><div class="stat-label">VISION</div><div class="stat-value">ACTIVE</div></div>', unsafe_allow_html=True)
with c3: st.markdown('<div class="stat-box"><div class="stat-label">VOICE</div><div class="stat-value">READY</div></div>', unsafe_allow_html=True)
with c4: st.markdown('<div class="stat-box"><div class="stat-label">SYSTEM</div><div class="stat-value">ARMED</div></div>', unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# --- 🛠️ MODULES ---
col_left, col_right = st.columns([1.2, 1])

with col_left:
    st.markdown('<p style="color:#666; font-size:10px;">MODULE 01 // VISION</p>', unsafe_allow_html=True)
    st.markdown('<h3 style="color:white; margin-top:-10px;">Snap anything. Get intelligence.</h3>', unsafe_allow_html=True)
    st.camera_input("SCANNER", label_visibility="hidden")

with col_right:
    st.markdown('<p style="color:#666; font-size:10px;">MODULE 02 // INTEL CONSOLE</p>', unsafe_allow_html=True)
    st.markdown('<div style="display:flex; gap:5px; margin-bottom:5px;"><button style="background:#222; color:#CDFF00; border:1px solid #CDFF00; flex:1; padding:5px;">QUERY</button><button style="background:#111; color:#555; border:1px solid #222; flex:1; padding:5px;">DEBUG</button></div>', unsafe_allow_html=True)
    user_input = st.text_area("INPUT", placeholder="Type your doubt, query, or code here...", height=150, label_visibility="collapsed")
    if st.button("RUN NEXUS ENGINE"):
        if user_input:
            st.info(f"NEXUS is processing your input: {user_input[:50]}...")
            time.sleep(1)
            st.success("Analysis complete. System ready for next instruction.")
        else:
            st.warning("Please enter a query in the console.")

st.markdown("<br><div style='color:#666; font-size:10px; border-top: 1px solid #222; padding-top:10px;'>STATUS: <span style='color:#CDFF00;'>ONLINE</span>. SYSTEM IS WAITING FOR ARCHITECT INPUT.</div>", unsafe_allow_html=True)
