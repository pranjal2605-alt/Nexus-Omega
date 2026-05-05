import streamlit as st
import PIL.Image as Image

# --- CONFIG ---
st.set_page_config(page_title="Nexus", layout="wide", initial_sidebar_state="collapsed")

# --- CSS: THE "EMERGENT" PROTOCOL (EXACT MATCH) ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@900&family=JetBrains+Mono:wght@700&display=swap');
    :root { --volt: #CDFF00; --vision: #A855F7; --voice: #EC4899; --dev: #FACC15; }
    
    [data-testid="stAppViewContainer"], .stApp { background-color: #000 !important; }
    header, footer, [data-testid="stHeader"] { display: none !important; }

    /* TYPOGRAPHY */
    .headline { font-family: 'Inter'; font-size: 72px; font-weight: 900; line-height: 0.85; letter-spacing: -4px; color: #FFF; padding: 20px 40px; }
    .headline span { color: var(--volt); }
    .sub-text { font-family: 'Inter'; color: #666; font-size: 18px; padding-left: 40px; margin-bottom: 30px; }

    /* MODULE CARDS */
    .mod-container { padding: 0 40px; margin-bottom: 20px; }
    .mod-card { background: #000; border-left: 4px solid #111; padding: 20px; margin-bottom: 10px; }
    .mod-tag { font-family: 'JetBrains Mono'; color: #444; font-size: 10px; letter-spacing: 2px; text-transform: uppercase; }
    .mod-title { font-family: 'Inter'; font-size: 32px; font-weight: 900; color: #FFF; margin: 0; }

    /* THE BLACK-TEXT INPUT (PER YOUR SCREENSHOT image_0e415f.png) */
    .stTextInput > div > div > input {
        background-color: var(--volt) !important;
        color: #000 !important;
        font-family: 'JetBrains Mono' !important;
        font-weight: 800 !important;
        border-radius: 0px !important;
        border: none !important;
        padding: 15px !important;
    }

    /* OUTPUT BOX */
    .terminal-output { 
        background: #050505; border: 1px solid #111; padding: 20px; 
        font-family: 'JetBrains Mono'; color: var(--volt); margin: 10px 40px; 
    }
    </style>
    """, unsafe_allow_html=True)

# --- UI CONTENT ---
st.markdown('<h1 class="headline">Your <span>academic<br>weapon</span>, compiled<br>and armed._</h1>', unsafe_allow_html=True)
st.markdown('<div class="sub-text">One tap to solve doubts with <b>vision</b>, <b>voice</b>, and <b>dev mode</b>.</div>', unsafe_allow_html=True)

# --- MODULE 01: VISION ---
st.markdown('<div class="mod-container"><div class="mod-card" style="border-color:var(--vision)"><p class="mod-tag">MODULE 01 // VISION</p><h2 class="mod-title">Snap a problem.</h2></div></div>', unsafe_allow_html=True)
v_file = st.file_uploader("UPLOAD IMAGE", type=['png', 'jpg'], label_visibility="collapsed")

# --- MODULE 02: VOICE ---
st.markdown('<div class="mod-container"><div class="mod-card" style="border-color:var(--voice)"><p class="mod-tag">MODULE 02 // VOICE</p><h2 class="mod-title">Ask out loud.</h2></div></div>', unsafe_allow_html=True)
if st.button("🎤 ACTIVATE MIC"):
    st.info("Listening...")

# --- MODULE 03: DEV MODE / SOLVER ---
st.markdown('<div class="mod-container"><div class="mod-card" style="border-color:var(--dev)"><p class="mod-tag">MODULE 03 // DEV MODE</p><h2 class="mod-title">Solve / Debug.</h2></div></div>', unsafe_allow_html=True)

# The Calculator/Solver Input
query = st.text_input("COMMAND", placeholder="TYPE 2+2 OR CODE HERE...", label_visibility="collapsed")

if query:
    st.markdown('<div class="terminal-output">', unsafe_allow_html=True)
    try:
        # EXECUTES MATH OR PYTHON LOGIC
        result = eval(query)
        st.code(f"> RESULT: {result}", language="bash")
    except Exception as e:
        st.code(f"> ERROR: {e}", language="bash")
    st.markdown('</div>', unsafe_allow_html=True)

# --- FINAL ACTION ---
st.markdown('<div style="padding: 20px 40px;">', unsafe_allow_html=True)
if st.button("✨ START SOLVING"):
    st.success("NEXUS DEPLOYED")
st.markdown('</div>', unsafe_allow_html=True)
