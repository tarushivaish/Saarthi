import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QTextEdit, QComboBox, QGraphicsScene, QGraphicsView, QGraphicsPixmapItem
from PyQt5.QtGui import QPixmap, QImage, QFont, QColor 
from PyQt5.QtGui import QPixmap, QImage, QFont, QColor, QPalette
from PyQt5.QtCore import Qt
from wordcloud import WordCloud
from collections import Counter
import matplotlib.pyplot as plt
from io import BytesIO
from textblob import TextBlob
import nltk
from nltk.corpus import stopwords
from indicnlp.tokenize import indic_tokenize
from indicnlp.normalize.indic_normalize import IndicNormalizerFactory
import numpy as np

nltk.download('stopwords')

# Set up Indic NLP library resources path
INDIC_RESOURCES_PATH = 'C:/Users/tuf/indic_nlp_resources'

def init():
    global INDIC_RESOURCES_PATH
    if INDIC_RESOURCES_PATH == '':
        raise IndicNlpException('INDIC_RESOURCES_PATH not set')

def get_resources_path():
    return INDIC_RESOURCES_PATH

def set_resources_path(resources_path):
    global INDIC_RESOURCES_PATH
    INDIC_RESOURCES_PATH = resources_path

class IndicNlpException(Exception):
    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return repr(self.msg)

set_resources_path(INDIC_RESOURCES_PATH)

advertools_stopwords = adv.stopwords

def load_stopwords_from_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as file:
        return set(file.read().strip().split())

gujarati_stopwords = load_stopwords_from_file("C://Users//tuf//Desktop//workingondata//gujarati.txt")
marathi_stopwords = load_stopwords_from_file("C://Users//tuf//Desktop//workingondata//hindi.txt")
kannada_stopwords = load_stopwords_from_file("C://Users//tuf//Desktop//workingondata//kannada.txt")

odia_stopwords = {
    "ଏହି", "ସେ", "କି", "କିଣ୍ଟୁ", "ସେହି", "ଏହା", "ସେହି", "କେବଳ", "ତଥାପି", "ଏକ", "ତା", "ତାହା", "ସହ",
    "ଏଠାରେ", "ଯେଉଁ", "ଜାଣି", "ନାହିଁ", "ସ୍ଥାନ", "ଅନ୍ୟ", "ହେଲେ", "ଏପରି", "ନୁହେଁ", "ବା", "ଅପେକ୍ଷା",
    "କିଣ୍ଟୁ", "ଏହି", "ନିମନ୍ତେ", "ଏହିପରି", "ସବୁ", "କେଉଁ", "ଜଣା", "ସହିତ", "ତେଣୁ", "ଏହା", "ଯେ", "ଏହି",
    "ଏହିପରି", "ଉପରେ", "କଥା", "ସେହି", "ପ୍ରତି", "ବେଳେ", "ସମୟ", "ଜାଣ", "ଅନ୍ୟା", "ସେ", "ହେଲେ", "ପ୍ରଥମ",
    "ଯେପରି", "ହେବା", "ଜଣା", "ଯଥା", "ତଥା", "ଅନୁସାରେ", "ଅନ୍ତର୍ଗତ", "ବିଶେଷ", "କିପରି", "କେଉଁସି", "କିଛି",
    "ସଂଖ୍ୟା", "ସେଗୁଡିକ", "ଅଧିକ", "ଏବଂ", "ଏହିପରି", "ବ୍ୟତୀତ", "ନେହାତି", "ଏହି", "ସମସ୍ତ", "ଉପରେ", "ସମସ୍ତେ",
    "ନିମନ୍ତେ", "ସହାୟ", "ପ୍ରସଙ୍ଗରେ", "ହେବାରୁ", "ସ୍ଥିତି", "ନିକଟ", "ଅନ୍ୟସମ୍ବନ୍ଧୀ", "କାରଣ", "ବସ୍ତୁ", "ପ୍ରକାର",
    "ମଧ୍ୟ", "ବ୍ୟବହାର", "କ୍ଷେତ୍ରରେ", "ସ୍ଥିତ", "ସହିତ", "ମାନେ", "ଯଥା", "ତାଳ", "ପ୍ରତି", "ଉପକାର", "ସଂବନ୍ଧୀୟ",
    "ତ୍ରାଣ", "ସେଗୁଡିକ", "ପ୍ରଧାନ", "ସହିତ", "ସମ୍ବନ୍ଧିତ", "ସ୍ଥାନରେ", "ସେଇ", "କ୍ଷେତ୍ର", "ଏକରୁ", "ଏହାପରି",
    "ସମ୍ବନ୍ଧ", "କେବଳ", "ଅଧିକ", "ସାଧାରଣ", "ଯାହା", "ସମୟରେ", "ସଂସ୍ଥା", "ନିମିତ୍ତ", "କିଛି", "ସାମ୍ପ୍ରତିକ",
    "ବସ୍ତୁରେ", "ବିନା", "ସମସ୍ତ", "ସେଗୁଡିକ", "କାର୍ୟ", "ସମ୍ପୂର୍ଣ୍ଣ", "ବେଲେ", "ସହାୟକ", "ପ୍ରଧାନ", "ଏହା",
    "ସାଧାରଣତଃ", "ତିନି", "ବେଳେ", "କିନ୍ତୁ", "ପ୍ରାୟ", "ବାହାରେ", "ବହୁତ", "ପ୍ରାୟ", "ସଂଖ୍ୟାରେ", "ପ୍ରକାରରେ",
    "ହୋଇ", "ଅନ୍ୟରୁ", "ଏବଂ", "ପ୍ରକାରରେ", "ପ୍ରସଙ୍ଗ", "ସବୁ", "ପ୍ରଥମେ", "ସେଗୁଡିକ", "ସମସ୍ତଙ୍କ", "କିପରି",
    "ଏହି", "ସେହି", "ଯଥା", "ସେ", "ସମସ୍ତ", "ସେମାନେ", "ସେ", "ସେମାନେ", "ଉପରେ", "ସହିତ", "ସମସ୍ତଙ୍କୁ", "ସବୁ",
    "ପ୍ରକାର", "କେଉଁ", "ସବୁ", "ନିର୍ଦ୍ଦିଷ୍ଟ", "ସମୟରେ", "ଅନୁଗତ", "ଅନ୍ତର୍ଗତ", "ବିଶେଷ", "ଏହି", "ସମ୍ପର୍କ",
    "କିପରି", "ତୁଳନା", "ପ୍ରକାର", "ସ୍ଥିତ", "ପ୍ରଧାନ", "ସହିତ", "ସାଧାରଣ", "ପ୍ରଧାନ", "କିଛି", "ସାମ୍ପ୍ରତିକ",
    "ବେଳେ", "ପ୍ରକାର", "ସବୁ", "ସ୍ଥିତି", "ସମୟରେ", "ସମ୍ବନ୍ଧ", "ସହିତ", "ପ୍ରକାର", "କ୍ଷେତ୍ର", "ସମ୍ପର୍କ"
}


