import streamlit as st

# --- CORE CONFIG ---
st.set_page_config(page_title="Nexus", layout="wide", initial_sidebar_state="collapsed")

# --- CSS: THE EXACT "NEXUS" SPEC ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@900&family=JetBrains+Mono:wght@700&display=swap');
    :root { --volt: #CDFF00; --vision: #A855F7; --voice: #EC4899; }
    
    [data-testid="stAppViewContainer"], .stApp { background-color: #000 !important; }
    header, footer, [data-testid="stHeader"] { display: none !important; }

    /* HEADER BLOCK */
    .header-box { padding: 40px 40px 10px 40px; }
    .session-line { width: 60px; height: 2px; background: #444; margin-bottom: 10px; }
    .session-id { font-family: 'JetBrains Mono'; color: #444; font-size: 14px; letter-spacing: 3px; }
    .headline { font-family: 'Inter'; font-size: 72px; font-weight: 900; line-height: 0.85; color: #FFF; margin-top: 20px; }
    .headline span { color: var(--volt); }
    .sub-desc { font-family: 'Inter'; color: #888; font-size: 18px; max-width: 500px; padding: 20px 0; }

    /* MODULE CARD STYLING */
    .mod-section { border-top: 1px solid #111; padding: 60px 40px; }
    .mod-tag { font-family: 'JetBrains Mono'; color: #444; font-size: 10px; letter-spacing: 2px; margin-bottom: 5px; }
    .mod-subtitle { font-family: 'JetBrains Mono'; color: #FFF; font-size: 18px; margin-bottom: 10px; text-transform: uppercase; }
    .mod-title { font-family: 'Inter'; font-size: 56px; font-weight: 900; color: #FFF; margin: 0; line-height: 1; }
    .v-text { color: var(--vision); } .vo-text { color: var(--voice); }

    /* THE BLACK-ON-VOLT BUTTONS */
    .stButton > button {
        background-color: var(--volt) !important; color: #000 !important;
        font-family: 'Inter' !important; font-weight: 900 !important;
        width: 100% !important; border-radius: 0px !important; border: none !important;
        padding: 20px !important; text-transform: uppercase; letter-spacing: 1px;
    }

    /* DASHBOARD GRID */
    .stat-grid { display: grid; grid-template-columns: repeat(2, 1fr); gap: 1px; background: #111; border: 1px solid #111; margin-top: 40px; }
    .stat-box { background: #000; padding: 30px; }
    .stat-label { font-family: 'JetBrains Mono'; color: #444; font-size: 11px; }
    .stat-value { font-family: 'Inter'; color: #FFF; font-size: 42px; font-weight: 900; }
    </style>
    """, unsafe_allow_html=True)

# --- TOP HEADER ---
st.markdown('''
    <div class="header-box">
        <div class="session-line"></div>
        <div class="session-id">SESSION // 000</div>
        <h1 class="headline">Your <span>academic<br>weapon</span>,<br>compiled and<br>armed._</h1>
        <p class="sub-desc">One tap to solve doubts with vision, voice, and dev mode. No distractions. Just answers.</p>
    </div>
''', unsafe_allow_html=True)

# --- MODULE 01: VISION ---
st.markdown('<div class="mod-section">', unsafe_allow_html=True)
st.markdown('<p class="mod-tag">MODULE 01 // VISION-TO-SOLUTION</p>', unsafe_allow_html=True)
st.markdown('<p class="mod-subtitle">SNAP IT. SOLVE IT.</p>', unsafe_allow_html=True)
st.markdown('<h2 class="mod-title v-text">Vision</h2>', unsafe_allow_html=True)
st.file_uploader("UPLOAD IMAGE", type=['png', 'jpg'], label_visibility="collapsed")
if st.button("📷 SOLVE WITH NEXUS"): st.write("ANALYZING...")
st.markdown('</div>', unsafe_allow_html=True)

# --- MODULE 02: VOICE ---
st.markdown('<div class="mod-section">', unsafe_allow_html=True)
st.markdown('<p class="mod-tag">MODULE 02 // VOICE-TO-KNOWLEDGE</p>', unsafe_allow_html=True)
st.markdown('<p class="mod-subtitle">ASK OUT LOUD.</p>', unsafe_allow_html=True)
st.markdown('<h2 class="mod-title vo-text">Voice</h2>', unsafe_allow_html=True)
if st.button("🎤 TAP TO SPEAK"): st.info("Nexus is listening...")
st.markdown('</div>', unsafe_allow_html=True)

# --- MODULE 03: DEV MODE ---
st.markdown('<div class="mod-section">', unsafe_allow_html=True)
st.markdown('<p class="mod-tag">MODULE 03 // DEV MODE</p>', unsafe_allow_html=True)
st.markdown('<p class="mod-subtitle">DEBUG. EXPLAIN. SCAFFOLD.</p>', unsafe_allow_html=True)
st.markdown('<h2 class="mod-title" style="color:var(--volt)">Dev Mode</h2>', unsafe_allow_html=True)
code_input = st.text_input("INPUT", placeholder="2+2 OR CODE...", label_visibility="collapsed")
if code_input:
    try:
        st.code(f"> RESULT: {eval(code_input)}")
    except:
        st.write("NEXUS_CORE // PROCESSING...")
if st.button("💻 RUN NEXUS"): st.success("BRAIN ENGAGED")
st.markdown('</div>', unsafe_allow_html=True)

# --- DASHBOARD ---
st.markdown('<div class="stat-grid">'
            '<div class="stat-box"><div class="stat-label">TOTAL DOUBTS</div><div class="stat-value">00</div></div>'
            '<div class="stat-box"><div class="stat-label">VISION</div><div class="stat-value">00</div></div>'
            '<div class="stat-box"><div class="stat-label">VOICE</div><div class="stat-value">00</div></div>'
            '<div class="stat-box"><div class="stat-label">CODE</div><div class="stat-value">00</div></div>'
            '</div>', unsafe_allow_html=True)

# --- FINAL FOOTER ---
st.markdown('<div style="padding: 40px; text-align: center; color: #333; font-family: JetBrains Mono; font-size: 10px;">NEXUS_OS // VERSION_1.0</div>', unsafe_allow_html=True)
