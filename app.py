import streamlit as st

# 1. Page Configuration
st.set_page_config(
    page_title="Dashboard",
    page_icon="⚖️",
    layout="wide"
)

# 2. Updated Styling: Lighter Background & Professional Accents
# 2. Updated Styling
st.markdown("""
    <style>
    /* Main background color */
    .stApp {
        background-color: #F0F2F6;
    }
    
    /* Sidebar styling */
    [data-testid="stSidebar"] {
        background-color: #1F3864;
    }
    
    /* 1. Target all general text, labels, and subheaders in sidebar */
    [data-testid="stSidebar"] .stText, 
    [data-testid="stSidebar"] label, 
    [data-testid="stSidebar"] p, 
    [data-testid="stSidebar"] h1, 
    [data-testid="stSidebar"] h2, 
    [data-testid="stSidebar"] h3,
    [data-testid="stSidebar"] .stMarkdown {
        color: white !important;
    }

    /* 2. Target the specific radio button text labels */
    [data-testid="stSidebar"] div[role="radiogroup"] label p {
        color: white !important;
    }

    /* Titles and Headers in Main Body */
    h1 {
        color: #1F3864;
        font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
        font-weight: 700;
    }

    /* Keep your existing radio button box styling but ensure text is white */
    div.row-widget.stRadio > div {
        background-color: #2D4A7D;
        padding: 10px;
        border-radius: 10px;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. Sidebar Navigation
st.sidebar.title("FinRecon Gateway")
st.sidebar.markdown("---")

# The selector for your two scripts
page = st.sidebar.radio(
    "Select Operation Mode:",
    ["Razorpay Portal", "Cashfree Portal"],
    index=0
)

st.sidebar.markdown("---")
st.sidebar.caption("Current Session: Active")

# 4. Main Content Area Logic
if page == "Razorpay Portal":
    st.markdown("<h1>🛡️ Razorpay x Shopify </h1>", unsafe_allow_html=True)
    try:
        with open("app.py", encoding="utf-8") as f:
            code = f.read()
            exec(code)
    except FileNotFoundError:
        st.error("Missing File: 'app.py' not found.")

elif page == "Cashfree Portal":
    st.markdown("<h1>📊 Cashfree x Shopify</h1>", unsafe_allow_html=True)
    try:
        with open("cashfree.py", encoding="utf-8") as f:
            code = f.read()
            exec(code)
    except FileNotFoundError:
        st.error("Missing File: 'cashfree.py' not found.")