hindi_stopwords = {
    "अंदर", "अत", "अदि", "अप", "अपना", "अपनि", "अपनी", "अपने", "अभि", "अभी", "आदि", "आप", "इंहिं", "इंहें",
    "इंहों", "इतयादि", "इत्यादि", "इन", "इनका", "इन्हीं", "इन्हें", "इन्हों", "इस", "इसका", "इसकि", "इसकी", "इसके",
    "इसमें", "इसि", "इसी", "इसे", "उंहिं", "उंहें", "उंहों", "उन", "उनका", "उनकि", "उनकी", "उनके", "उनको",
    "उन्हीं", "उन्हें", "उन्हों", "उस", "उसके", "उसि", "उसी", "उसे", "एक", "एवं", "एस", "एसे", "ऐसे", "ओर", "और",
    "कइ", "कई", "कर", "करता", "करते", "करना", "करने", "करें", "कहते", "कहा", "का", "काफि", "काफ़ी", "कि", "किंहें",
    "किंहों", "कितना", "किन्हें", "किन्हों", "किया", "किर", "किस", "किसि", "किसी", "किसे", "की", "कुछ", "कुल", "के",
    "को", "कोइ", "कोई", "कोन", "कोनसा", "कौन", "कौनसा", "गया", "घर", "जब", "जहाँ", "जहां", "जा", "जिंहें", "जिंहों",
    "जितना", "जिधर", "जिन", "जिन्हें", "जिन्हों", "जिस", "जिसे", "जीधर", "जेसा", "जेसे", "जैसा", "जैसे", "जो", "तक",
    "तब", "तरह", "तिंहें", "तिंहों", "तिन", "तिन्हें", "तिन्हों", "तिस", "तिसे", "तो", "था", "थि", "थी", "थे", "दबारा",
    "दवारा", "दिया", "दुसरा", "दुसरे", "दूसरे", "दो", "द्वारा", "न", "नहिं", "नहीं", "ना", "निचे", "निहायत", "नीचे",
    "ने", "पर", "पहले", "पुरा", "पूरा", "पे", "फिर", "बनि", "बनी", "बहि", "बही", "बहुत", "बाद", "बाला", "बिलकुल",
    "भि", "भितर", "भी", "भीतर", "मगर", "मानो", "मे", "में", "यदि", "यह", "यहाँ", "यहां", "यहि", "यही", "या", "यिह",
    "ये", "रखें", "रवासा", "रहा", "रहे", "ऱ्वासा", "लिए", "लिये", "लेकिन", "व", "वगेरह", "वरग", "वर्ग", "वह", "वहाँ",
    "वहां", "वहिं", "वहीं", "वाले", "वुह", "वे", "वग़ैरह", "संग", "सकता", "सकते", "सबसे", "सभि", "सभी", "साथ", "साबुत",
    "साभ", "सारा", "से", "सो", "हि", "ही", "हुअ", "हुआ", "हुइ", "हुई", "हुए", "हे", "हें", "है", "हैं", "हो", "होता",
    "होति", "होती", "होते", "होना", "होने", "ले", "सकें", "और", "साथ", "ही", "बिना", "किसी", "क", "को", "या", "दे", "रही", 
    "है", "परंतु", "फिर", "भी", "उन्हें", "कई", "बार", "लेने", "का", "देता", "है", "एक", "ऐसी", "अब", "आता", "है"
}

    
    

