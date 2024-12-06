# import streamlit as st
# from scraper import scrape_articles
# from summarizer import summarize_text
# from telegram_bot import start_bot

# st.title("Automated Content Management System")
# st.sidebar.header("Navigation")
# # option = st.sidebar.selectbox("Choose a task", ["Scrape & Summarize", "Run Telegram Bot"])
# option = st.sidebar.selectbox("Choose a task", ["Scrape & Summarize"])

# if option == "Scrape & Summarize":
#     url = st.text_input("Enter the article URL:")
#     if st.button("Scrape and Summarize"):
#         raw_text = scrape_articles(url)
#         if raw_text:
#             summary = summarize_text(raw_text)
#             st.text_area("Generated Summary", summary)
#             print(summary)
#             start_bot(summary) 
#         else:
#             st.error("Failed to scrape or process the URL.")

# # elif option == "Run Telegram Bot":



import streamlit as st
from scraper import scrape_articles
from summarizer import summarize_text
from telegram_bot import start_bot

# Set page configuration for better appearance
st.set_page_config(
    page_title="Automated Content Management System",
    page_icon="📚",
    layout="wide",
)

# Apply some custom CSS for styling
st.markdown(
    """
    <style>
    .main-title {
        font-size: 2.5rem;
        color: #2e86c1;
        text-align: center;
        font-weight: bold;
        margin-bottom: 20px;
    }
    .sidebar .sidebar-content {
        background-color: #f8f9fa;
        padding: 10px;
    }
    .stTextInput>div>input {
        border: 1px solid #2e86c1;
        border-radius: 5px;
        padding: 10px;
    }
    .stButton>button {
        color: white;
        background: #2e86c1;
        border: none;
        padding: 10px 20px;
        border-radius: 5px;
    }
    .stButton>button:hover {
        background: #21618c;
    }
    .stTextArea textarea {
        border: 1px solid #2e86c1;
        border-radius: 5px;
        padding: 10px;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Main title
st.markdown('<div class="main-title">Automated Content Management System 📚</div>', unsafe_allow_html=True)

# Sidebar for navigation
st.sidebar.header("🛠️ Navigation")
option = st.sidebar.selectbox("Choose a task", ["Scrape & Summarize"])

if option == "Scrape & Summarize":
    st.header("Scrape & Summarize Articles ✍️")
    st.write("Provide an article URL, and the system will scrape and summarize it for you.")
    
    # Input for URL
    url = st.text_input("🔗 Enter the article URL:")
    
    # Button to trigger scraping and summarization
    if st.button("🚀 Scrape and Summarize"):
        with st.spinner("Processing... Please wait!"):
            raw_text = scrape_articles(url)
            if raw_text:
                summary = summarize_text(raw_text)
                
                # Display summary
                st.success("Summary generated successfully!")
                st.text_area("📝 Generated Summary", summary, height=200)
                
                # Print summary for debugging/logging
                print(summary)
                
                # Send the summary via Telegram bot
                start_bot(summary)
                st.info("Summary sent to Telegram successfully!")
            else:
                st.error("Failed to scrape or process the URL. Please check the URL and try again.")
