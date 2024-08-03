import sys
import torch
from PyQt5.QtWidgets import QHBoxLayout, QApplication, QMainWindow, QWidget, QVBoxLayout, QLabel, QComboBox, QTextEdit, QPushButton, QGraphicsView, QGraphicsScene, QGraphicsPixmapItem
from PyQt5.QtCore import Qt
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
from IndicTransTokenizer import IndicProcessor

# Define the languages and their codes
languages = {
    "Assamese": "asm_Beng",
    "Bengali": "ben_Beng",
    "Gujarati": "guj_Gujr",
    "Hindi": "hin_Deva",
    "Kannada": "kan_Knda",
    "Malayalam": "mal_Mlym",
    "Marathi": "mar_Deva",
    "Nepali": "npi_Deva",
    "Odia": "ory_Orya",
    "Punjabi": "pan_Guru",
    "Sanskrit": "san_Deva",
    "Sindhi (Devanagari)": "snd_Deva",
    "Tamil": "tam_Taml",
    "Telugu": "tel_Telu",
    "Urdu": "urd_Arab",
    "English": "eng_Latn"
}

# Function to determine the model based on source and target languages
def load_model(source_lang, target_lang):
    if source_lang == "eng_Latn":
        return "en-indic"
    elif target_lang == "eng_Latn":
        return "indic-en"
    else:
        return "indic-indic"

class TranslatorApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Indic Language Translator")
        self.setGeometry(100, 100, 1000, 700)  # Adjusted window size for better readability

        # Create central widget
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        # Create layout
        layout = QVBoxLayout(central_widget)
        self.setStyleSheet("background-color: #FFDFDD;")
        # Create heading and tagline
        self.heading_label = QLabel("SAARTHI: Translator", self)
        self.heading_label.setStyleSheet("background-color: #a278f5; font-size: 36px; font-weight: bold; color: #333333;")
        self.heading_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.heading_label)

        self.tagline_label = QLabel("Bhaasha Ki Yatra Mein Apka Saathi", self)
        self.tagline_label.setStyleSheet("font-size: 24px; font-weight: bold; font-style: italic; color: #555555;")
        self.tagline_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.tagline_label)

        # Create source language dropdown and text area
        source_layout = QVBoxLayout()
        source_label = QLabel("Source Language:", self)
        source_label.setStyleSheet("font-size: 22px;")
        source_layout.addWidget(source_label)

        self.source_lang_combo = QComboBox()
        self.source_lang_combo.addItems(languages.keys())
        self.source_lang_combo.setStyleSheet("font-size: 18px;")
        source_layout.addWidget(self.source_lang_combo)

        source_text_label = QLabel("Enter text to translate:", self)
        source_text_label.setStyleSheet("font-size: 20px; font-weight: bold;")
        source_layout.addWidget(source_text_label)

        self.text_input = QTextEdit()
        self.text_input.setStyleSheet("font-size: 18px; font-weight: bold;")
        source_layout.addWidget(self.text_input)

        # Create target language dropdown and text area
        target_layout = QVBoxLayout()
        target_label = QLabel("Target Language:", self)
        target_label.setStyleSheet("font-size: 22px;")
        target_layout.addWidget(target_label)

        self.target_lang_combo = QComboBox()
        self.target_lang_combo.addItems(languages.keys())
        self.target_lang_combo.setStyleSheet("font-size: 18px;")
        target_layout.addWidget(self.target_lang_combo)

        target_text_label = QLabel("Translated text:", self)
        target_text_label.setStyleSheet("font-size: 20px; font-weight: bold;")
        target_layout.addWidget(target_text_label)

        self.text_output = QTextEdit()
        self.text_output.setReadOnly(True)
        self.text_output.setStyleSheet("font-size: 22px; font-weight: bold;")
        target_layout.addWidget(self.text_output)

        # Create translate button
        self.translate_button = QPushButton("Translate")
        self.translate_button.setStyleSheet("""
            font-size: 20px; 
            color: #ffffff; 
            font-weight: bold; 
            padding: 10px; 
            border: none; 
            border-radius: 5px; 
            background-color: #007BFF;
            transition: background-color 0.3s;
        """)
        self.translate_button.setCursor(Qt.PointingHandCursor)
        self.translate_button.clicked.connect(self.translate_text)
        self.translate_button.installEventFilter(self)
        
        # Create layout to arrange source and target side by side
        within_layout = QHBoxLayout()
        within_layout.addLayout(source_layout)
        within_layout.addSpacing(20)
        within_layout.addLayout(target_layout)

        layout.addLayout(within_layout)
        layout.addWidget(self.translate_button)

    def eventFilter(self, source, event):
        if source is self.translate_button and event.type() == event.Enter:
            self.translate_button.setStyleSheet("""
                font-size: 20px; 
                color: #ffffff; 
                font-weight: bold; 
                padding: 10px; 
                border: none; 
                border-radius: 5px; 
                background-color: #0056b3;
                transition: background-color 0.3s;
            """)
        elif source is self.translate_button and event.type() == event.Leave:
            self.translate_button.setStyleSheet("""
                font-size: 20px; 
                color: #ffffff; 
                font-weight: bold; 
                padding: 10px; 
                border: none; 
                border-radius: 5px; 
                background-color: #007BFF;
                transition: background-color 0.3s;
            """)
        return super().eventFilter(source, event)

    def translate_text(self):
        # Get user selections
        src_lang = languages[self.source_lang_combo.currentText()]
        tgt_lang = languages[self.target_lang_combo.currentText()]
        input_sentence = self.text_input.toPlainText()

        # Determine the appropriate model based on source and target languages
        model_name = "ai4bharat/indictrans2-" + load_model(src_lang, tgt_lang) + "-1B"
        tokenizer = AutoTokenizer.from_pretrained(model_name, trust_remote_code=True)
        model = AutoModelForSeq2SeqLM.from_pretrained(model_name, trust_remote_code=True)
        ip = IndicProcessor(inference=True)

        # Preprocess input sentence
        batch = ip.preprocess_batch([input_sentence], src_lang=src_lang, tgt_lang=tgt_lang)
        DEVICE = "cuda" if torch.cuda.is_available() else "cpu"

        # Tokenize and encode input
        inputs = tokenizer(
            batch,
            truncation=True,
            padding="longest",
            return_tensors="pt",
            return_attention_mask=True,
        ).to(DEVICE)

        # Generate translation
        with torch.no_grad():
            generated_tokens = model.generate(
                **inputs,
                use_cache=True,
                min_length=0,
                max_length=256,
                num_beams=5,
                num_return_sequences=1,
            )

        # Decode and postprocess translation
        with tokenizer.as_target_tokenizer():
            generated_tokens = tokenizer.batch_decode(     #converts the token Ids back into text
                generated_tokens.detach().cpu().tolist(),
                skip_special_tokens=True,
                clean_up_tokenization_spaces=True,
            )
        translation = ip.postprocess_batch(generated_tokens, lang=tgt_lang)

        # Display the translation
        self.text_output.setPlainText(translation[0])

def main():
    app = QApplication(sys.argv)
    window = TranslatorApp()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
