import streamlit as st

# --- NEXUS // OMEGA: TOTAL VISUAL LOCK ---
st.set_page_config(page_title="Nexus // Emergent", layout="wide", initial_sidebar_state="collapsed")

# 💠 THE ENGINE: FORCED NEON PHYSICS & TYPOGRAPHY
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700;900&family=JetBrains+Mono:wght@500;700&display=swap');
    
    /* Absolute Zero Canvas */
    .stApp { background-color: #000000 !important; color: #FFFFFF !important; font-family: 'Inter', sans-serif !important; }
    header, footer, #MainMenu { visibility: hidden !important; height: 0; }
    .block-container { padding: 0 !important; max-width: 100% !important; }

    /* NAVIGATION BAR: Tactical Icons */
    .top-nav {
        display: flex; justify-content: space-between; align-items: center;
        padding: 45px 30px 15px 30px; border-bottom: 1px solid #111;
    }
    .n-logo { 
        background: #CDFF00; color: #000; font-weight: 900; 
        padding: 8px 18px; font-size: 24px; box-shadow: 0 0 25px rgba(205, 255, 0, 0.4);
    }
    .nav-icons { display: flex; gap: 35px; color: #555; font-family: 'JetBrains Mono'; font-size: 22px; }
    .nav-icons span:hover { color: #CDFF00; cursor: pointer; }

    /* HERO: The Academic Weapon Build */
    .hero-section { padding: 60px 30px; }
    .session-info { color: #444; font-family: 'JetBrains Mono'; font-size: 11px; letter-spacing: 5px; margin-bottom: 12px; }
    .session-info span { color: #CDFF00; }
    
    .main-title { 
        font-size: 72px; font-weight: 900; line-height: 0.85; 
        letter-spacing: -5px; margin: 0;
    }
    .highlight { color: #CDFF00; }
    
    .sub-copy { color: #888; font-size: 19px; margin-top: 30px; max-width: 550px; line-height: 1.4; font-weight: 400; }
    .sub-copy b { color: #FFF; font-weight: 700; }

    /* MODULES: 2x2 Tactical Grid */
    .module-grid { display: grid; grid-template-columns: 1fr 1fr; background: #111; gap: 1px; border-top: 1px solid #111; }
    .mod-card { background: #000; padding: 55px 30px; position: relative; min-height: 220px; transition: 0.3s; }
    .mod-card:hover { background: #050505; }
    
    .mod-tag { color: #CDFF00; font-family: 'JetBrains Mono'; font-size: 10px; letter-spacing: 3px; text-transform: uppercase; margin-bottom: 18px; display: block; opacity: 0.8; }
    .mod-name { font-size: 34px; font-weight: 800; margin: 0; letter-spacing: -1.5px; color: #FFF; }
    .mod-desc { color: #666; font-size: 15px; margin-top: 12px; line-height: 1.4; max-width: 85%; }

    /* Tactical Arrow Button */
    .go-btn { 
        position: absolute; top: 55px; right: 30px; 
        width: 45px; height: 45px; background: #111; 
        display: flex; align-items: center; justify-content: center;
        border: 1px solid #222; color: #CDFF00; font-size: 20px;
    }
    </style>
    """, unsafe_allow_html=True)

# --- UI STRUCTURE ---

# Top Navigation
st.markdown("""
    <div class="top-nav">
        <div class="n-logo">N</div>
        <div class="nav-icons">
            <span>>_</span>
            <span>⌾</span>
            <span>🎙</span>
            <span>⧉</span>
            <span>↺</span>
        </div>
    </div>
""", unsafe_allow_html=True)

# Hero Header
st.markdown("""
    <div class="hero-section">
        <div class="session-info">————— SESSION // <span>000</span></div>
        <h1 class="main-title">Your <span class="highlight">academic<br>weapon</span>, compiled<br>and armed._</h1>
        <p class="sub-copy">One tap to solve doubts with <b>vision</b>, <b>voice</b>, and a full developer console. No distractions. Just answers.</p>
    </div>
""", unsafe_allow_html=True)

# Feature Grid
st.markdown('<div class="module-grid">', unsafe_allow_html=True)

# Row 1
c1, c2 = st.columns(2)
with c1:
    st.markdown("""
        <div class="mod-card">
            <span class="mod-tag">SNAP IT. SOLVE IT.</span>
            <h3 class="mod-name">Vision</h3>
            <p class="mod-desc">Upload a photo of a textbook problem, handwritten equation, or diagram. Nexus will solve it step-by-step.</p>
            <div class="go-btn">→</div>
        </div>
    """, unsafe_allow_html=True)
with c2:
    st.markdown("""
        <div class="mod-card">
            <span class="mod-tag">ASK OUT LOUD.</span>
            <h3 class="mod-name">Voice</h3>
            <p class="mod-desc">Hold the mic, ask any doubt mid-lecture, and get a concise answer you can read or play back.</p>
            <div class="go-btn">→</div>
        </div>
    """, unsafe_allow_html=True)

# Row 2
c3, c4 = st.columns(2)
with c3:
    st.markdown("""
        <div class="mod-card" style="border-top: 1px solid #111;">
            <span class="mod-tag">DEBUG. EXPLAIN. BOILERPLATE.</span>
            <h3 class="mod-name">Dev Mode</h3>
            <p class="mod-desc">Paste code to fix bugs, explain algorithms, or scaffold setup for any IDE / language.</p>
            <div class="go-btn">→</div>
        </div>
    """, unsafe_allow_html=True)
with c4:
    st.markdown("""
        <div class="mod-card" style="border-top: 1px solid #111;">
            <span class="mod-tag">ARCHIVE // DOUBT HISTORY</span>
            <h3 class="mod-name">History</h3>
            <p class="mod-desc">Your intellectual runbook. Access every past solution, scanned image, and voice query in one place.</p>
            <div class="go-btn">→</div>
        </div>
    """, unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)
