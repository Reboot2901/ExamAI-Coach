import streamlit as st

def apply_global_styles():
    """Applies the core Premium SaaS styling to the application."""
    st.markdown("""
    <style>
        /* Google Fonts Import */
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=Outfit:wght@400;500;600;700;800&display=swap');

        /* Global Typography & Deep Navy Backgrounds */
        .stApp, .main {
            background: radial-gradient(circle at 50% 0%, #11142b 0%, #03040c 100%);
            background-color: #03040c; 
            color: #F8FAFC;
            font-family: 'Inter', sans-serif;
            background-attachment: fixed;
        }
        
        p, span, div, li, ul {
            font-family: 'Inter', sans-serif;
        }
        
        h1, h2, h3, h4, h5, h6 {
            font-family: 'Outfit', sans-serif;
            letter-spacing: -0.02em;
        }

        /* Hide Streamlit Headers/Footers & Native Element Overrides */
        header {visibility: hidden;}
        footer {visibility: hidden;}
        hr { display: none !important; }
        
        div[data-testid="stVerticalBlock"] {
            gap: 1.5rem !important; 
        }
        
        .block-container {
            padding-top: 2rem !important;
            padding-bottom: 4rem !important;
            max-width: 1100px !important; 
        }

        /* Hero Section */
        .hero-title {
            font-family: 'Outfit', sans-serif;
            font-size: 3.5rem;
            font-weight: 800;
            text-align: left;
            margin-top: 2rem;
            margin-bottom: 0.5rem;
            color: #FFFFFF;
            line-height: 1.1;
            letter-spacing: -0.03em;
        }
        
        .gradient-text {
            background: linear-gradient(135deg, #6366f1 0%, #0ea5e9 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            filter: drop-shadow(0 4px 20px rgba(14, 165, 233, 0.3));
        }
        
        .hero-subtitle {
            text-align: left;
            color: #94A3B8;
            font-size: 1.2rem;
            font-weight: 400;
            margin-bottom: 2rem;
            max-width: 600px;
            line-height: 1.6;
        }

        /* Sidebar Navigation Rail */
        [data-testid="stSidebar"] {
            background: linear-gradient(180deg, rgba(8,11,21,0.98) 0%, rgba(3,4,12,0.98) 100%) !important;
            border-right: 1px solid rgba(255,255,255,0.04);
            color: white;
            min-width: 280px !important;
            max-width: 280px !important;
        }
        
        .sidebar-brand {
            display: flex;
            align-items: center;
            gap: 16px;
            padding: 2rem 1.5rem 1.5rem 1.5rem;
        }
        .brand-icon {
            font-size: 2rem;
            line-height: 1;
            background: linear-gradient(135deg, #6366f1, #0ea5e9);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            filter: drop-shadow(0 2px 10px rgba(14, 165, 233, 0.3));
        }
        .brand-text h2 {
            color: #FFFFFF;
            font-size: 1.25rem;
            font-weight: 800;
            margin: 0;
            line-height: 1.2;
        }
        .brand-text p {
            color: #64748B;
            font-size: 0.8rem;
            margin: 0;
            font-weight: 500;
        }
        
        .sidebar-divider {
            height: 1px;
            background: linear-gradient(90deg, rgba(255,255,255,0), rgba(255,255,255,0.06) 50%, rgba(255,255,255,0));
            margin: 0 1.5rem 1.5rem 1.5rem;
        }
        
        [data-testid="stSidebar"] [data-testid="stVerticalBlock"] {
            gap: 4px !important;
        }
        
        /* Sidebar Native Button Overrides (INACTIVE) */
        [data-testid="stSidebar"] button[data-testid="baseButton-secondary"] {
            width: 90%;
            height: 48px;
            margin: 0 auto 4px auto;
            background: transparent; 
            border: 1px solid transparent; 
            color: #94A3B8;
            text-align: left;
            padding: 0 16px;
            border-radius: 10px;
            font-size: 0.95rem;
            font-family: 'Inter', sans-serif;
            font-weight: 500;
            display: flex;
            align-items: center;
            justify-content: flex-start;
            box-shadow: none;
            transition: all 0.2s ease;
        }
        
        [data-testid="stSidebar"] button[data-testid="baseButton-secondary"]:hover {
            background: rgba(255,255,255,0.03);
            color: #F8FAFC;
        }
        
        /* Sidebar Native Button Overrides (ACTIVE) */
        [data-testid="stSidebar"] button[data-testid="baseButton-primary"] {
            width: 90%;
            height: 48px;
            margin: 0 auto 4px auto;
            background: linear-gradient(90deg, rgba(99,102,241,0.1) 0%, rgba(14,165,233,0.1) 100%);
            border: 1px solid rgba(99,102,241,0.2); 
            color: #38bdf8;
            text-align: left;
            padding: 0 16px;
            border-radius: 10px;
            font-size: 0.95rem;
            font-family: 'Inter', sans-serif;
            font-weight: 600;
            display: flex;
            align-items: center;
            justify-content: flex-start;
            box-shadow: none;
        }

        /* --- Global Form Container & Glass Panels --- */
        .glass-panel, div[data-testid="stForm"], div[data-testid="stVerticalBlockBorderWrapper"] {
            background: rgba(15, 20, 35, 0.4) !important;
            backdrop-filter: blur(24px) !important;
            -webkit-backdrop-filter: blur(24px) !important;
            border: 1px solid rgba(255, 255, 255, 0.05) !important;
            border-radius: 16px !important;
            padding: 2rem !important;
            box-shadow: 0 10px 30px rgba(0, 0, 0, 0.3), inset 0 1px 0 rgba(255,255,255,0.03) !important;
            margin-bottom: 2rem !important;
            transition: all 0.3s ease !important;
        }

        /* --- Input Fields System --- */
        .stTextInput>div>div>input, .stTextArea>div>textarea, .stSelectbox>div>div>div, .stNumberInput>div>div>input {
            background-color: rgba(0, 0, 0, 0.2) !important;
            color: #F8FAFC !important;
            border: 1px solid rgba(255, 255, 255, 0.08) !important;
            border-radius: 10px !important;
            padding: 0 16px !important; 
            height: 48px !important;
            min-height: 48px !important;
            font-size: 0.95rem !important;
            box-shadow: inset 0 2px 4px rgba(0,0,0,0.2) !important;
            transition: border 0.2s ease, box-shadow 0.2s ease !important;
        }
        
        .stTextArea>div>textarea {
            height: auto !important;
            padding: 16px !important;
            line-height: 1.6 !important;
        }

        .stSelectbox label, .stTextInput label, .stTextArea label, .stNumberInput label {
            color: #cbd5e1 !important;
            font-weight: 500 !important;
            font-size: 0.9rem !important;
            margin-bottom: 6px !important;
        }
        
        .stTextInput>div>div>input:focus, .stTextArea>div>textarea:focus, .stSelectbox>div>div>div:focus, .stNumberInput>div>div>input:focus {
            border-color: #38bdf8 !important;
            box-shadow: 0 0 0 1px #38bdf8, inset 0 2px 4px rgba(0,0,0,0.2) !important;
        }

        /* --- Primary Action Buttons --- */
        .action-btn button, div[data-testid="stForm"] button[kind="primary"], .stButton>button[kind="primary"] {
            background: linear-gradient(135deg, #4f46e5 0%, #0ea5e9 100%) !important;
            border: none !important;
            border-radius: 10px !important;
            height: 48px !important;
            color: white !important;
            font-family: 'Outfit', sans-serif !important;
            font-weight: 600 !important;
            box-shadow: 0 4px 14px rgba(14, 165, 233, 0.25), inset 0 1px 0 rgba(255,255,255,0.2) !important;
            transition: all 0.2s ease !important;
        }
        .action-btn button:hover, div[data-testid="stForm"] button[kind="primary"]:hover, .stButton>button[kind="primary"]:hover {
            transform: translateY(-2px) !important;
            box-shadow: 0 6px 20px rgba(14, 165, 233, 0.4), inset 0 1px 0 rgba(255,255,255,0.2) !important;
            filter: brightness(1.1) !important;
        }

        /* Secondary Buttons */
        div[data-testid="stForm"] button[kind="secondary"], .secondary-btn button, .stButton>button[kind="secondary"] {
            background: rgba(255,255,255,0.03) !important;
            border: 1px solid rgba(255,255,255,0.1) !important;
            border-radius: 10px !important;
            height: 48px !important;
            color: #E2E8F0 !important;
            font-family: 'Outfit', sans-serif !important;
            font-weight: 500 !important;
            transition: all 0.2s ease !important;
        }
        div[data-testid="stForm"] button[kind="secondary"]:hover, .secondary-btn button:hover, .stButton>button[kind="secondary"]:hover {
            background: rgba(255,255,255,0.06) !important;
            border-color: rgba(255,255,255,0.2) !important;
            color: white !important;
        }

        /* --- AI Tutor Chat (ChatGPT/Perplexity Style) --- */
        [data-testid="stChatMessage"] {
            background: transparent !important;
            border: none !important;
            padding: 1.5rem !important;
            margin-bottom: 0 !important;
            width: 100% !important;
            max-width: 100% !important;
            display: flex !important;
            gap: 1.5rem !important;
            box-shadow: none !important;
            border-top: 1px solid rgba(255,255,255,0.02) !important;
        }

        /* Assistant Bubble Container */
        [data-testid="stChatMessage"][data-baseweb="block"]:has([data-testid="chatAvatarIcon-assistant"]),
        [data-testid="stChatMessage"][data-baseweb="block"]:has(svg[title="assistant"]) {
            background: rgba(15, 20, 35, 0.4) !important; /* Slight dark highlight for AI */
        }
        
        /* Message Content Text Styling */
        [data-testid="stChatMessage"] [data-testid="stMarkdownContainer"] p {
            font-size: 1rem !important;
            line-height: 1.7 !important;
            color: #F1F5F9 !important;
        }

        /* Chat Input Sticky Bottom */
        [data-testid="stChatInput"] {
            background: rgba(5, 8, 22, 0.85) !important;
            backdrop-filter: blur(20px) !important;
            -webkit-backdrop-filter: blur(20px) !important;
            border: 1px solid rgba(255,255,255,0.08) !important;
            border-radius: 16px !important;
            padding: 4px !important;
            box-shadow: 0 -10px 40px rgba(0,0,0,0.5) !important;
        }
        [data-testid="stChatInput"] textarea {
            color: white !important;
        }
        
        /* Dashboard Interactive Cards System */
        div[data-testid="column"]:has(.premium-card) {
            transition: transform 0.2s ease;
        }
        div[data-testid="column"]:has(.premium-card):hover {
            transform: translateY(-4px);
        }

        .premium-card {
            background: rgba(15, 20, 35, 0.5); 
            backdrop-filter: blur(12px);
            border: 1px solid rgba(255, 255, 255, 0.05); 
            border-radius: 16px; 
            padding: 1.5rem;
            position: relative;
            height: 100%;
            min-height: 240px;
            display: flex;
            flex-direction: column;
            box-shadow: 0 4px 20px rgba(0,0,0,0.2), inset 0 1px 0 rgba(255,255,255,0.02);
            transition: all 0.2s ease;
            cursor: pointer;
        }
        div[data-testid="column"]:hover .premium-card {
            background: rgba(20, 26, 43, 0.7);
            border-color: rgba(255,255,255,0.1);
            box-shadow: 0 10px 30px rgba(0,0,0,0.4), inset 0 1px 0 rgba(255,255,255,0.05);
        }
        
        .card-icon-container {
            width: 48px;
            height: 48px;
            border-radius: 12px;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 1.5rem;
            margin-bottom: 1rem;
            box-shadow: inset 0 1px 0 rgba(255,255,255,0.2);
        }
        
        .premium-card h3 {
            color: #FFFFFF;
            font-size: 1.1rem;
            font-weight: 700;
            margin-bottom: 0.5rem;
        }
        .premium-card p {
            color: #94A3B8;
            font-size: 0.9rem;
            line-height: 1.5;
            flex-grow: 1;
            margin-bottom: 0;
        }

        /* Card Button Mask (Invisible overlay to make whole card clickable) */
        .card-button-wrapper {
            position: absolute;
            top: 0; left: 0; right: 0; bottom: 0;
            opacity: 0;
            z-index: 10;
        }
        /* Make internal streamlit button expand to full height/width and be invisible */
        .card-button-wrapper button {
            width: 100% !important;
            height: 100% !important;
            padding: 0 !important;
            margin: 0 !important;
        }

        /* Gradient Accents for specific cards */
        .theme-indigo-violet .card-icon-container { background: linear-gradient(135deg, #4f46e5 0%, #7c3aed 100%); }
        .theme-cyan-blue .card-icon-container { background: linear-gradient(135deg, #0ea5e9 0%, #3b82f6 100%); }
        .theme-emerald-teal .card-icon-container { background: linear-gradient(135deg, #10b981 0%, #14b8a6 100%); }
        .theme-amber-coral .card-icon-container { background: linear-gradient(135deg, #f59e0b 0%, #f43f5e 100%); }
        .theme-magenta-purple .card-icon-container { background: linear-gradient(135deg, #db2777 0%, #9333ea 100%); }

        /* Global Header Typography */
        .page-header {
            margin-top: 2rem; 
            margin-bottom: 0.5rem; 
            display: flex; 
            align-items: center; 
            gap: 1rem;
        }
        .page-header-icon {
            font-size: 2rem;
            background: rgba(255, 255, 255, 0.05);
            border-radius: 12px;
            padding: 10px;
            display: flex;
            align-items: center;
            justify-content: center;
            border: 1px solid rgba(255, 255, 255, 0.08);
            box-shadow: inset 0 1px 0 rgba(255,255,255,0.05);
        }
        .page-header-title {
            margin: 0; 
            font-size: 2.2rem; 
            font-weight: 800; 
            color: #F8FAFC; 
        }
        .page-subtitle {
            color: #94A3B8; 
            font-size: 1.05rem; 
            margin-bottom: 2rem;
            font-weight: 400;
        }
    </style>
    """, unsafe_allow_html=True)

def render_page_header(icon, title, subtitle):
    """
    Renders the standardized top page header across all tools.
    Must be called at the beginning of each module.
    """
    render_back_button()
    st.markdown(f'''
    <div class="page-header">
        <div class="page-header-icon">{icon}</div>
        <h1 class="page-header-title">{title}</h1>
    </div>
    <p class="page-subtitle">{subtitle}</p>
    ''', unsafe_allow_html=True)

def render_back_button():
    """Renders a consistent subtle back button."""
    if st.button("⬅ Back to Dashboard", key=f"back_btn_{st.session_state.page}"):
        st.session_state.page = "Dashboard"
        st.rerun()

def render_separator():
    """Renders a subtle gradient divider."""
    st.markdown('<div class="sidebar-divider" style="margin: 32px 0;"></div>', unsafe_allow_html=True)