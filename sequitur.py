import streamlit as st
from datetime import datetime

# Page config
st.set_page_config(
    page_title="Documentation & Updates",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for styling
st.markdown("""
    <style>
        .main {
            background-color: white;
        }
        .stButton button {
            background-color: #E6F3FF;
            color: black;
        }
        .notification-box {
            background-color: #E6F3FF;
            padding: 20px;
            border-radius: 5px;
            margin-bottom: 20px;
        }
        .content-section {
            background-color: white;
            padding: 20px;
            border-radius: 5px;
            margin-bottom: 20px;
        }
    </style>
""", unsafe_allow_html=True)

# Sample data - Replace with your actual content
NOTIFICATIONS = [
    {
        "date": "2024-03-19",
        "content": "New documentation updates available in the manual section"
    },
    {
        "date": "2024-03-12",
        "content": "System maintenance scheduled for next week"
    }
]

FAQ_DATA = {
    "How do I reset my password?": "Instructions for password reset...",
    "Where can I find the latest updates?": "Check the notifications section...",
    "What are the system requirements?": "Minimum system requirements include..."
}

MANUAL_SECTIONS = {
    "Getting Started": "Step by step guide to get started...",
    "Advanced Features": "Detailed explanation of advanced features...",
    "Troubleshooting": "Common issues and their solutions..."
}

ARTICLES = [
    {
        "title": "New Features Released",
        "date": "2024-03-15",
        "content": "Detailed article about new features..."
    },
    {
        "title": "Best Practices Guide",
        "date": "2024-03-10",
        "content": "Article about best practices..."
    }
]

def main():
    # Sidebar for navigation
    st.sidebar.title("Navigation")
    section = st.sidebar.radio(
        "Go to",
        ["Section 1: Documentation", "Section 2: Updates & News"]
    )

    # Main content area
    if section == "Section 1: Documentation":
        st.title("Documentation")

        # FAQ Section
        with st.expander("FAQ", expanded=True):
            for question, answer in FAQ_DATA.items():
                st.subheader(question)
                st.write(answer)
                st.divider()

        # Manual Section
        with st.expander("Manual", expanded=False):
            for section_title, content in MANUAL_SECTIONS.items():
                st.subheader(section_title)
                st.write(content)
                st.divider()

    else:  # Section 2: Updates & News
        st.title("Updates & News")

        # Notifications
        st.subheader("📢 Latest Notifications")
        for notification in NOTIFICATIONS:
            with st.container():
                st.markdown(f"""
                    <div class="notification-box">
                        <strong>{notification['date']}</strong><br>
                        {notification['content']}
                    </div>
                """, unsafe_allow_html=True)

        # Articles and News
        st.subheader("📰 Articles & News")
        for article in ARTICLES:
            with st.expander(f"{article['title']} - {article['date']}"):
                st.write(article['content'])

if __name__ == "__main__":
    main()
