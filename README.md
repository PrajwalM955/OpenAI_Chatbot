# 🤖 OpenAI Chatbot with Personality & API Key Rotation  

![Python](https://img.shields.io/badge/Python-3.9%2B-blue?logo=python)  
![Dependencies](https://img.shields.io/badge/Requirements-up%20to%20date-brightgreen)  
![License](https://img.shields.io/badge/License-MIT-yellow.svg)  
![Stars](https://img.shields.io/github/stars/PrajwalM955/OpenAI_Chatbot?style=social)  
![Forks](https://img.shields.io/github/forks/PrajwalM955/OpenAI_Chatbot?style=social)  

A simple **Python-based chatbot** leveraging the **OpenAI API** with key features like **API key rotation**, **lightweight multi-model support**, and secure **.env integration**.  

This project demonstrates building a chatbot that engages users with a witty, quirky personality — perfect for **portfolios** and **demos**.  

---

## 📌 Overview  

This project showcases how to create a chatbot using Python and the OpenAI API, focusing on:  

- 🔄 **API key rotation** to handle quota limits seamlessly  
- 🧠 **Multiple model support** including lightweight options for demo purposes  
- 🔐 **Secure management** of API keys via `.env`  
- ⚡ **Error handling** for rate and quota limiting  
- 🤖 **Engaging personality** with casual emojis, jokes, and fun responses  
- 💻 **Lightweight, terminal-based interface** for straightforward interaction  
- 🛠️ **Offline demo mode** with canned witty responses (usable without API keys)  

---

## 🚀 Features  

✅ Chat with models like `gpt-3.5-turbo`, `gpt-5-mini`, and `gpt-5-nano`  
✅ Automatically rotate through multiple API keys when limits are hit  
✅ Securely store keys in environment variables (`.env`)  
✅ CLI chatbot interface that runs directly in your terminal  
✅ Demo mode with quirky, emoji-rich conversation (no API key needed)  

---

## 🛠️ Setup Instructions  

### 1️⃣ Clone this repo  

```bash
git clone https://github.com/PrajwalM955/OpenAI_Chatbot.git
cd OpenAI_Chatbot
2️⃣ Create & activate a virtual environment
bash
Copy
Edit
python -m venv .venv

# Windows
.\.venv\Scripts\activate

# macOS/Linux
source .venv/bin/activate
3️⃣ Install dependencies
bash
Copy
Edit
pip install -r requirements.txt
4️⃣ Create a .env file with your OpenAI API keys
text
Copy
Edit
OPENAI_API_KEY=your_main_key
OPENAI_API_KEY_1=your_backup_key
# Add more keys as needed (e.g., OPENAI_API_KEY_2 to OPENAI_API_KEY_7)
🗨️ Usage
🔹 Live Chatbot Mode (Using OpenAI API)
bash
Copy
Edit
python main.py
👉 Start chatting in your terminal.
The bot maintains its quirky personality, supports multiple API keys with automatic rotation, and handles errors gracefully.

🔹 Demo Mode (Offline, No API Key Needed)
bash
Copy
Edit
python demo_chatbot.py
👉 Enjoy witty and emoji-rich canned responses from mock_responses.json.
Perfect for demos and presentations without consuming API quotas.

🎨 Customize the Personality
Want to personalize the bot’s demo mode?
📝 Edit mock_responses.json and add your own witty phrases, jokes, and emoji combos to shape the bot’s unique voice.

📸 Demo Screenshot


🤝 Contributing
Got ideas to enhance the chatbot’s personality, add features, or improve error handling?
We’d love your input!

Open an issue 💡

Submit a pull request 🚀

📜 License
This project is licensed under the MIT License.