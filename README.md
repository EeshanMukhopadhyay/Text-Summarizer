# Text-Summarizer

A Python-based GUI application that allows you to **summarize text** or **articles from URLs** using Natural Language Processing (NLP) techniques. The app uses the **Sumy** library with **LSA (Latent Semantic Analysis)** summarization and features a simple interface built with **Tkinter**.

![App Screenshot](text-analysis-tools_new.jpg)

---

## 🚀 Features

- 🔗 Summarize news/articles directly from a **URL**
- ✍️ Summarize **custom pasted text**
- 📜 Clean, scrollable input/output sections
- 🖼️ Displays a custom image in the GUI
- ✅ Error handling and user-friendly warnings
- 🪄 Built with Sumy’s LSA summarization algorithm

---

## 🧰 Technologies Used

- Python 3
- Tkinter (GUI)
- Sumy (NLP Summarization)
- Newspaper3k (for extracting article content from URLs)
- Pillow (for image handling)

---

## 📦 Installation

Make sure you have Python 3 installed. Then, install the required Python libraries:

pip install tkinter
pip install newspaper3k
pip install sumy
pip install pillow

##▶️ How to Run

After installing dependencies, simply run:

python text_summarizer.py

**📌 Usage**

1. Choose the input method:

   .Summarize from URL
   .Paste your own text

2. Enter the URL or paste your content.

3.Click "Summarize".

4.View the output in the summary box.


**❗ Troubleshooting**

If you encounter nltk or newspaper3k errors, try running:

import nltk
nltk.download('punkt')

Make sure your system is connected to the internet when using the URL option (to fetch and parse the article).

**Connect**

Feel free to connect or raise issues:

GitHub: EeshanMukhopadhyay