punjabi_stopwords = {
    "ਦਾ", "ਤੇ", "ਇੱਕ", "ਨੂੰ", "ਦੇ", "ਹੈ", "ਕੀ", "ਹੋਰ", "ਇਹ", "ਹੇਠਾਂ", "ਅਤੇ", "ਤੁਹਾਡਾ", "ਤੁਹਾਡੇ", "ਕਿੰਨ੍ਹਾ",
    "ਵਿੱਚ", "ਕਿਸੇ", "ਸਭ", "ਹਨ", "ਤੋਂ", "ਵਾਹਿਗੁਰੂ", "ਜੋ", "ਤੁਸੀਂ", "ਕਦੇ", "ਹਰ", "ਕਿਹੜਾ", "ਹੈ", "ਹੋ", "ਨਹੀਂ",
    "ਪਹਿਲਾਂ", "ਜੋ", "ਤੁਹਾਡਾ", "ਹੋਣਾ", "ਅਸੀਂ", "ਇਸ", "ਵਿਚ", "ਹੁਣ", "ਕਿਉਂ", "ਜਦੋਂ", "ਤੋ", "ਕਿਹੜੇ", "ਜਾਂ", "ਬਾਅਦ",
    "ਸੰਗ", "ਜਿਸ", "ਪੂਰੀ", "ਕੋ", "ਸਾਹਿਬ", "ਪਤਾ", "ਸਕਦਾ", "ਸਕਦੀ", "ਸਕਦੇ", "ਸਕਦੀ", "ਤੁਹਾਨੂੰ", "ਇੱਕ", "ਕਰ", "ਕਰਨਾ",
    "ਕਰਨ", "ਆਪਣੇ", "ਉਸ", "ਉਹ", "ਉਹਨਾਂ", "ਉਹਨਾਂ", "ਤੁਹਾਡੇ", "ਤੁਹਾਨੂੰ", "ਬਿਲਕੁਲ", "ਇਸ", "ਜਿਸ", "ਜਿਸ ਨੂੰ", "ਜਿੰਨ੍ਹਾਂ",
    "ਉਹਨਾਂ", "ਤਿਨ੍ਹਾਂ", "ਜਿੰਨਾਂ", "ਵੱਧ", "ਤੂੰ", "ਪਿਛਲੇ", "ਆਪ", "ਹੋ", "ਲਈ", "ਆਪਣੇ", "ਉਹਨਾਂ", "ਮੁਤਾਬਕ", "ਪ੍ਰਸੰਗ",
    "ਹੋਰ", "ਕਿੰਝ", "ਕਿਸੇ", "ਉਹ", "ਸਕਦੇ", "ਕਿਰਿਆ", "ਹੋਣ", "ਦਿਨ", "ਹਰ", "ਪ੍ਰਕਾਰ", "ਰਹਿੰਦਾ", "ਰਹਿੰਦੀ", "ਨੂੰ", "ਵਿਦੇਸ਼",
    "ਕਿਵੇਂ", "ਇਸ", "ਪਿਛਲੇ", "ਲਾਹ", "ਹੋਣਾ", "ਕਿਸੇ", "ਤਸਵੀਰ", "ਇਹ", "ਹੋਣਾ", "ਤੋਂ", "ਜੋ", "ਲਗਭਗ", "ਤਕ", "ਕਿਸੇ",
    "ਉਹਨਾਂ", "ਹੇਠਾਂ", "ਉਹ", "ਅਸਲ", "ਤੁਹਾਡਾ", "ਪਿਛਲੇ", "ਹੋਣਾ", "ਕਿਸੇ", "ਸਿੱਧਾ", "ਅੰਤ", "ਨਵਾਂ", "ਬਦਲ", "ਇਹ", "ਜਾਂ",
    "ਸਿੱਧੇ", "ਹੁਣ", "ਸਿਰਫ", "ਬਚਾ", "ਨੌਕਰੀ", "ਲਗਦਾ", "ਤੁਹਾਨੂੰ", "ਜੋ", "ਚੀਜ਼", "ਕੀ", "ਕਿਰਿਆ", "ਹੋਰ", "ਹੂੰ", "ਸਾਰੇ",
    "ਹੀ", "ਪਿਛਲਾ", "ਕਰ", "ਕਰਨਾ", "ਹੋਰ", "ਬਹੁਤ", "ਵਾਰ", "ਤਰੀਕਾ", "ਜਿਥੇ", "ਅਹੰਕਾਰ", "ਵਧੀਆ", "ਉਹ", "ਪੇਸ਼", "ਬਿਨਾਂ",
    "ਸਿਰਫ", "ਉਹ", "ਸਾਰੇ", "ਵਿਆਖਿਆ", "ਲੌਟ", "ਕਰ", "ਕਰਨਾ", "ਕਦੇ", "ਹੁਣ", "ਵਿਕਲਪ", "ਵਰਗ", "ਅਜਿਹੇ", "ਲੰਬਾ", "ਹੁਣ",
    "ਇਹ", "ਕਰ", "ਕਰਨਾ", "ਜਿਸ", "ਵਿਦੇਸ਼", "ਉਹ", "ਹੇਠਾਂ", "ਜਿਸ", "ਸਾਰਾ", "ਪਾਰ", "ਲਾਗੂ", "ਤੂ", "ਆਪ", "ਵਿਚ"
}


