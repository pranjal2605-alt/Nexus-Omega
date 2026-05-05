import streamlit as st
from datetime import datetime

# --- SYSTEM CONFIG ---
st.set_page_config(page_title="Nexus // Emergent", layout="wide", initial_sidebar_state="collapsed")

# 1. THE BRAIN (Logic Engine)
if 'page' not in st.session_state:
    st.session_state.page = 'home'
if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []

def process_nexus_query(q):
    """Simple 'Brain' to handle queries"""
    q = q.lower()
    if "hello" in q or "hi" in q: return "Systems online. Standing by for academic or tactical input."
    if "code" in q or "python" in q: return "Terminal ready. I can help with Ursina engine or logic scripts."
    if "watch" in q: return "Horology module active. Titan or Casio specs available."
    return f"Query '{q}' analyzed. I'm searching the Nexus database for the best solution..."

# 2. THE CSS (Fixing Visibility & Search Bar)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@900&family=JetBrains+Mono:wght@500;800&display=swap');
    
    :root { --volt: #CDFF00; --bg: #000000; }

    /* FORCE VISIBILITY */
    [data-testid="stAppViewContainer"], .stApp { background-color: var(--bg) !important; }
    header, footer, .stDeployButton { display: none !important; }
    [data-testid="stMainViewContainer"] > section > div { max-width: 100vw !important; padding: 0 !important; }

    /* TOP UTILITY BAR */
    .top-bar {
        display: flex; justify-content: space-between; align-items: center;
        padding: 15px 50px; border-bottom: 1px solid #111;
    }
    .sys-clock { font-family: 'JetBrains Mono'; color: var(--volt); font-size: 13px; letter-spacing: 3px; }
    
    /* TOP RIGHT ICONS EXPLAINED: 
       Icon 1: System Status (Active/Idle)
       Icon 2: Network Link
       Icon 3: Security Protocol 
    */
    .status-icons { display: flex; gap: 12px; }
    .s-icon { width: 14px; height: 14px; border: 1px solid #333; border-radius: 2px; }
    .s-icon.active { background: var(--volt); border-color: var(--volt); box-shadow: 0 0 8px var(--volt); }

    /* ASK NEXUS: FIXING WHITE-ON-WHITE VISIBILITY */
    div[data-baseweb="input"] {
        background-color: #111 !important;
        border: 1px solid #222 !important;
    }
    input { 
        color: #FFFFFF !important; /* Forces text to be white on dark background */
        caret-color: var(--volt) !important;
        font-family: 'JetBrains Mono' !important;
    }
    ::placeholder { color: #444 !important; }

    /* THE GRID */
    .grid-container { display: grid; grid-template-columns: 1fr 1fr; background: #111; gap: 1px; }
    .grid-item { background: var(--bg); padding: 80px 50px; cursor: pointer; }
    .item-title { font-family: 'Inter'; font-size: 50px; font-weight: 900; color: #FFF; margin: 0; }
    
    /* SQUASHED HEADLINE */
    .headline {
        font-family: 'Inter'; font-size: 8vw; font-weight: 900; line-height: 0.8;
        letter-spacing: -0.05em; color: #FFF; padding: 40px 50px;
    }
    .headline span { color: var(--volt); }
    </style>
    """, unsafe_allow_html=True)

# --- TOP BAR RENDER ---
st.markdown(f"""
    <div class="top-bar">
        <div style="display:flex; gap:10px; align-items:center;">
            <div style="width:8px; height:8px; background:var(--volt); border-radius:50%;"></div>
            <div class="sys-clock">{datetime.now().strftime("%H:%M:%S")}</div>
        </div>
        <div class="status-icons">
            <div class="s-icon active"></div>
            <div class="s-icon active"></div>
            <div class="s-icon"></div>
        </div>
    </div>
""", unsafe_allow_html=True)

# --- PAGE ROUTING ---
if st.session_state.page == 'home':
    st.markdown('<div style="padding: 40px 50px;"><div style="background:var(--volt); color:black; font-weight:900; width:50px; height:50px; display:flex; align-items:center; justify-content:center; font-size:24px;">N</div></div>', unsafe_allow_html=True)
    st.markdown('<h1 class="headline">Your <span>academic<br>weapon</span>, armed._</h1>', unsafe_allow_html=True)
    
    # FUNCTIONAL SEARCH BAR
    query = st.text_input("Ask Nexus", placeholder="INPUT COMMAND OR QUESTION...", label_visibility="collapsed")
    if query:
        response = process_nexus_query(query)
        st.markdown(f'<div style="padding:0 50px 20px 50px; font-family:JetBrains Mono; color:var(--volt);">> {response}</div>', unsafe_allow_html=True)

    # GRID
    st.markdown('<div class="grid-container">', unsafe_allow_html=True)
    c1, c2 = st.columns(2)
    with c1:
        st.markdown('<div class="grid-item"><h2 class="item-title">Vision</h2></div>', unsafe_allow_html=True)
        if st.button("OPEN VISION", key="v"): st.session_state.page = 'vision'
    with c2:
        st.markdown('<div class="grid-item"><h2 class="item-title">Voice</h2></div>', unsafe_allow_html=True)
        if st.button("OPEN VOICE", key="vo"): st.session_state.page = 'voice'
    
    c3, c4 = st.columns(2)
    with c3:
        st.markdown('<div class="grid-item"><h2 class="item-title">Omega AI</h2></div>', unsafe_allow_html=True)
        if st.button("OPEN OMEGA", key="om"): st.session_state.page = 'omega'
    with c4:
        st.markdown('<div class="grid-item"><h2 class="item-title">Dev Terminal</h2></div>', unsafe_allow_html=True)
        if st.button("OPEN DEV", key="dev"): st.session_state.page = 'dev'
    st.markdown('</div>', unsafe_allow_html=True)

elif st.session_state.page == 'omega':
    st.markdown('<div style="padding:50px;">', unsafe_allow_html=True)
    if st.button("← EXIT TO HOME"): st.session_state.page = 'home'
    st.markdown("<h1 style='color:var(--volt); font-family:Inter; font-weight:900; font-size:60px;'>OMEGA_SYS</h1>", unsafe_allow_html=True)
    chat_input = st.chat_input("Chat with Omega...")
    if chat_input:
        st.session_state.chat_history.append({"role": "user", "content": chat_input})
        st.session_state.chat_history.append({"role": "assistant", "content": f"Omega analyzing: '{chat_input}'. System status nominal."})
    for msg in st.session_state.chat_history:
        st.chat_message(msg["role"]).write(msg["content"])

elif st.session_state.page == 'vision':
    st.markdown('<div style="padding:50px;">', unsafe_allow_html=True)
    if st.button("← EXIT TO HOME"): st.session_state.page = 'home'
    st.camera_input("SCAN_ASSIGNMENT")

elif st.session_state.page == 'dev':
    st.markdown('<div style="padding:50px;">', unsafe_allow_html=True)
    if st.button("← EXIT TO HOME"): st.session_state.page = 'home'
    st.code("import python_logic\n# Current Project: Neon Heist Syndicate", language="python")
