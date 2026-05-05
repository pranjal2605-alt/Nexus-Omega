import streamlit as st

# --- CORE CONFIG ---
st.set_page_config(page_title="Nexus", layout="wide", initial_sidebar_state="collapsed")

# --- CSS: THE "EMERGENT" PROTOCOL ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@900&family=JetBrains+Mono:wght@700&display=swap');
    :root { --volt: #CDFF00; --vision: #A855F7; --voice: #EC4899; }
    
    [data-testid="stAppViewContainer"], .stApp { background-color: #000 !important; }
    header, footer, [data-testid="stHeader"] { display: none !important; }

    /* TYPOGRAPHY */
    .headline { font-family: 'Inter'; font-size: 82px; font-weight: 900; line-height: 0.85; letter-spacing: -5px; color: #FFF; padding: 40px 40px 10px 40px; }
    .headline span { color: var(--volt); }
    .sub-text { font-family: 'Inter'; color: #666; font-size: 18px; padding-left: 40px; margin-bottom: 30px; }

    /* MODULE HEADERS */
    .mod-header { border-left: 4px solid #222; padding: 20px 40px; margin: 20px 0; background: #050505; }
    .v-border { border-color: var(--vision) !important; }
    .vo-border { border-color: var(--voice) !important; }
    .mod-tag { font-family: 'JetBrains Mono'; color: #444; font-size: 10px; letter-spacing: 2px; }
    .mod-title { font-family: 'Inter'; font-size: 32px; font-weight: 900; color: #FFF; margin: 0; }

    /* STAT DASHBOARD */
    .stat-grid { display: grid; grid-template-columns: repeat(2, 1fr); gap: 1px; background: #1A1A1A; border: 1px solid #1A1A1A; margin: 20px 40px; }
    .stat-box { background: #000; padding: 30px; }
    .stat-label { font-family: 'JetBrains Mono'; color: #444; font-size: 12px; letter-spacing: 2px; }
    .stat-value { font-family: 'Inter'; color: #FFF; font-size: 48px; font-weight: 900; }

    /* THE BLACK-TEXT INPUT (MATCHING image_0e415f.png) */
    .stTextInput > div > div > input {
        background-color: var(--volt) !important;
        color: #000 !important;
        font-family: 'JetBrains Mono' !important;
        font-weight: 900 !important;
        border-radius: 0px !important;
        border: none !important;
        padding: 20px !important;
    }

    /* THE BRAIN OUTPUT */
    .nexus-output { margin: 20px 40px; padding: 30px; background: #050505; border: 1px solid var(--volt); font-family: 'JetBrains Mono'; color: var(--volt); }
    </style>
    """, unsafe_allow_html=True)

# --- UI START ---
st.markdown('<h1 class="headline">Your <span>academic<br>weapon</span>, compiled<br>and armed._</h1>', unsafe_allow_html=True)
st.markdown('<div class="sub-text">One tap to solve doubts with vision, voice, and dev mode.</div>', unsafe_allow_html=True)

# --- MODULE 01: VISION ---
st.markdown('<div class="mod-header v-border"><p class="mod-tag">MODULE 01 // VISION-TO-SOLUTION</p><h2 class="mod-title">Snap a problem.</h2></div>', unsafe_allow_html=True)
v_file = st.file_uploader("DROP IMAGE", type=['png', 'jpg'], label_visibility="collapsed")

# --- MODULE 02: VOICE ---
st.markdown('<div class="mod-header vo-border"><p class="mod-tag">MODULE 02 // VOICE-TO-KNOWLEDGE</p><h2 class="mod-title">Ask out loud.</h2></div>', unsafe_allow_html=True)
if st.button("🎤 TAP TO SPEAK"): st.info("Nexus is listening...")

# --- MODULE 03: DEV MODE (THE BRAIN) ---
st.markdown('<div class="mod-header"><p class="mod-tag">MODULE 03 // DEV MODE</p><h2 class="mod-title">Debug. Explain.</h2></div>', unsafe_allow_html=True)
query = st.text_input("COMMAND", placeholder="TYPE 2+2 OR CODE HERE...", label_visibility="collapsed")

if query:
    st.markdown('<div class="nexus-output">', unsafe_allow_html=True)
    try:
        # THE BRAIN: Executes math and logic
        result = eval(query)
        st.code(f"> INPUT: {query}\n> RESULT: {result}", language="python")
    except Exception as e:
        st.code(f"> ERROR: {e}", language="python")
    st.markdown('</div>', unsafe_allow_html=True)

# --- STAT DASHBOARD ---
st.markdown('<div class="stat-grid">'
            '<div class="stat-box"><div class="stat-label">TOTAL DOUBTS</div><div class="stat-value">00</div></div>'
            '<div class="stat-box"><div class="stat-label">VISION</div><div class="stat-value">00</div></div>'
            '<div class="stat-box"><div class="stat-label">VOICE</div><div class="stat-value">00</div></div>'
            '<div class="stat-box"><div class="stat-label">CODE</div><div class="stat-value">00</div></div>'
            '</div>', unsafe_allow_html=True)

# --- FINAL SOLVE BUTTON ---
st.markdown('<div style="padding: 20px 40px;">', unsafe_allow_html=True)
if st.button("✨ START SOLVING"): st.success("NEXUS DEPLOYED")
st.markdown('</div>', unsafe_allow_html=True)