sindhi_stopwords = {
    "۽", "جي", "مان", "ٿي", "جو", "جيئي", "بهرحال", "سڀني", "اهو", "ڪم", "هڪ", "ڪن", "پڻ", "تو", "جڏهن", 
    "ڪهڙو", "ان", "مختلف", "سڀ", "اڳ ۾", "جيتوڻيڪ", "نٿو", "اهڙي", "جڻڪ", "جنهن", "اِهو", "جائزو", "هر", 
    "صرف", "جيڪي", "نئون", "توهان", "ٻيا", "ڳڻڻ", "پنهنجي", "کڻ", "ڪڙي", "ڇا", "شمار", "ڪندؤ", "جڳهه", 
    "جيئن", "سڀڪو", "چوڻ", "خاص", "ادائيگي", "محسوس", "اهڙين", "انهي", "جيڪي", "ڪنهن", "جنهن", "واسطو", 
    "خود", "ڳڻڻ", "جائزو", "جي", "آهي", "ڪن", "ڀرپور", "ماڻهو", "ملڻ", "درست", "اڃان", "اڳ", "سڀ", "جزو", 
    "سمجهاڻي", "ڪم", "پوسٽ", "سمجھڻ", "جي", "اهي", "ان ۾", "سڀني", "اڪثر", "سڄو", "نظريو", "ظاہر", "خود", 
    "جگہ", "مدد", "پڻ", "پڻ", "قوت", "وجھڻ", "جزء", "سڀ", "ڪم", "آسان", "خاص", "آهي", "تسليم", "تسليم", 
    "بنياد", "تبديل", "جڳھ", "اجازت", "تمام", "سڀ", "پراڻن", "جيتوڻيڪ", "واسطو", "جيئن", "افسوس", "ادائيگي", 
    "ملڻ", "ڪڻڻ", "جڳهه", "سڀئي", "ڳڻڻ", "پڻ", "تفصيل", "تجويز", "جڏهن", "تنقيد", "مان", "ڳڻڻ", "پڇڻ", 
    "تجويز", "پيٽ", "ملڻ", "ضروري", "ضروري", "تبديل", "سڀئي", "پوءِ", "پوسٽ", "پر", "پڻ", "منصوبو", "خاص", 
    "چڪاس", "چٽي", "ڪا", "بند", "چون", "اهو", "تجويز", "وڏو", "تفصيل", "شامل", "تجويز", "سڀني", "وڌيڪ", 
    "چون", "پهرين", "هن", "ڪندؤ", "شروعات", "جڳھ", "چونڊ", "پھر", "اهو", "معلومات", "پڻ", "سڀني", "خاص", 
    "سڀ", "وجھڻ", "پوسٽ", "تبديل", "تفصيل", "رپورٽ", "پوءِ", "پڻ", "سمجهاڻي", "جڏهن", "ادائيگي", "محسوس"
}


