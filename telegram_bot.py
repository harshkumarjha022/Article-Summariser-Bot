# import os
# import requests
# from bs4 import BeautifulSoup
# import google.generativeai as genai
# from telebot import TeleBot
# from dotenv import load_dotenv
# import pandas as pd

# # Load environment variables
# load_dotenv()

# # Set up API keys
# TELEGRAM_API_KEY = os.getenv("TELEGRAM_API_KEY") or "YOUR_TELEGRAM_API_KEY"
# GEMINI_API_KEY = os.getenv("GEMINI_API_KEY") or "YOUR_GEMINI_API_KEY"

# # Configure Gemini API
# genai.configure(api_key=GEMINI_API_KEY)

# # Initialize the Telegram bot
# bot = TeleBot(TELEGRAM_API_KEY)

# # Scraping function
# def scrape_articles(url):
#     try:
#         response = requests.get(url)
#         response.raise_for_status()
#         soup = BeautifulSoup(response.text, 'html.parser')
#         paragraphs = [p.get_text(strip=True) for p in soup.find_all('p')]
#         return "\n".join(paragraphs)
#     except Exception as e:
#         return f"Error scraping URL {url}: {e}"

# # Summarization function using Gemini API
# def summarize_text(content, max_sentences=3):
#     try:
#         model = genai.GenerativeModel(model_name="gemini-1.5-flash")
#         prompt = f"Summarize the given text in {max_sentences} sentences."
#         response = model.generate_content([prompt, content])
#         return response.text if response else "No summary generated."
#     except Exception as e:
#         return f"Error during summarization: {e}"

# # Save data to CSV
# def save_to_csv(data, filename="data.csv"):
#     df = pd.DataFrame(data)
#     df.to_csv(filename, index=False)
#     return f"Data saved to {filename}"

# # Bot command handlers
# @bot.message_handler(commands=['start'])
# def greet_user(message):
#     bot.reply_to(message, "Welcome to the Summary Bot! Use /summary <URL> to get a summary of an article.")

# @bot.message_handler(commands=['summary'])
# def send_summary(message):
#     try:
#         # Extract URL from the user's message
#         url = message.text.split(" ", 1)[1].strip()
#         bot.send_message(message.chat.id, "Scraping and summarizing the content, please wait...")
        
#         # Scrape content
#         content = scrape_articles(url)
#         if "Error" in content:
#             bot.send_message(message.chat.id, content)
#             return
        
#         # Summarize content
#         summary = summarize_text(content)
#         bot.send_message(message.chat.id, summary)
#     except IndexError:
#         bot.send_message(message.chat.id, "Please provide a URL. Usage: /summary <URL>")
#     except Exception as e:
#         bot.send_message(message.chat.id, f"An error occurred: {e}")

# # Start the bot
# def start_bot():
#     print("Starting Telegram Bot...")
#     bot.polling()

# # Run the bot
# if __name__ == "__main__":
#     start_bot()


# from telebot import TeleBot
# import os

# TELEGRAM_API_KEY = os.getenv("TELEGRAM_API_KEY") or "YOUR_TELEGRAM_API_KEY"
# bot = TeleBot(TELEGRAM_API_KEY)

# # Clear pending updates to avoid conflicts
# bot.get_updates(offset=-1)

# @bot.message_handler(commands=['start'])
# def greet_user(message):
#     bot.reply_to(message, "Welcome to the bot!")

# if __name__ == "__main__":
#     bot.polling()
    


















import os
import requests
from bs4 import BeautifulSoup
import google.generativeai as genai
from telebot import TeleBot
from dotenv import load_dotenv
import pandas as pd

# Load environment variables
load_dotenv()

# Set up API keys
TELEGRAM_API_KEY = os.getenv("TELEGRAM_API_KEY") or "YOUR_TELEGRAM_API_KEY"

bot = TeleBot(TELEGRAM_API_KEY)
bot.get_updates(offset=-1)



# Start the bot
def start_bot(summary):
    # bot.polling()
    print("Starting Telegram Bot...")
    print(summary)
    try:
        bot.send_message("927617217", summary)
    except IndexError:
        bot.send_message("927617217", "Please provide a URL. Usage: /summary <URL>")
    except Exception as e:
        bot.send_message("927617217", f"An error occurred: {e}")

# Run the bot
# if __name__ == "__main__":
#     bot.polling()
#     start_bot()
