import streamlit as st
import time

# --- CONFIG ---
st.set_page_config(page_title="Nexus", layout="wide", initial_sidebar_state="collapsed")

# --- CSS: THE "EMERGENT" SPEC ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@900&family=JetBrains+Mono:wght@700&display=swap');
    
    :root { --volt: #CDFF00; --bg: #000; --border: #1A1A1A; --gray: #888; }

    /* PURE BLACK CANVAS */
    [data-testid="stAppViewContainer"], .stApp { background-color: #000 !important; }
    header, footer, [data-testid="stHeader"] { display: none !important; }

    /* HEADLINE TYPOGRAPHY */
    .headline {
        font-family: 'Inter'; font-size: 72px; font-weight: 900; 
        line-height: 0.85; letter-spacing: -4px; color: #FFF; 
        padding: 10px 40px; margin-bottom: 10px;
    }
    .headline span { color: var(--volt); }

    /* STAT GRID */
    .stat-grid { 
        display: grid; grid-template-columns: 1fr 1fr; gap: 1px; 
        background: var(--border); border: 1px solid var(--border);
        margin: 20px 40px; 
    }
    .stat-box { background: #000; padding: 25px; }
    .stat-label { font-family: 'JetBrains Mono'; color: #444; font-size: 11px; letter-spacing: 2px; }
    .stat-value { font-family: 'Inter'; color: #FFF; font-size: 42px; font-weight: 900; }

    /* THE BLACK-TEXT INPUT FIX */
    .stTextInput > div > div > input {
        background-color: var(--volt) !important; /* Making it pop like the button */
        color: #000 !important; /* Black text as requested */
        font-family: 'JetBrains Mono' !important;
        font-weight: 800 !important;
        font-size: 20px !important;
        border-radius: 0px !important;
        border: none !important;
        padding: 15px !important;
    }

    /* TERMINAL OUTPUT AREA */
    .terminal-out {
        margin: 20px 40px;
        padding: 20px;
        border: 1px solid var(--volt);
        background: rgba(205, 255, 0, 0.05);
        font-family: 'JetBrains Mono';
        color: var(--volt);
    }
    </style>
    """, unsafe_allow_html=True)

# --- UI LAYOUT ---
st.markdown('<h1 class="headline">Your <span>academic<br>weapon</span>, compiled<br>and armed._</h1>', unsafe_allow_html=True)

# Grid Counters
st.markdown('''
    <div class="stat-grid">
        <div class="stat-box"><div class="stat-label">TOTAL DOUBTS</div><div class="stat-value">01</div></div>
        <div class="stat-box"><div class="stat-label">VISION</div><div class="stat-value">00</div></div>
        <div class="stat-box"><div class="stat-label">VOICE</div><div class="stat-value">00</div></div>
        <div class="stat-box"><div class="stat-label">CODE</div><div class="stat-value">00</div></div>
    </div>
''', unsafe_allow_html=True)

# The Functional Logic
query = st.text_input("COMMAND_LINE", placeholder="ENTER CALCULATION OR QUERY...", label_visibility="collapsed")

if query:
    st.markdown('<div class="terminal-out">', unsafe_allow_html=True)
    st.write(f"PROCESSED_BY_NEXUS //")
    
    try:
        # Handling basic math like 2+2
        result = eval(query)
        st.markdown(f"### RESULT: {result}")
    except:
        st.markdown(f"ANALYZING: {query} ... (API Connection Standby)")
    
    st.markdown('</div>', unsafe_allow_html=True)

# Start Solving Button
st.markdown('<div style="padding: 0 40px;">', unsafe_allow_html=True)
if st.button("✨ START SOLVING"):
    st.toast("Nexus Overdrive Active", icon="🛡️")
st.markdown('</div>', unsafe_allow_html=True)
