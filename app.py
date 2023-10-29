import tkinter as tk
from tkinter import ttk
from googletrans import Translator

class LanguageTranslatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Dil Çevirici Uygulaması")

        self.translator = Translator()
        self.languages = {
            "bn": "Bangla", "en": "İngilizce", "ko": "Korece", "fr": "Fransızca", 'tr': 'Türkçe',
            "de": "Almanca", "he": "İbranice", "hi": "Hintçe", "it": "İtalyanca",
            "ja": "Japonca", "la": "Latince", "ms": "Malayca", "ne": "Nepalce",
            "ru": "Rusça", "ar": "Arapça", "zh": "Çince", "es": "İspanyolca"
        }

        self.style = ttk.Style()
        self.style.theme_use("clam")
        self.style.configure("TButton", font=("Arial", 12), foreground="white", background="#0078d4")
        self.style.configure("TLabel", font=("Arial", 12))
        self.style.configure("TCombobox", font=("Arial", 12))

        self.create_widgets()

    def create_widgets(self):
        self.language_var = tk.StringVar(value="İngilizce")
        
        label = tk.Label(self.root, text="Metin Çevirici", font=("Arial", 16, "bold"))
        label.pack(pady=10)
        
        self.output_text = tk.Text(self.root, height=10, width=40)
        self.output_text.pack(padx=10, pady=10)

        self.language_label = tk.Label(self.root, text="Çevrilecek Dil:", font=("Arial", 12))
        self.language_label.pack()

        self.language_menu = ttk.Combobox(self.root, textvariable=self.language_var, values=list(self.languages.values()))
        self.language_menu.pack()

        self.translate_button = tk.Button(self.root, text="Çevir", font=("Arial", 12), command=self.translate_text)
        self.translate_button.pack(pady=10)

        self.quit_button = tk.Button(self.root, text="Çıkış", font=("Arial", 12), command=self.root.quit)
        self.quit_button.pack()

    def translate_text(self):
        selected_language = self.language_var.get()
        input_text = self.output_text.get("1.0", tk.END).strip()

        if not input_text:
            return

        try:
            for code, language in self.languages.items():
                if language == selected_language:
                    selected_code = code
                    break

            translated = self.translator.translate(input_text, dest=selected_code)
            # translated_text = f"{selected_language} Çevirisi:\n{translated.text}\n\n"
            translated_text = f"{translated.text}"
            # translated_text += f"Telaffuz: {translated.pronunciation}\n"
            # translated_text += f"Çevrildiği Dil: {self.languages[translated.src]}"

            self.output_text.delete("1.0", tk.END)
            self.output_text.insert(tk.END, translated_text)
        except Exception as e:
            self.output_text.delete("1.0", tk.END)
            self.output_text.insert(tk.END, f"Bir hata oluştu: {e}")

if __name__ == "__main__":
    root = tk.Tk()
    app = LanguageTranslatorApp(root)
    root.mainloop()
