import streamlit as st

# --- NEXUS // OMEGA: CHROMATIC SYNC ---
st.set_page_config(page_title="Nexus // Emergent", layout="wide", initial_sidebar_state="collapsed")

# 💠 THE ENGINE: MULTI-ACCENT TACTICAL UI
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700;900&family=JetBrains+Mono:wght@500;800&display=swap');
    
    .stApp { background-color: #000000 !important; color: #FFFFFF !important; font-family: 'Inter', sans-serif !important; }
    header, footer, #MainMenu { visibility: hidden !important; height: 0; }
    .block-container { padding: 0 !important; max-width: 100% !important; }

    /* CHROMATIC PALETTE */
    :root { 
        --volt: #DFFF00;    /* Primary Accent */
        --vision: #A855F7;  /* Purple for Vision */
        --voice: #EC4899;   /* Pink for Voice */
        --dev: #06B6D4;     /* Cyan for Dev */
        --steel: #E0E0E0;   
        --smoke: #666666;
    }

    /* NAVIGATION */
    .top-nav {
        display: flex; justify-content: space-between; align-items: center;
        padding: 50px 35px 20px 35px; border-bottom: 1px solid #111;
    }
    .n-logo { 
        background: var(--volt); color: #000; font-weight: 900; 
        padding: 10px 20px; font-size: 26px; box-shadow: 0 0 35px rgba(223, 255, 0, 0.3);
    }
    .nav-icons { display: flex; gap: 40px; opacity: 0.5; }
    .nav-icons svg { fill: white; width: 22px; height: 22px; }

    /* HERO: Chromatic Highlights */
    .hero-section { padding: 80px 35px; }
    .main-title { 
        font-size: 84px; font-weight: 900; line-height: 0.8; 
        letter-spacing: -6px; margin: 0; color: var(--steel);
    }
    .highlight { color: var(--volt); }
    .v-highlight { color: var(--vision); }
    .vo-highlight { color: var(--voice); }
    
    .sub-copy { color: var(--smoke); font-size: 20px; margin-top: 35px; max-width: 600px; line-height: 1.4; }
    .sub-copy b.v { color: var(--vision); }
    .sub-copy b.vo { color: var(--voice); }

    /* GRID: Module-Specific Accents */
    .module-grid { display: grid; grid-template-columns: 1fr 1fr; background: #111; gap: 1px; border-top: 1px solid #111; }
    .mod-card { background: #000; padding: 60px 35px; position: relative; min-height: 240px; }
    
    .mod-tag { font-family: 'JetBrains Mono'; font-size: 10px; letter-spacing: 4px; font-weight: 800; margin-bottom: 20px; display: block; }
    .tag-vision { color: var(--vision); }
    .tag-voice { color: var(--voice); }
    .tag-dev { color: var(--dev); }
    .tag-hist { color: var(--volt); opacity: 0.7; }

    .mod-name { font-size: 40px; font-weight: 900; margin: 0; letter-spacing: -2px; color: var(--steel); }
    .mod-desc { color: #444; font-size: 16px; margin-top: 15px; line-height: 1.4; max-width: 80%; }

    .go-btn { 
        position: absolute; top: 60px; right: 35px; 
        width: 48px; height: 48px; background: #080808; 
        display: flex; align-items: center; justify-content: center;
        border: 1px solid #1A1A1A;
    }
    </style>
    """, unsafe_allow_html=True)

# --- UI RENDER ---

st.markdown("""
    <div class="top-nav">
        <div class="n-logo">N</div>
        <div class="nav-icons">
            <svg viewBox="0 0 24 24"><path d="M20 4H4c-1.1 0-2 .9-2 2v12c0 1.1.9 2 2 2h16c1.1 0 2-.9 2-2V6c0-1.1-.9-2-2-2zm-8 10H5v-2h7v2zm7-4H5V8h14v2z"/></svg>
            <svg viewBox="0 0 24 24"><path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm0 18c-4.41 0-8-3.59-8-8s3.59-8 8-8 8 3.59 8 8-3.59 8-8 8zm-1-13h2v6h-2zm0 8h2v2h-2z"/></svg>
            <svg viewBox="0 0 24 24"><path d="M12 14c1.66 0 3-1.34 3-3V5c0-1.66-1.34-3-3-3S9 3.34 9 5v6c0 1.66 1.34 3 3 3z"/></svg>
            <svg viewBox="0 0 24 24"><path d="M19 3H5c-1.1 0-2 .9-2 2v14c0 1.1.9 2 2 2h14c1.1 0 2-.9 2-2V5c0-1.1-.9-2-2-2zm0 16H5V5h14v14z"/></svg>
            <svg viewBox="0 0 24 24"><path d="M13 3c-4.97 0-9 4.03-9 9H1l3.89 3.89.07.14L9 12H6c0-3.87 3.13-7 7-7s7 3.13 7 7-3.13 7-7 7c-1.93 0-3.68-.79-4.94-2.06l-1.42 1.42C8.27 19.99 10.51 21 13 21c4.97 0 9-4.03 9-9s-4.03-9-9-9z"/></svg>
        </div>
    </div>
""", unsafe_allow_html=True)

st.markdown("""
    <div class="hero-section">
        <h1 class="main-title">Your <span class="highlight">academic<br>weapon</span>, compiled<br>and armed._</h1>
        <p class="sub-copy">One tap to solve doubts with <b class="v">vision</b>, <b class="vo">voice</b>, and a full developer console. No distractions. Just answers.</p>
    </div>
""", unsafe_allow_html=True)

st.markdown('<div class="module-grid">', unsafe_allow_html=True)

c1, c2 = st.columns(2)
with c1:
    st.markdown("""<div class="mod-card">
        <span class="mod-tag tag-vision">SNAP IT. SOLVE IT.</span><h3 class="mod-name">Vision</h3>
        <p class="mod-desc">Upload a photo of a textbook problem. Nexus will solve it step-by-step.</p>
        <div class="go-btn" style="color:var(--vision)">→</div>
    </div>""", unsafe_allow_html=True)
with c2:
    st.markdown("""<div class="mod-card">
        <span class="mod-tag tag-voice">ASK OUT LOUD.</span><h3 class="mod-name">Voice</h3>
        <p class="mod-desc">Hold the mic and get a concise answer you can read or play back.</p>
        <div class="go-btn" style="color:var(--voice)">→</div>
    </div>""", unsafe_allow_html=True)

c3, c4 = st.columns(2)
with c3:
    st.markdown("""<div class="mod-card" style="border-top:1px solid #111;">
        <span class="mod-tag tag-dev">DEBUG. EXPLAIN. BOILERPLATE.</span><h3 class="mod-name">Dev Mode</h3>
        <p class="mod-desc">Paste code to fix bugs or scaffold setup for any IDE.</p>
        <div class="go-btn" style="color:var(--dev)">→</div>
    </div>""", unsafe_allow_html=True)
with c4:
    st.markdown("""<div class="mod-card" style="border-top:1px solid #111;">
        <span class="mod-tag tag-hist">INTEL RUNBOOK</span><h3 class="mod-name">History</h3>
        <p class="mod-desc">Access every past solution and voice query in one place.</p>
        <div class="go-btn" style="color:var(--volt)">→</div>
    </div>""", unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)
