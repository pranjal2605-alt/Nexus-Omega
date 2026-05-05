import streamlit as st
import PIL.Image as Image

# --- OS CONFIG ---
st.set_page_config(page_title="Nexus", layout="wide", initial_sidebar_state="collapsed")

# --- CSS: THE "EMERGENT" PROTOCOL ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@900&family=JetBrains+Mono:wght@700&display=swap');
    :root { --volt: #CDFF00; }
    
    [data-testid="stAppViewContainer"] { background-color: #000 !important; }
    header, footer { display: none !important; }

    /* TYPOGRAPHY MATCHING 1000244729_7.mp4 */
    .headline { font-family: 'Inter'; font-size: 72px; font-weight: 900; line-height: 0.85; letter-spacing: -4px; color: #FFF; padding: 40px 40px 10px 40px; }
    .headline span { color: var(--volt); }

    /* THE BLACK-TEXT INPUT (PER image_0e415f.png) */
    .stTextInput > div > div > input {
        background-color: var(--volt) !important;
        color: #000 !important;
        font-family: 'JetBrains Mono' !important;
        font-weight: 800 !important;
        border-radius: 0px !important;
        border: none !important;
        padding: 20px !important;
        font-size: 22px !important;
    }

    /* TACTICAL OUTPUT AREA */
    .output-box { 
        margin: 20px 40px; padding: 30px; 
        border: 1px solid #1A1A1A; background: #050505;
        font-family: 'JetBrains Mono'; color: var(--volt);
    }
    .brain-icon { font-size: 40px; margin-bottom: 10px; }
    </style>
    """, unsafe_allow_html=True)

# --- UI CONTENT ---
st.markdown('<h1 class="headline">ASK<br><span>NEXUS</span>_</h1>', unsafe_allow_html=True)

# --- THE INPUT BRAIN ---
st.markdown('<div style="padding: 0 40px;">', unsafe_allow_html=True)
query = st.text_input("COMMAND", placeholder="2+2 OR ASK ANYTHING...", label_visibility="collapsed")
st.markdown('</div>', unsafe_allow_html=True)

# --- LOGIC HANDLING ---
if query:
    st.markdown('<div class="output-box">', unsafe_allow_html=True)
    st.markdown('<div class="brain-icon">🧠</div>', unsafe_allow_html=True)
    st.write("NEXUS_CORE // PROCESSING")
    
    try:
        # This handles the 2+2 math logic
        result = eval(query)
        st.markdown(f"## {result}")
    except:
        # Fallback for text questions
        st.markdown(f"### Analyzing: {query}")
        st.info("Direct logic applied to input.")
    
    st.markdown('</div>', unsafe_allow_html=True)

# --- QUICK ACTION MODULES (FROM VIDEO) ---
col1, col2, col3 = st.columns(3)
with col1:
    if st.button("📷 VISION"):
        st.file_uploader("DROP IMAGE", type=['png', 'jpg'], label_visibility="collapsed")
with col2:
    if st.button("🎤 VOICE"):
        st.write("Listening...")
with col3:
    if st.button("💻 CODE"):
        st.write("Dev Mode Active")

# --- START BUTTON ---
st.markdown('<div style="padding: 20px 40px;">', unsafe_allow_html=True)
if st.button("✨ START SOLVING"):
    st.toast("Nexus Brain Engaged")
st.markdown('</div>', unsafe_allow_html=True)
