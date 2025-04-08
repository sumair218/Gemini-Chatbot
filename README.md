# 💬 Gemini AI Chatbot

![Gemini Chatbot Banner](https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExdGZ1cXNvZm1yZ25ndTBjN3Zmejl3NnNmOXRxYzV1MXZsdm1vOWM2ZSZlcD12MV9naWZzX3NlYXJjaCZjdD1n/TilmLMmWrRYYHjLfub/giphy.gif)

> 🌟 An intelligent, real-time conversational AI chatbot powered by Google Gemini API, crafted using HTML, CSS, JavaScript, and Flask!

---

## 🚀 Features

- ⚡ **Real-Time Chat Interface** – Instant responses to your queries.
- 🧠 **Gemini API Integration** – High-performance and context-aware replies.
- 🎨 **Modern & Responsive UI** – Clean design with full responsiveness.
- 🌙 **Dark Mode Ready** – Chat stylishly any time of the day.
- 🔐 **Secure Flask Backend** – Handles API communication & routing safely.
- 🛠️ **Easy to Customize** – Plug and play your own styles or extend features.

---

## 📸 Demo Preview

![Gemini Chat Demo](https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExZHR1eW53OHF4Z2Z0aW9rbjY4amFqZ3dnazN1ejlhczVxc2w2bGU3MiZlcD12MV9naWZzX3NlYXJjaCZjdD1n/5xtDarzqClzZ2fLgvPq/giphy.gif)


---

## 🧩 Tech Stack

- **Frontend:** HTML5, CSS3, JavaScript (Vanilla)
- **Backend:** Python 3, Flask
- **AI Engine:** [Gemini API](https://ai.google.dev/)
- **Extras:** Fetch API, JSON, Jinja2 templating

---

## 📂 Project Structure

```
gemini-chatbot/
│
├── static/
│   ├── css/
│   │   └── style.css
│   ├── js/
│   │   └── script.js
│
├── templates/
│   └── index.html
│
├── app.py
├── requirements.txt
└── README.md
```

---

## ⚙️ Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/gemini-chatbot.git
cd gemini-chatbot
```

### 2. Create a Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Required Packages
```bash
pip install -r requirements.txt
```

### 4. Add Your Gemini API Key
In `app.py`, replace `'your_gemini_api_key_here'` with your actual Gemini API key.

```python
api_key = "your_gemini_api_key_here"
```

### 5. Run the Flask App
```bash
python app.py
```

Then open `http://127.0.0.1:5000` in your browser and start chatting!

---

## 💡 How It Works

1. ✍️ User types a message in the chat box.
2. 📡 The frontend sends the message to the Flask backend.
3. 🔐 Flask uses the Gemini API to process and get a response.
4. 💬 The chatbot responds intelligently in real-time.

---

## 🌈 Customization Ideas

- Add user authentication (Flask-Login)
- Enable speech-to-text with Web Speech API
- Store chat history with SQLite/PostgreSQL
- Add animated avatars or typing indicators

---

## 📦 Dependencies

- Flask
- requests
- dotenv (optional)
- HTML/CSS/JS (no external framework dependencies)

Install with:

```bash
pip install flask requests python-dotenv
```

---

## 🤝 Contributing

Pull requests are welcome! For major changes, please open an issue first.  
Make sure to follow best practices and clean code conventions.

---

## 📃 License

This project is licensed under the **MIT License**. Feel free to use, modify, and share!

---

## 👨‍💻 Developed by

**Sumair Irshad**  
📧 sumairirshad52@gmail.com  
🌐 [LinkedIn](https://www.linkedin.com/in/sumair-irshad) | [GitHub](https://github.com/sumair218/Sumair218)

---

> ⭐ If you found this project useful, don't forget to star the repo and share it with others!
