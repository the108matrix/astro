import streamlit as st
import re

# Page configuration
st.set_page_config(page_title='Phishing Email Detector', page_icon='📧')
st.title('📧 Phishing Email Detector')

# Custom CSS
st.markdown("""
<style>
    html, body, [class*="css"] {
        font-family: 'Arial', sans-serif;
    }
    .big-font {
        font-size:30px !important;
        font-weight: bold;
        color: #28527a;
    }
    .footer {
        width: 100%;
        color: #fff;
        text-align: left;
        padding: 10px;
    }
    .stButton>button {
        width: 100%;
        border-radius: 20px;
        background-color: #49a942;  /* Changed for visibility */
        color: white;
        border: none;
        height: 50px;
        font-size: 16px;
        padding: 10px;
    }
    .stButton>button:hover {
        background-color: #28527a;  /* Dark blue for hover effect */
        color: #fff;
        transform: translateY(-3px);
    }
    .stTextArea>div>div>textarea {
        width: 680px; /* Fixed width */
        height: 300px; /* Fixed height */
        padding: 15px;
        border-radius: 15px;
        border: 2px solid #49a942;  /* Changed for consistency */
        font-size: 16px;
        transition: border-color .3s, box-shadow .3s;
        resize: none; /* Disables resizing */
    }
    .stTextArea>div>div>textarea:focus {
        border-color: #28527a;
        box-shadow: 0 0 0 2px rgba(40,82,122,.2);
    }
    .result-container {
        margin-top: 20px;  /* Added margin top for spacing */
        margin-bottom: 20px;  /* Added margin bottom for spacing */
    }
</style>
""", unsafe_allow_html=True)

st.markdown("""
This tool helps you detect potential phishing emails by analyzing the text you provide.
            
**Instructions:** Paste the content of an email below, and press the "Analyze Email" button to see if it might be a phishing attempt.
""")

col1, col2 = st.columns([3, 1])
with col1:
    email_content = st.text_area(
        "", height=300, placeholder="Paste email content here...", key="email_textarea")
with col2:
    st.write("")  # Adds vertical space
    analyze_button = st.button(
        'Analyze Email', help="Click to analyze the pasted email content.")

# Phishing detection function


def detect_phishing(email):
    phishing_words = ['urgent', 'immediate action required', 'verify your account', 'confirm your identity',
                      'password', 'update', 'alert', 'secure', 'link', 'error', 'suspended account',
                      'unusual activity', 'login attempt', 'validate', 'credentials', 'security alert']
    patterns = [r'https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+', r'\bDear\s+Customer\b', r'\bClick\s+here\b',
                r'\bwithin\s+24\s+hours\b', r'\bfailure\s+to\b', r'\bplease\b', r'\baccount\b']
    score = 0
    for word in phishing_words:
        if word in email.lower():
            score += 1
    for pattern in patterns:
        if re.search(pattern, email, re.IGNORECASE):
            score += 1
    max_score = len(phishing_words) + len(patterns)
    risk_level = 'Low'
    if score > max_score * 0.3:
        risk_level = 'Medium'
    if score > max_score * 0.6:
        risk_level = 'High'
    return risk_level


# Result display logic
if analyze_button and email_content:
    risk_level = detect_phishing(email_content)
    result_color = "#FFCCCC" if risk_level == "High" else "#FFDD99" if risk_level == "Medium" else "#CCFFCC"
    st.markdown(f"<div class='result-container' style='background-color: {result_color}; padding: 10px; border-radius: 10px; font-size: 18px; color: black;'>"
                f"🛡️ <strong style='color: black;'>{risk_level} Risk:</strong> The email has a {risk_level.lower()} risk of being a phishing attempt.</div>", unsafe_allow_html=True)
    st.markdown('---')  # Optional: add a divider for clarity
    with st.expander("Learn more about phishing indicators 📚"):
        st.markdown("""
        **Phishing Indicators:**
        - **Urgency:** Phishing attempts often create a sense of urgency to provoke quick action. 🚨
        - **Suspicious Links:** Hover over links to see if the URL address looks legitimate. 🔗
        - **Generic Salutations:** Phishing emails often use generic names like 'Dear Customer.' 🙍‍♂️
        - **Spelling/Grammar:** Poor spelling or grammar can be a sign of phishing. 📝
        - **Request for Information:** Any unsolicited request for personal or financial information should be considered suspicious. ❓
        """)
elif analyze_button:
    st.error("Please paste some email content to analyze. ❌")

# Footer
st.markdown(
    """
    <footer class="footer">
        <small>
            © Akilesh Jayakumar | Created with Python and Streamlit
        </small>
    </footer>
    """, unsafe_allow_html=True
)
