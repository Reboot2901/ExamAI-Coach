import streamlit as st


def apply_global_styles():
    """Apply premium AI SaaS dark theme with deep blue/purple glassmorphism."""
    st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=Outfit:wght@400;500;600;700;800&display=swap');

        /* === GLOBAL BACKGROUND === */
        .stApp, .main {
            background: radial-gradient(circle at 30% 0%, #1e1b4b 0%, #020617 70%);
            background-color: #020617;
            color: #F8FAFC;
            font-family: 'Inter', sans-serif;
            background-attachment: fixed;
        }

        p, span, div, li, ul { font-family: 'Inter', sans-serif; }
        h1, h2, h3, h4, h5, h6 { font-family: 'Outfit', sans-serif; letter-spacing: -0.02em; }

        /* === HIDE CLUTTER === */
        header { visibility: hidden; }
        footer { visibility: hidden; }
        hr { display: none !important; }
        [data-testid="stDecoration"] { display: none !important; }

        /* === LAYOUT === */
        .block-container {
            padding-top: 2rem !important;
            padding-bottom: 4rem !important;
            max-width: 1120px !important;
        }

        div[data-testid="stVerticalBlock"] { gap: 1.25rem !important; }

        /* === HERO === */
        .hero-title {
            font-family: 'Outfit', sans-serif;
            font-size: 3.2rem;
            font-weight: 800;
            color: #FFFFFF;
            line-height: 1.1;
            letter-spacing: -0.03em;
            margin-bottom: 0.5rem;
        }
        .gradient-text {
            background: linear-gradient(135deg, #818cf8 0%, #38bdf8 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }
        .hero-subtitle {
            color: #94A3B8;
            font-size: 1.1rem;
            font-weight: 400;
            line-height: 1.6;
            margin-bottom: 2rem;
            max-width: 580px;
        }

        /* === SIDEBAR === */
        [data-testid="stSidebar"] {
            background: linear-gradient(180deg, rgba(10,12,30,0.99) 0%, rgba(2,6,23,0.99) 100%) !important;
            border-right: 1px solid rgba(255,255,255,0.04);
            min-width: 275px !important;
            max-width: 275px !important;
        }
        .sidebar-brand {
            display: flex;
            align-items: center;
            gap: 14px;
            padding: 2rem 1.5rem 1.5rem;
        }
        .brand-icon {
            font-size: 1.8rem;
            background: linear-gradient(135deg, #818cf8, #38bdf8);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }
        .brand-text h2 { color: #FFFFFF; font-size: 1.2rem; font-weight: 800; margin: 0; }
        .brand-text p { color: #64748B; font-size: 0.78rem; margin: 0; }
        .sidebar-divider {
            height: 1px;
            background: linear-gradient(90deg, transparent, rgba(255,255,255,0.07) 50%, transparent);
            margin: 0 1.5rem 1.25rem;
        }
        [data-testid="stSidebar"] [data-testid="stVerticalBlock"] { gap: 3px !important; }

        /* Sidebar buttons - inactive */
        [data-testid="stSidebar"] button[data-testid="baseButton-secondary"] {
            width: 90%; height: 46px; margin: 0 auto 3px;
            background: transparent; border: 1px solid transparent;
            color: #94A3B8; text-align: left; padding: 0 16px;
            border-radius: 10px; font-size: 0.92rem;
            font-family: 'Inter', sans-serif; font-weight: 500;
            display: flex; align-items: center; justify-content: flex-start;
            transition: all 0.2s ease;
        }
        [data-testid="stSidebar"] button[data-testid="baseButton-secondary"]:hover {
            background: rgba(255,255,255,0.04); color: #F8FAFC;
        }
        /* Sidebar buttons - active */
        [data-testid="stSidebar"] button[data-testid="baseButton-primary"] {
            width: 90%; height: 46px; margin: 0 auto 3px;
            background: linear-gradient(90deg, rgba(99,102,241,0.15), rgba(56,189,248,0.1));
            border: 1px solid rgba(99,102,241,0.3);
            color: #818cf8; text-align: left; padding: 0 16px;
            border-radius: 10px; font-size: 0.92rem;
            font-family: 'Inter', sans-serif; font-weight: 600;
            display: flex; align-items: center; justify-content: flex-start;
        }

        /* === GLASS PANELS === */
        .glass-panel,
        div[data-testid="stForm"],
        div[data-testid="stVerticalBlockBorderWrapper"] {
            background: rgba(15, 20, 40, 0.45) !important;
            backdrop-filter: blur(20px) !important;
            -webkit-backdrop-filter: blur(20px) !important;
            border: 1px solid rgba(255,255,255,0.06) !important;
            border-radius: 16px !important;
            padding: 1.75rem !important;
            box-shadow: 0 8px 32px rgba(0,0,0,0.35), inset 0 1px 0 rgba(255,255,255,0.04) !important;
        }

        /* === INPUTS === */
        .stTextInput > div > div > input,
        .stTextArea > div > textarea,
        .stSelectbox > div > div > div,
        .stNumberInput > div > div > input {
            background-color: rgba(0,0,0,0.25) !important;
            color: #F8FAFC !important;
            border: 1px solid rgba(255,255,255,0.1) !important;
            border-radius: 10px !important;
            font-size: 0.94rem !important;
            box-shadow: inset 0 2px 4px rgba(0,0,0,0.15) !important;
        }
        .stTextArea > div > textarea { padding: 14px !important; line-height: 1.6 !important; }
        .stSelectbox label, .stTextInput label, .stTextArea label, .stNumberInput label {
            color: #CBD5E1 !important; font-weight: 500 !important; font-size: 0.88rem !important;
        }
        .stTextInput > div > div > input:focus,
        .stTextArea > div > textarea:focus {
            border-color: #818cf8 !important;
            box-shadow: 0 0 0 1px #818cf8, inset 0 2px 4px rgba(0,0,0,0.15) !important;
        }

        /* === BUTTONS === */
        div[data-testid="stForm"] button[kind="primary"],
        .stButton > button[kind="primary"] {
            background: linear-gradient(135deg, #4f46e5 0%, #0ea5e9 100%) !important;
            border: none !important; border-radius: 10px !important; height: 46px !important;
            color: white !important; font-family: 'Outfit', sans-serif !important;
            font-weight: 600 !important;
            box-shadow: 0 4px 14px rgba(99,102,241,0.3), inset 0 1px 0 rgba(255,255,255,0.2) !important;
            transition: all 0.2s ease !important;
        }
        div[data-testid="stForm"] button[kind="primary"]:hover,
        .stButton > button[kind="primary"]:hover {
            transform: translateY(-2px) !important;
            box-shadow: 0 6px 20px rgba(99,102,241,0.45), inset 0 1px 0 rgba(255,255,255,0.2) !important;
        }
        div[data-testid="stForm"] button[kind="secondary"],
        .stButton > button[kind="secondary"] {
            background: rgba(255,255,255,0.04) !important;
            border: 1px solid rgba(255,255,255,0.1) !important;
            border-radius: 10px !important; height: 46px !important;
            color: #E2E8F0 !important; font-family: 'Outfit', sans-serif !important;
            transition: all 0.2s ease !important;
        }
        div[data-testid="stForm"] button[kind="secondary"]:hover,
        .stButton > button[kind="secondary"]:hover {
            background: rgba(255,255,255,0.07) !important;
            border-color: rgba(255,255,255,0.18) !important;
        }

        /* === CHAT === */
        [data-testid="stChatMessage"] {
            background: transparent !important;
            border: none !important; padding: 1rem 1.25rem !important;
            border-top: 1px solid rgba(255,255,255,0.03) !important;
            box-shadow: none !important;
        }
        [data-testid="stChatInput"] {
            background: rgba(5,8,22,0.88) !important;
            backdrop-filter: blur(20px) !important;
            border: 1px solid rgba(255,255,255,0.08) !important;
            border-radius: 16px !important;
            box-shadow: 0 -8px 30px rgba(0,0,0,0.4) !important;
        }
        [data-testid="stChatInput"] textarea { color: white !important; }

        /* === DASHBOARD CARDS === */
        .premium-card {
            background: rgba(15,20,45,0.55);
            backdrop-filter: blur(16px);
            border: 1px solid rgba(255,255,255,0.06);
            border-radius: 18px; padding: 1.5rem;
            position: relative; min-height: 220px;
            display: flex; flex-direction: column;
            box-shadow: 0 4px 24px rgba(0,0,0,0.25), inset 0 1px 0 rgba(255,255,255,0.03);
            transition: all 0.25s ease; cursor: pointer;
        }
        div[data-testid="column"]:hover .premium-card {
            background: rgba(25,32,65,0.75);
            border-color: rgba(255,255,255,0.12);
            box-shadow: 0 12px 40px rgba(0,0,0,0.4), inset 0 1px 0 rgba(255,255,255,0.06);
            transform: translateY(-3px);
        }
        .card-icon-container {
            width: 46px; height: 46px; border-radius: 12px;
            display: flex; align-items: center; justify-content: center;
            font-size: 1.4rem; margin-bottom: 14px;
        }
        .premium-card h3 { color: #FFFFFF; font-size: 1.05rem; font-weight: 700; margin-bottom: 6px; }
        .premium-card p { color: #94A3B8; font-size: 0.88rem; line-height: 1.5; flex-grow: 1; margin: 0; }

        /* Card overlay button */
        .card-button-wrapper {
            position: absolute; top: 0; left: 0; right: 0; bottom: 0;
            opacity: 0; z-index: 10;
        }
        .card-button-wrapper button { width: 100% !important; height: 100% !important; padding: 0 !important; }

        /* Card icon gradients */
        .theme-indigo-violet .card-icon-container { background: linear-gradient(135deg, #4f46e5, #7c3aed); }
        .theme-violet-magenta .card-icon-container { background: linear-gradient(135deg, #8b5cf6, #d946ef); }
        .theme-cyan-blue .card-icon-container { background: linear-gradient(135deg, #0ea5e9, #3b82f6); }
        .theme-emerald-teal-tut .card-icon-container { background: linear-gradient(135deg, #34d399, #0d9488); }
        .theme-amber-coral .card-icon-container { background: linear-gradient(135deg, #f59e0b, #f43f5e); }
        .theme-magenta-purple .card-icon-container { background: linear-gradient(135deg, #db2777, #9333ea); }
        .theme-indigo-purple .card-icon-container { background: linear-gradient(135deg, #6366f1, #a855f7); }
        .theme-teal-cyan .card-icon-container { background: linear-gradient(135deg, #14b8a6, #06b6d4); }
        .theme-violet-blue .card-icon-container { background: linear-gradient(135deg, #8b5cf6, #2563eb); }
        .theme-emerald-teal .card-icon-container { background: linear-gradient(135deg, #10b981, #14b8a6); }

        /* === PAGE HEADERS === */
        .page-header {
            display: flex; align-items: center; gap: 14px;
            margin: 1.5rem 0 0.5rem;
        }
        .page-header-icon {
            font-size: 1.8rem;
            background: rgba(255,255,255,0.05);
            border: 1px solid rgba(255,255,255,0.08);
            border-radius: 12px; padding: 10px;
            display: flex; align-items: center; justify-content: center;
        }
        .page-header-title { margin: 0; font-size: 2rem; font-weight: 800; color: #F8FAFC; }
        .page-subtitle { color: #94A3B8; font-size: 1rem; margin-bottom: 1.75rem; }
    </style>
    """, unsafe_allow_html=True)


def render_page_header(icon: str, title: str, subtitle: str):
    """Standardized page header used by all feature pages."""
    render_back_button()
    st.markdown(f"""
    <div class="page-header">
        <div class="page-header-icon">{icon}</div>
        <h1 class="page-header-title">{title}</h1>
    </div>
    <p class="page-subtitle">{subtitle}</p>
    """, unsafe_allow_html=True)


def render_back_button():
    """Back to Dashboard button."""
    page_key = st.session_state.get("page", "Dashboard")
    if st.button("⬅ Back to Dashboard", key=f"back_{page_key}"):
        st.session_state.page = "Dashboard"
        st.rerun()


def render_separator():
    """Subtle section divider."""
    st.markdown(
        '<div style="height:1px;background:linear-gradient(90deg,transparent,rgba(255,255,255,0.06) 50%,transparent);margin:24px 0;"></div>',
        unsafe_allow_html=True
    )