import streamlit as st

# --- NEXUS // OMEGA: FINAL VISUAL LOCK ---
st.set_page_config(page_title="Nexus // Emergent", layout="wide", initial_sidebar_state="collapsed")

# 💠 THE ENGINE: FORCED POSITIONING & NEON PHYSICS
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@900&family=JetBrains+Mono:wght@700&display=swap');
    
    /* Absolute Pitch Black Canvas */
    .stApp { background-color: #000000 !important; color: #FFFFFF !important; font-family: 'Inter', sans-serif !important; }
    header, footer, #MainMenu { visibility: hidden !important; height: 0; }
    .block-container { padding: 0 !important; max-width: 100% !important; }

    /* THE LOGO: Fixed Position so it CANNOT vanish */
    .nav-logo { 
        position: fixed; top: 60px; left: 25px;
        background: #CDFF00; color: #000; font-weight: 900; 
        padding: 10px 22px; font-size: 32px; 
        box-shadow: 0 0 30px #CDFF00; z-index: 9999; line-height: 1;
    }

    /* THE TITLE: Fixed Position to match Video Layout */
    .hero-fixed {
        position: fixed; top: 160px; left: 25px; z-index: 9998;
    }
    .title { 
        font-size: 72px; font-weight: 900; line-height: 0.8; 
        letter-spacing: -5px; margin: 0; text-transform: lowercase; 
    }
    .highlight { color: #CDFF00; }

    /* Tactical Navigation Icons at very top */
    .nav-bar {
        position: fixed; top: 0; left: 0; width: 100%; height: 50px;
        display: flex; justify-content: space-around; align-items: center;
        background: #000; border-bottom: 1px solid #111; z-index: 10000;
    }

    /* The Tactical Grid: Pushed to the bottom */
    .grid-container { 
        margin-top: 400px; /* Moves it below the fixed title */
        display: grid; grid-template-columns: 1fr 1fr; gap: 1px; 
        background: #111; border-top: 1px solid #111;
    }
    .module-box { background: #000; padding: 50px 25px; min-height: 180px; }
    .mod-label { color: #CDFF00; font-family: 'JetBrains Mono'; font-size: 10px; letter-spacing: 3px; text-transform: uppercase; margin-bottom: 15px; display: block; opacity: 0.6; }
    .mod-title { font-size: 30px; font-weight: 800; color: #FFF; margin: 0; letter-spacing: -1px; }

    /* System Clock */
    #sys-clock { position: fixed; bottom: 30px; right: 30px; font-family: 'JetBrains Mono'; color: #CDFF00; font-weight: 700; font-size: 14px; opacity: 0.5; z-index: 10000; }
    </style>

    <div class="nav-logo">N</div>
    <div class="hero-fixed">
        <h1 class="title">academic<br><span class="highlight">weapon</span></h1>
    </div>
    
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

# --- NAVIGATION ICONS ---
# Using columns for the top bar logic
nav_cols = st.columns([1,1,1,1,1])
with nav_cols[0]: st.button("●")
with nav_cols[1]: st.button("○")
with nav_cols[2]: st.button("▲")
with nav_cols[3]: st.button("■")
with nav_cols[4]: st.button("☰")

# --- GRID (RENDERED AT BOTTOM) ---
st.markdown('<div class="grid-container">', unsafe_allow_html=True)
c1, c2 = st.columns(2)
with c1: st.markdown('<div class="module-box"><span class="mod-label">OPTICAL SCAN</span><h3 class="mod-title">Vision</h3></div>', unsafe_allow_html=True)
with c2: st.markdown('<div class="module-box"><span class="mod-label">SONIC INPUT</span><h3 class="mod-title">Voice</h3></div>', unsafe_allow_html=True)

c3, c4 = st.columns(2)
with c3: st.markdown('<div class="module-box" style="border-top:1px solid #111;"><span class="mod-label">TERMINAL</span><h3 class="mod-title">Dev</h3></div>', unsafe_allow_html=True)
with c4: st.markdown('<div class="module-box" style="border-top:1px solid #111;"><span class="mod-label">LOGS</span><h3 class="mod-title">History</h3></div>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)
