import streamlit as st

# --- CORE CONFIG ---
st.set_page_config(page_title="Nexus", layout="wide", initial_sidebar_state="collapsed")

# --- CSS: THE "EMERGENT" PROTOCOL ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@900&family=JetBrains+Mono:wght@700&display=swap');
    :root { --volt: #CDFF00; }
    
    /* ABSOLUTE DARKNESS */
    [data-testid="stAppViewContainer"], .stApp { background-color: #000 !important; }
    header, footer, [data-testid="stHeader"] { display: none !important; }

    /* TYPOGRAPHY */
    .headline { 
        font-family: 'Inter'; font-size: 82px; font-weight: 900; 
        line-height: 0.85; letter-spacing: -5px; color: var(--volt); 
        padding: 60px 40px 20px 40px; text-transform: uppercase;
    }

    /* THE VOLT INPUT BOX (MATCHING YOUR SCREENSHOT) */
    .stTextInput > div > div > input {
        background-color: var(--volt) !important;
        color: #000 !important;
        font-family: 'JetBrains Mono' !important;
        font-weight: 900 !important;
        font-size: 24px !important;
        border-radius: 4px !important;
        border: none !important;
        padding: 25px !important;
    }

    /* TACTICAL BUTTONS (NO WHITE BACKGROUNDS) */
    .stButton > button {
        background-color: transparent !important;
        color: #FFF !important;
        border: 1px solid #333 !important;
        font-family: 'JetBrains Mono' !important;
        text-transform: uppercase;
        letter-spacing: 2px;
        font-size: 14px !important;
        padding: 10px 20px !important;
        border-radius: 4px !important;
    }
    .stButton > button:hover { border-color: var(--volt) !important; color: var(--volt) !important; }

    /* BRAIN OUTPUT AREA */
    .nexus-terminal {
        margin: 20px 40px; padding: 40px;
        background: #050505; border-left: 5px solid var(--volt);
        font-family: 'JetBrains Mono'; color: #FFF;
    }
    .nexus-status { color: var(--volt); font-size: 12px; margin-bottom: 20px; letter-spacing: 3px; }
    </style>
    """, unsafe_allow_html=True)

# --- INTERFACE ---
st.markdown('<h1 class="headline">ASK<br>NEXUS_</h1>', unsafe_allow_html=True)

# --- THE INPUT BRAIN ---
st.markdown('<div style="padding: 0 40px;">', unsafe_allow_html=True)
query = st.text_input("COMMAND", placeholder="TYPE 2+2 OR ANALYZE...", label_visibility="collapsed")
st.markdown('</div>', unsafe_allow_html=True)

# --- LOGIC HANDLING (THE BRAIN) ---
if query:
    st.markdown('<div class="nexus-terminal">', unsafe_allow_html=True)
    st.markdown('<div class="nexus-status">NEXUS_CORE // ACTIVE_PROCESS</div>', unsafe_allow_html=True)
    
    try:
        # This handles the 2+2 logic and Python math
        result = eval(query)
        st.markdown(f"### RESULT: {result}")
    except Exception:
        # Fallback for text-based reasoning
        st.markdown(f"### ANALYZING: {query}")
        st.write("Deploying deep-logic solvers for your request...")
    
    st.markdown('</div>', unsafe_allow_html=True)

# --- ACTION ROW ---
st.markdown('<div style="padding: 20px 40px;">', unsafe_allow_html=True)
col1, col2, col3, col4 = st.columns([1,1,1,2])
with col1:
    if st.button("📷 VISION"): st.toast("Camera Interface Ready")
with col2:
    if st.button("🎤 VOICE"): st.toast("Microphone Active")
with col3:
    if st.button("💻 CODE"): st.toast("Compiler Ready")
with col4:
    if st.button("✨ START SOLVING"): st.balloons()
st.markdown('</div>', unsafe_allow_html=True)
