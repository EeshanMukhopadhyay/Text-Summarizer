import tkinter as tk
from tkinter import scrolledtext, messagebox
from newspaper import Article
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer
from PIL import Image, ImageTk # Added for image

# === Summarizer functions ===
def summarize_text(text, sentence_count=3):
    parser = PlaintextParser.from_string(text, Tokenizer("english"))
    summarizer = LsaSummarizer()
    summary = summarizer(parser.document, sentence_count)
    return ' '.join(str(sentence) for sentence in summary)

def summarize_article_from_url(url, sentence_count=3):
    article = Article(url)
    article.download()
    article.parse()
    return summarize_text(article.text, sentence_count)

def summarize():
    if input_mode.get() == "url":
        url = url_entry.get()
        if not url.strip():
            messagebox.showwarning("Input Needed", "Please enter a URL.")
            return
        try:
            summary = summarize_article_from_url(url)
            output_text.delete(1.0, tk.END)
            output_text.insert(tk.END, summary)
        except Exception as e:
            messagebox.showerror("Error", str(e))
    else:
        text = custom_text.get("1.0", tk.END).strip()
        if not text:
            messagebox.showwarning("Input Needed", "Please paste or type your text.")
            return
        summary = summarize_text(text)
        output_text.delete(1.0, tk.END)
        output_text.insert(tk.END, summary)

# === GUI Setup ===
root = tk.Tk()
root.title("📰 Text Summarizer")
root.geometry("750x650")
root.configure(bg = "white")  

input_mode = tk.StringVar(value="url")

# === Styles ===
label_font = ("Helvetica", 12, "bold")
section_bg = "#e0f7fa"
entry_bg = "#ffffff"
button_bg = "#26a69a"
button_fg = "#ffffff"
highlight_color = "#00796b"

# === Input method selection ===
tk.Label(root, text="Choose Input Method:", font=label_font, bg="#f0f4f8", fg=highlight_color).pack(anchor="w", padx=15, pady=(15, 5))
tk.Radiobutton(root, text="Summarize from URL", variable=input_mode, value="url", bg="#f0f4f8", fg="#333", font=("Helvetica", 11)).pack(anchor="w", padx=30)
tk.Radiobutton(root, text="Paste your own text", variable=input_mode, value="text", bg="#f0f4f8", fg="#333", font=("Helvetica", 11)).pack(anchor="w", padx=30)

# === URL input ===
tk.Label(root, text="Enter URL:", font=("Helvetica", 11), bg="#f0f4f8", fg="#000").pack(anchor="w", padx=15, pady=(15, 0))
url_entry = tk.Entry(root, width=80, bg="#fffde7", font=("Helvetica", 10))
url_entry.pack(padx=15, pady=5)

# === Custom text input ===
tk.Label(root, text="Paste your text below:", font=("Helvetica", 11), bg="#f0f4f8", fg="#000").pack(anchor="w", padx=15, pady=(15, 0))
custom_text = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=100, height=10, bg="#fffde7", font=("Helvetica", 10))
custom_text.pack(padx=15, pady=5)

# === Summarize button ===
tk.Button(root, text="Summarize", command=summarize,
          bg=button_bg, fg=button_fg, font=("Helvetica", 12, "bold"), padx=10, pady=5).pack(pady=15)

# === Summary output ===
tk.Label(root, text="Summary Output:", font=("Helvetica", 11), bg="#f0f4f8", fg="#000").pack(anchor="w", padx=15)
output_text = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=100, height=10, bg="#e8f5e9", font=("Helvetica", 10))
output_text.pack(padx=15, pady=5)

# === Image ===
# Load image 
image = Image.open("text-analysis-tools_new.jpg")  
image = image.resize((200, 100)) 
photo = ImageTk.PhotoImage(image)

# Placing it in the GUI
img_label = tk.Label(root, image=photo, bg="white")
img_label.image = photo  # Keep a reference to avoid garbage collection
img_label.pack(pady=10)

# Run app
root.mainloop()