sanskrit_stopwords = {
    "अत", "तत", "यत", "तस्मिन्", "किमपि", "एव", "इति", "अत", "अपि", "न", "च", "किं", "यत्र", "इत्यादि",
    "स्व", "सप्त", "नहि", "वह", "अस्मिन्", "कथा", "अद्य", "पञ्च", "पृष्ठ", "यः", "यदि", "गत्वा", "ते", "मम",
    "एष", "नम", "कृ", "अधिक", "प्रथम", "अन्य", "नूतन", "प्रति", "जस्मिन्", "तत्र", "कथं", "यावद्", "तव", "को",
    "एवं", "अस्मात्", "कथयामि", "मात्र", "अवश्य", "गत्वा", "तुल", "कोप", "अनुमान", "रूप", "तुलना", "सकर्मक",
    "अधिकार", "प्रस्ताव", "सर्व", "वर्तमान", "संपर्क", "विचार", "पुस्तक", "तथा", "किम", "नून", "अलं", "साध",
    "परीक्षा", "कथा", "उप", "ध्यान", "सुन", "अत्र", "उपस्थित", "विचार", "संख्या", "यथा", "नियम", "विधान", "पद्धति",
    "वर्ग", "सिद्ध", "विषय", "विषयः", "अन्तर", "सूचना", "तंत्र", "प्रकार", "संबंध", "अनुसार", "द्वारा", "कर",
    "लक्ष्य", "अनुवाद", "अधिकार", "सामग्री", "विस्तार", "रचना", "ग्रहण", "सह", "स्वीकृत", "कर्म", "संक्षेप",
    "अर्थ", "प्रमाण", "सार", "उपयोग", "उद्देश्य", "विवरण", "सूत्र", "वर्ण", "अधिकार", "दृष्टि", "सामान्य", "वास्तव",
    "मूल", "पात्र", "अभ्यास", "साधारण", "प्रस्ताव", "चयन", "अवलोकन", "स्वरूप", "उपाय", "संयोजन", "नियमित", "संदर्भ",
    "ध्यान", "प्रस्तावना", "प्रस्तुत", "पुस्तिका", "सम्बंध", "मूल्य", "निम्न", "उल्लेख", "संदर्भ", "विकल्प", "अनुभव",
    "तुलना", "केंद्रीय", "सिद्धांत", "विशेष", "वर्ग", "अनुसंधान", "अवधि", "संविधान", "आधार", "वर्णन", "प्रयोजन",
    "उपस्थिति", "परिस्थिति", "अर्थात", "विधि", "समाज", "विस्तृत", "संग्रह", "प्रकार", "आवश्यक", "सदस्य", "सहायता",
    "विधि", "संघटन", "विश्लेषण", "वर्णन", "परीक्षण", "संज्ञा", "संस्थापन", "विवरण", "योजना", "उपयोग", "साहित्य", "विषय", "किम्", "इति","अर्हति","अतः"
    "अत", "तत", "यत", "अधि", "अस्मिन्", "स्व", "अल", "न", "इति", "च", "इदम्", "प्रति", "य", "किम", 
    "वह", "स्मिन", "तत्र", "विषय", "तस्मिन्", "सर्व", "कृ", "प्रकार", "उप", "अधिक", "अतः", "संग", 
    "द्वार", "आ", "नहि", "कथम्", "तुम", "नय", "अन्य", "सं", "सहित", "विषये", "तथा", "संदर्भ", "कथा", 
    "पर", "उपस्थित", "संपर्क", "अर्थ", "वर्ण", "अवधि", "समय", "प्रकारे", "अस्मि", "इह", "त", "को", 
    "अलं", "उपयोग", "उपस्थित", "मात्र", "सिद्ध", "त", "प्रश्न", "ध्यान", "साधारण", "परिस्थिति", "संग्रह", "अस्ति", "यत्", "अ", "अ","वा", "यथा", "सः" 
}

