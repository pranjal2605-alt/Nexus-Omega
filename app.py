import streamlit as st

# --- NEXUS // OMEGA: SPACING & ICON SYNC ---
st.set_page_config(page_title="Nexus // Emergent", layout="wide", initial_sidebar_state="collapsed")

# 💠 THE ENGINE: HIGH-CONTRAST TACTICAL UI
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700;900&family=JetBrains+Mono:wght@500;800&display=swap');
    
    /* Base Onyx Background */
    .stApp { background-color: #000000 !important; color: #FFFFFF !important; font-family: 'Inter', sans-serif !important; }
    header, footer, #MainMenu { visibility: hidden !important; height: 0; }
    .block-container { padding: 0 !important; max-width: 100% !important; }

    /* REFINED COLORS (Muted & Deep) */
    :root { 
        --volt: #CDFF00;    
        --vision: #A855F7;  
        --voice: #EC4899;   
        --dev: #06B6D4;     
        --steel: #F0F0F0;   
        --smoke: #777777;
    }

    /* NAVIGATION: Spaced & Colored Icons */
    .top-nav {
        display: flex; justify-content: space-between; align-items: center;
        padding: 60px 50px 30px 50px; /* Added spacing */
    }
    .n-logo { 
        background: var(--volt); color: #000; font-weight: 900; 
        padding: 12px 24px; font-size: 28px; box-shadow: 0 0 40px rgba(205, 255, 0, 0.2);
    }
    .nav-icons { display: flex; gap: 40px; }
    .nav-icons svg { width: 24px; height: 24px; opacity: 0.6; transition: 0.3s; }
    
    /* Icon-Specific Coloring */
    .icon-dev:hover { fill: var(--dev); filter: drop-shadow(0 0 8px var(--dev)); opacity: 1; }
    .icon-scan:hover { fill: var(--vision); filter: drop-shadow(0 0 8px var(--vision)); opacity: 1; }
    .icon-mic:hover { fill: var(--voice); filter: drop-shadow(0 0 8px var(--voice)); opacity: 1; }
    .icon-hist:hover { fill: var(--volt); filter: drop-shadow(0 0 8px var(--volt)); opacity: 1; }

    /* HERO: Maximum Weight, Balanced Spacing */
    .hero-section { padding: 100px 50px; } /* Increased vertical space */
    .main-title { 
        font-size: 92px; font-weight: 900; line-height: 0.82; 
        letter-spacing: -6px; margin: 0; color: var(--steel);
    }
    .main-title span { color: var(--volt); }
    
    .sub-copy { color: var(--smoke); font-size: 22px; margin-top: 45px; max-width: 650px; line-height: 1.5; }
    .sub-copy b.v { color: var(--vision); text-shadow: 0 0 10px rgba(168, 85, 247, 0.3); }
    .sub-copy b.vo { color: var(--voice); text-shadow: 0 0 10px rgba(236, 72, 153, 0.3); }

    /* GRID: Balanced Tiles */
    .module-grid { display: grid; grid-template-columns: 1fr 1fr; background: #111; gap: 2px; border-top: 1px solid #111; }
    .mod-card { background: #000; padding: 70px 50px; position: relative; min-height: 280px; }
    
    .mod-tag { font-family: 'JetBrains Mono'; font-size: 11px; letter-spacing: 5px; font-weight: 800; margin-bottom: 25px; display: block; }
    .mod-name { font-size: 44px; font-weight: 900; margin: 0; letter-spacing: -2px; color: var(--steel); }
    .mod-desc { color: #555; font-size: 17px; margin-top: 20px; line-height: 1.5; max-width: 85%; }

    .go-btn { 
        position: absolute; top: 70px; right: 50px; 
        width: 55px; height: 55px; background: #0A0A0A; 
        display: flex; align-items: center; justify-content: center;
        border: 1px solid #222; transition: 0.3s;
    }
    .go-btn:hover { border-color: var(--volt); background: #111; }
    </style>
    """, unsafe_allow_html=True)

# --- THE UI ---

# Top Nav with Colored SVG Icons
st.markdown("""
    <div class="top-nav">
        <div class="n-logo">N</div>
        <div class="nav-icons">
            <svg class="icon-dev" viewBox="0 0 24 24" fill="white"><path d="M20 4H4c-1.1 0-2 .9-2 2v12c0 1.1.9 2 2 2h16c1.1 0 2-.9 2-2V6c0-1.1-.9-2-2-2zm-8 10H5v-2h7v2zm7-4H5V8h14v2z"/></svg>
            <svg class="icon-scan" viewBox="0 0 24 24" fill="white"><path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm0 18c-4.41 0-8-3.59-8-8s3.59-8 8-8 8 3.59 8 8-3.59 8-8 8zm-1-13h2v6h-2zm0 8h2v2h-2z"/></svg>
            <svg class="icon-mic" viewBox="0 0 24 24" fill="white"><path d="M12 14c1.66 0 3-1.34 3-3V5c0-1.66-1.34-3-3-3S9 3.34 9 5v6c0 1.66 1.34 3 3 3z"/></svg>
            <svg class="icon-hist" viewBox="0 0 24 24" fill="white"><path d="M13 3c-4.97 0-9 4.03-9 9H1l3.89 3.89.07.14L9 12H6c0-3.87 3.13-7 7-7s7 3.13 7 7-3.13 7-7 7c-1.93 0-3.68-.79-4.94-2.06l-1.42 1.42C8.27 19.99 10.51 21 13 21c4.97 0 9-4.03 9-9s-4.03-9-9-9z"/></svg>
        </div>
    </div>
""", unsafe_allow_html=True)

# Hero Header with breathing room
st.markdown("""
    <div class="hero-section">
        <h1 class="main-title">Your <span>academic<br>weapon</span>, compiled<br>and armed._</h1>
        <p class="sub-copy">One tap to solve doubts with <b class="v">vision</b>, <b class="vo">voice</b>, and a full developer console. No distractions. Just answers.</p>
    </div>
""", unsafe_allow_html=True)

# Feature Grid
st.markdown('<div class="module-grid">', unsafe_allow_html=True)

c1, c2 = st.columns(2)
with c1:
    st.markdown("""<div class="mod-card">
        <span class="mod-tag" style="color:var(--vision)">SNAP IT. SOLVE IT.</span><h3 class="mod-name">Vision</h3>
        <p class="mod-desc">Upload a photo of a textbook problem. Nexus will solve it step-by-step.</p>
        <div class="go-btn" style="color:var(--vision)">→</div>
    </div>""", unsafe_allow_html=True)
with c2:
    st.markdown("""<div class="mod-card">
        <span class="mod-tag" style="color:var(--voice)">ASK OUT LOUD.</span><h3 class="mod-name">Voice</h3>
        <p class="mod-desc">Hold the mic and get a concise answer you can read or play back.</p>
        <div class="go-btn" style="color:var(--voice)">→</div>
    </div>""", unsafe_allow_html=True)

c3, c4 = st.columns(2)
with c3:
    st.markdown("""<div class="mod-card" style="border-top:1px solid #111;">
        <span class="mod-tag" style="color:var(--dev)">DEBUG. EXPLAIN. BOILERPLATE.</span><h3 class="mod-name">Dev Mode</h3>
        <p class="mod-desc">Paste code to fix bugs or scaffold setup for any IDE.</p>
        <div class="go-btn" style="color:var(--dev)">→</div>
    </div>""", unsafe_allow_html=True)
with c4:
    st.markdown("""<div class="mod-card" style="border-top:1px solid #111;">
        <span class="mod-tag" style="color:var(--volt)">ARCHIVE // DOUBT HISTORY</span><h3 class="mod-name">History</h3>
        <p class="mod-desc">Your intellectual runbook. Access every past solution in one place.</p>
        <div class="go-btn" style="color:var(--volt)">→</div>
    </div>""", unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)
