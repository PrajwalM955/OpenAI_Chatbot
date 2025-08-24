# 🤖 OpenAI Chatbot  

A simple Python-based chatbot using OpenAI API with **API key rotation**, **lightweight model switching**, and secure **.env integration** for portfolio/demo purposes.  

---

## 📌 Overview  

This project demonstrates how to build a chatbot with **Python** and the **OpenAI API**, focusing on:  
- 🔄 **API key rotation** (handles quota limits automatically)  
- 🧠 **Multiple model support** (lightweight models for demo purposes)  
- 🔐 **Secure environment variables** using `.env` (API keys are never exposed)  
- ⚡ **Error handling** for quota/rate limits  

---

## 🚀 Features  

- Chat with different OpenAI models:  
  `gpt-3.5-turbo`, `gpt-5-mini`, `gpt-5-nano`  
- Automatically rotates API keys when quota is reached  
- Uses `.env` to securely store API keys  
- CLI-based chatbot (runs in terminal)  

---

## 🛠️ Setup Instructions  

1. Clone this repo:  
   ```bash
   git clone https://github.com/PrajwalM955/OpenAI_Chatbot.git
   cd OpenAI_Chatbot