malayalam_stopwords = {
    "എന്നേക്കും", "മാത്രമേ", "തുടരുന്ന", "പിന്നെയും", "കുറഞ്ഞത്", "മാറി", "വേണ്ട", "ഇതുവരെയല്ല", "അത്", "ആ", 
    "ഇവ", "എവിടെ", "വരുന്നു", "നിങ്ങളുടെ", "വിലക്ക്", "ആകുന്നു", "ചെയ്യുന്ന", "അന്ന", "അല്ല", "എന്തായാലും", 
    "ഉള്ള", "ഒരു", "ചെയ്യുന്നത്", "അതുപോലെ", "ഇവിടെ", "അല്ലെങ്കില്", "അവ", "ആരും", "അങ്ങ്", "കഴിഞ്ഞ", 
    "ഈ", "ഒരുപക്ഷേ", "സമയം", "ഇതിനു", "എന്റെ", "നിങ്ങളെ", "അങ്ങനെ", "നിങ്ങള്", "ചില", "തികയ്ക്കേണ്ട", 
    "കണ്ടു", "കാത്തിരിക്കുക", "എങ്ങനെയോ", "വരെ", "ആവശ്യം", "ഉടന്", "പ്രകാരം", "വേണ്ടി", "അവസാനം", 
    "പുതിയ", "ഇത്", "എന്തെങ്കിലും", "അതേ", "കൂട്ടി", "എനിക്ക്", "അയാളുടെ", "ഒരിക്കൽ", "അവസാനമായി", 
    "സഹായം", "അനുവദിക്കുന്നു", "ഏതെങ്കിലും", "വിശേഷണം", "വലിയ", "നിങ്ങളുടെ", "പൂർണ്ണ", "എത്ര", "പെട്ടെന്ന്", 
    "പ്രധാന", "എന്ത്", "സാധാരണം", "ചിലപ്പോൾ", "ഇവരേയും", "ആയിരിക്കും", "ഇവിടെയാണ്", "പറ്റിയ", "പടി", 
    "ഇല്ല", "സാധിച്ചാൽ", "ഇവിടെ", "ആവശ്യമായ", "പല", "അവിടെ", "ഒരു", "അറിയുക", "വിതരണ", "ഇവിടെ", 
    "വിവരങ്ങൾ", "നിങ്ങളുടെ", "അവയുടെ", "കൂടുതൽ", "എനിക്ക്", "പണിയെടുക്കുക", "വിവിധ", "പക്ഷേ", "പ്രവൃത്തി", 
    "പരിശോധന", "ആയിരിക്കും", "ആവശ്യകത", "എങ്കിലും", "ഇടയിൽ", "ഏത്", "വിശേഷ", "വായിക്കുക", "സാധ്യമായ", 
    "പങ്കു", "അവിടെ", "വിവരം", "പരിധി", "ഉപയോഗം", "വില", "സംഭവം", "സാധാരണ", "വിശേഷണം", "സാധ്യമായ", 
    "ആവശ്യമായി", "പ്രവൃത്തി", "കൂടി", "വാസ്തവത്തിൽ", "എങ്കിൽ", "കൂടെ", "മാത്രം", "അവസാന", "ഈ", 
    "പ്രസിദ്ധ", "വേണം", "നിലവിൽ", "ഇവിടെയുള്ള", "എന്റെ", "വിവരണം", "പ്രവൃത്തികൾ", "ഏത്", "വൈവിധ്യ",
    "ശേഷം", "അറിയണം", "നിങ്ങളുടെ", "നിലവിൽ", "പുറത്ത്", "അവസാനം", "മാത്രം", "ഇല്ലാതാക്കുക", 
    "ലഭിച്ച", "നിങ്ങളെ", "പിന്നീട്", "പുത്തൻ", "കൂടാതെ", "ഒരുപാട്", "പോലെ", "പട്ടിക", "ഉണ്ട്", 
    "പുതിയ", "വിശദീകരണം", "സഹായിക്കുക", "അവസ്ഥ", "ആവശ്യം", "ഇവിടെ", "സാധ്യമായ", "ചെയ്യുക"
}


font_paths = {
    'asm': 'C://Users//tuf//Desktop//workingondata//Noto//assamese.ttf',
    'bn': 'noto_sans/Bengali/NotoSansBengali-Regular.ttf',
    'gu': 'noto_sans/Gujarati/NotoSansGujarati-Regular.ttf',
    'hi': 'Back/noto_sans/Devanagari/NotoSansDevanagariUI-Regular.ttf',
    'kn': 'C://Users//tuf//Desktop//git repo//Saarthi//Back//noto_sans//Kannada//NotoSansKannadaUI-Regular.ttf',
    'ml': 'noto_sans/Malayalam/NotoSansMalayalam-Regular.ttf',
    'mr': 'noto_sans/Devanagari/NotoSansDevanagari-Regular.ttf',
    'ne': 'C://Users//tuf//Desktop//workingondata//Noto//nepali.ttf',
    'or': 'noto_sans/Oriya/NotoSansOriya-Regular.ttf',
    'pa': 'C://Users//tuf//Desktop//workingondata//lohit.punjabi.ttf',
    'sa': 'C://Users//tuf//Desktop//workingondata//Noto//TiroDevanagariSanskrit-Regular.ttf',
    'sd': 'noto_sans/Arabic/NotoNaskhArabic-Regular.ttf',
    'ta': 'noto_sans/Tamil/NotoSansTamil-Regular.ttf',
    'te': 'noto_sans/Telugu/NotoSansTelugu-Regular.ttf',
    'ur': 'noto_sans/Arabic/NotoNaskhArabic-Regular.ttf',
    'en': 'Back/noto_sans/Latin/NotoSans-Medium.ttf'
}

# Regular expressions for different scripts
regex_patterns = {
    'asm': r"[\u0980-\u09FF]+",  # Bengali (for Assamese)
    'bn': r"[\u0980-\u09FF]+",   # Bengali
    'gu': r"[\u0A80-\u0AFF]+",   # Gujarati
    'hi': r"[\u0900-\u097F]+",   # Devanagari (for Hindi)
    'kn': r"[\u0C80-\u0CFF]+",   # Kannada
    'ml': r"[\u0D00-\u0D7F]+",   # Malayalam
    'mr': r"[\u0900-\u097F]+",   # Devanagari (for Marathi)
    'ne': r"[\u0900-\u097F]+",   # Devanagari (for Nepali)
    'or': r"[\u0B00-\u0B7F]+",   # Oriya
    'pa': r"[\u0A00-\u0A7F]+",   # Gurmukhi (for Punjabi)
    'sa': r"[\u0900-\u097F]+",   # Devanagari (for Sanskrit)
    'sd': r"[\u0600-\u06FF]+",   # Arabic (for Sindhi)
    'ta': r"[\u0B80-\u0BFF]+",   # Tamil
    'te': r"[\u0C00-\u0C7F]+",   # Telugu
    'ur': r"[\u0600-\u06FF]+",   # Arabic (for Urdu)
    'en': r"[a-zA-Z]+"           # Latin (for English)
}

# Language options
languages = {
    'en': 'eng_Latn',
    'bn': 'ben_Beng',
    'ne': 'npi_Deva',
    'ta': 'tam_Taml',
    'te': 'tel_Telu',
    'ur': 'urd_Arab',
    'hi': 'hin_Deva',
    'gu': 'guj_Gujr',
    'mr': 'mar_Deva',
    'pa': 'pan_Guru',
    'or': 'ory_Orya',
    'sa': 'san_Deva',
    'sd': 'snd_Deva',
    'ml': 'mal_Mlym',
    'kn': 'kan_Knda'}

def preprocess_text(text, lang):
    if not isinstance(text, str):
        raise ValueError("Input text must be a string.")

    if lang == 'en':
        stop_words = set(advertools_stopwords['english'])
    elif lang == 'bn':
        stop_words = set(advertools_stopwords['bengali'])
    elif lang == 'ne':
        stop_words = set(advertools_stopwords['nepali'])
    elif lang == 'ta':
        stop_words = set(advertools_stopwords['tamil'])
    elif lang == 'te':
        stop_words = set(advertools_stopwords['telugu'])
    elif lang == 'ur':
        stop_words = set(advertools_stopwords['urdu'])
    elif lang == 'hi':
        stop_words = hindi_stopwords
    elif lang == 'gu':
        stop_words = gujarati_stopwords
    elif lang == 'mr':
        stop_words = marathi_stopwords
    elif lang == 'pa':
        stop_words = punjabi_stopwords
    elif lang == 'or':
        stop_words = odia_stopwords
    elif lang == 'sa':
        stop_words = sanskrit_stopwords
    elif lang == 'sd':
        stop_words = sindhi_stopwords
    elif lang == 'ml':
        stop_words = malayalam_stopwords
    elif lang == 'kn':
        stop_words = kannada_stopwords
    else:
        normalizer_factory = IndicNormalizerFactory()
        normalizer = normalizer_factory.get_normalizer(lang)
        normalized_text = normalizer.normalize(text)
        tokens = indic_tokenize.trivial_tokenize(normalized_text)
        filtered_tokens = [token for token in tokens if token not in stop_words.get(lang, set())]
        return ' '.join(filtered_tokens)

    tokens = text.split()
    filtered_tokens = [token for token in tokens if token.lower() not in stop_words]
    return ' '.join(filtered_tokens)

class WordCloudApp(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("Word Cloud Generator")
        self.setGeometry(100, 100, 1200, 800)
        self.setStyleSheet("background-color: #FFDFDD;")

        # Set up central widget and layout
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout()
        self.central_widget.setLayout(self.layout)

        # Set up heading label
        self.heading_label = QLabel("SAARTHI : WORDCLOUD GENERATOR")
        self.heading_label.setFont(QFont("Times", 28, QFont.Bold))
        self.heading_label.setAlignment(Qt.AlignCenter)
        self.heading_label.setStyleSheet("""
            background-color: #a278f5;
            color: #ffffff;
            padding: 15px;
            margin-bottom: 20px;
            border-radius: 5px;
        """)
        self.layout.addWidget(self.heading_label)

        # Set up title label
        self.title_label = QLabel("Word Cloud Generator")
        self.title_label.setFont(QFont("Arial", 28, QFont.Bold))
        self.title_label.setAlignment(Qt.AlignCenter)
        self.title_label.setStyleSheet("color: #333333; padding: 10px;")
        self.layout.addWidget(self.title_label)

        # Set up language selection
        self.language_label = QLabel("Select Language:")
        self.language_label.setFont(QFont("Arial", 18))
        self.language_label.setStyleSheet("color: #333333; padding: 10px;")
        self.layout.addWidget(self.language_label)

        self.language_combobox = QComboBox()
        self.language_combobox.addItems([
            'Assamese', 'Bengali', 'Gujarati', 'Hindi', 'Kannada',
            'Malayalam', 'Marathi', 'Nepali', 'Oriya', 'Punjabi',
            'Sanskrit', 'Sindhi', 'Tamil', 'Telugu', 'Urdu', 'English'
        ])
        self.language_combobox.setFont(QFont("Arial", 16))
        self.language_combobox.setStyleSheet("background-color: #ffffff; border: 1px solid #cccccc; border-radius: 5px; padding: 10px;")
        self.layout.addWidget(self.language_combobox)

        # Set up text input
        self.text_input = QTextEdit()
        self.text_input.setPlaceholderText("Enter the paragraph here...")
        self.text_input.setFont(QFont("Arial", 16))
        self.text_input.setStyleSheet("background-color: #ffffff; border: 1px solid #cccccc; border-radius: 5px; padding: 15px;")
        self.layout.addWidget(self.text_input)

        # Set up generate button
        self.generate_button = QPushButton("Generate Word Cloud")
        self.generate_button.setFont(QFont("Arial", 16, QFont.Bold))
        self.generate_button.setStyleSheet("""
            background-color: #28a745;
            color: #ffffff;
            border: none;
            border-radius: 5px;
            padding: 15px;
            font-weight: bold;
            transition: background-color 0.3s;
        """)
        self.generate_button.clicked.connect(self.generate_wordcloud)
        self.generate_button.installEventFilter(self)
        self.layout.addWidget(self.generate_button)

        # Set up result view
        self.result_view = QGraphicsView()
        self.result_scene = QGraphicsScene()
        self.result_view.setScene(self.result_scene)
        self.result_view.setStyleSheet("background-color: #ffffff; border: 1px solid #cccccc;")
        self.layout.addWidget(self.result_view)

    def eventFilter(self, source, event):
        if source is self.generate_button and event.type() == event.Enter:
            self.generate_button.setStyleSheet("""
                background-color: #218838;
                color: #ffffff;
                border: none;
                border-radius: 5px;
                padding: 15px;
                font-weight: bold;
                transition: background-color 0.3s;
            """)
        elif source is self.generate_button and event.type() == event.Leave:
            self.generate_button.setStyleSheet("""
                background-color: #28a745;
                color: #ffffff;
                border: none;
                border-radius: 5px;
                padding: 15px;
                font-weight: bold;
                transition: background-color 0.3s;
            """)
        return super().eventFilter(source, event)

    def generate_wordcloud(self):
        language_map = {
            'Assamese': 'asm',
            'Bengali': 'bn',
            'Gujarati': 'gu',
            'Hindi': 'hi',
            'Kannada': 'kn',
            'Malayalam': 'ml',
            'Marathi': 'mr',
            'Nepali': 'ne',
            'Oriya': 'or',
            'Punjabi': 'pa',
            'Sanskrit': 'sa',
            'Sindhi': 'sd',
            'Tamil': 'ta',
            'Telugu': 'te',
            'Urdu': 'ur',
            'English': 'en'
        }

        selected_lang = self.language_combobox.currentText()
        lang_code = language_map.get(selected_lang)

        if lang_code:
            text = self.text_input.toPlainText()

            try:
                preprocessed_text = preprocess_text(text, lang_code)

                if preprocessed_text:
                    font_path = font_paths.get(lang_code)
                    regexp = regex_patterns.get(lang_code)

                    if font_path and regexp:
                        wordcloud = WordCloud(
                            font_path=font_path,
                            background_color="white",
                            width=1000,  # Increased width
                            height=500,  # Increased height
                            regexp=regexp
                        ).generate(preprocessed_text)

                        plt.figure(figsize=(12, 6))
                        plt.imshow(wordcloud, interpolation='bilinear')
                        plt.axis("off")

                        buf = BytesIO()
                        plt.savefig(buf, format='png')
                        buf.seek(0)
                        image = QImage()
                        image.loadFromData(buf.getvalue())
                        pixmap = QPixmap.fromImage(image)

                        self.result_scene.clear()
                        self.result_scene.addItem(QGraphicsPixmapItem(pixmap))
                        self.result_view.setScene(self.result_scene)

                        plt.close()
                    else:
                        print(f"Font path or regex pattern not found for {lang_code}")
                else:
                    print("Preprocessed text is empty. Please provide valid text.")
            except ValueError as ve:
                print(f"Error processing text: {ve}")
        else:
            print("Invalid language selected!")

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    window = WordCloudApp()
    window.show()
    sys.exit(app.exec_())