from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLineEdit, QLabel, QComboBox, QTextEdit
from PyQt5.QtGui import QPixmap, QImage
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QImage, QPixmap
import sys
import random

# Template definitions
templates_english = [
    "Mastering {}: Advanced Strategies for Success",
    "Unveiling {}: What You Need to Know to Get Ahead",
    "The Comprehensive Guide to {}: Tips, Techniques, and Tools",
    "Transform Your Understanding of {} with These Expert Tips",
    "The Ultimate Handbook on {}: Everything You Need to Succeed",
    "How {} is Shaping the Future",
    "The Definitive Guide to Navigating {}: Challenges and Solutions",
    "Essential Insights into {}: A Deep Dive",
    "The Top Trends in {} You Should Know About in 2024",
    "Harnessing {}: Practical Applications",
    "From Novice to Expert: Your Journey with {}",
    "The Role of {} in Various Scenarios",
    "Debunking Myths About {}: What’s True and What’s Not",
    "A Step-by-Step Approach to Mastering {}",
    "Innovative Approaches to {}: Emerging Techniques and Insights",
    "How {} is Revolutionizing Industries: Key Developments",
    "Expert Strategies for Leveraging {} to Achieve Goals",
    "The Most Common Misconceptions About {} and How to Avoid Them",
    "Advanced Techniques for Excelling at {}",
    "The Pros and Cons of {}",
    "Everything You Need to Start {}",
    "The Secrets Behind {}",
    "How {} Can Transform Your Life",
    "The Evolution of {}: A Historical Perspective",
    "Understanding {}: An In-Depth Analysis",
    "The Future of {} in Technology",
    "Common Mistakes to Avoid with {}",
    "Best Practices for {}",
    "How {} Can Boost Your Career",
    "Expert Opinions on {}",
    "The Essential Guide to {}",
    "How to Succeed in {}: Proven Strategies",
    "A Comprehensive Overview of {}: What You Need to Know",
    "Unlocking the Secrets of {}: Expert Advice",
    "{}: Key Techniques for Effective Results",
    "The Ultimate Guide to Mastering {}",
    "{}: Essential Tips and Best Practices",
    "How to Navigate the Challenges of {}",
    "The Benefits of {}: What Experts Say",
    "The Impact of {} on Daily Life",
    "{}: How to Get Started",
    "Advanced Concepts in {}: A Detailed Guide",
    "Understanding the Basics of {}: A Primer",
    "{}: Trends and Predictions for the Future",
    "How to Excel in {}: A Step-by-Step Guide",
    "{}: Common Pitfalls and How to Avoid Them",
    "The Evolution of {}: Past, Present, and Future",
    "How to Make the Most of {}: Practical Tips",
    "{}: Key Innovations and Developments",
    "Essential Skills for Mastering {}",
    "The Importance of {} in Modern Times",
    "How {} is Changing the Way We Live",
    "Exploring {}: Key Concepts and Ideas",
    "The Future of {}: What to Expect",
    "{}: Strategies for Long-Term Success",
    "How to Thrive in {}: Expert Insights",
    "Effective {} Strategies for Modern Challenges",
    "Unlocking the Potential of {}: A Comprehensive Guide",
    "Understanding {}: Key Concepts and Applications",
    "Navigating the World of {}: Tips and Tricks",
    "{} for Beginners: A Step-by-Step Approach",
    "{}: Best Practices and Case Studies",
    "The Essentials of {}: What Every Professional Should Know",
    "How to Achieve Excellence in {}",
    "{}: From Fundamentals to Advanced Techniques",
    "The Impact of {} on Industry Trends",
    "How to Build a Successful {} Strategy",
    "{}: Key Factors for Success",
    "Harnessing the Power of {}: Practical Advice",
    "Exploring the Benefits and Challenges of {}",
    "{}: What You Need to Know to Stay Ahead",
    "The Role of {} in Shaping the Future",
    "{}: Key Insights from Industry Leaders",
    "How to Implement Effective {} Solutions",
    "{}: The Path to Innovation and Growth",
    "The Most Common Misconceptions About Water and How to Avoid Them",
    "Understanding the Role of {} in Today's World",
    "{}: Proven Methods for Effective Implementation",
    "The Future of {}: Opportunities and Challenges",
    "How to Master {}: A Comprehensive Resource",
    "The Influence of {} on Modern Practices",
    "Key Considerations for Effective {} Management",
    "The Strategic Advantage of {}: Insights and Implications",
    "Elevating Your {} Strategy: Key Tactics for Excellence",
    "Maximizing Impact with {}: Advanced Methods and Practices",
    "The Paradigm Shift in {}: Revolutionary Approaches and Techniques",
    "Optimizing Performance with {}: Cutting-Edge Innovations",
    "Advanced Analytics in {}: Transforming Data into Actionable Insights",
    "Leveraging {} for Competitive Edge: Best Practices and Case Studies",
    "Redefining {}: Breakthrough Strategies for the Modern Era",
    "{} in the Digital Age: Harnessing Technology for Superior Outcomes",
    "The Art and Science of {}: Combining Creativity with Data-Driven Insights",
    "Enhancing {} through Strategic Planning and Execution",
    "The Evolution of {}: Historical Context and Future Trends",
    "Driving Success with {}: Leadership, Vision, and Innovation",
    "Harnessing the Power of {}: Advanced Tools and Techniques",
    "The Comprehensive Playbook for Mastering {}",
    "Navigating the Complexities of {}: Expert Guidance and Solutions",
    "Innovative Solutions for {}: Leading the Way in Industry",
    "Strategic Insights into {}: Lessons from Industry Leaders",
    "Empowering Your Organization with {}: A Blueprint for Success",
    "The Future-Proof Strategy for {}: Preparing for Tomorrow's Challenges",
    "Transforming {}: Integrating Advanced Technologies and Processes",
    "The Ultimate Guide to Scaling {}: Best Practices and Pitfalls to Avoid",
    "Unlocking New Opportunities in {}: Emerging Trends and Strategies",
    "Achieving Excellence in {}: Key Metrics and Performance Indicators",
    "The Leadership Guide to {}: Driving Change and Innovation",
    "Strategic Vision for {}: Long-Term Planning and Execution",
    "Revolutionizing {} with Disruptive Technologies and Innovations",
    "The Advanced Practitioner's Guide to {}: Techniques and Insights",
    "{} Best Practices: Proven Methods and Techniques for Success",
    "Understanding the Impact of {} on Global Markets and Industries",
    "Accelerating Growth with {}: Strategies for Market Leaders",
    "Developing a Robust {} Framework: Key Components and Implementation Steps",
    "Pioneering Advances in {}: From Concept to Market Adoption",
    "Strategic Approaches to {}: Balancing Risk and Reward",
    "Innovative Models for {}: Redefining Success in the Modern World",
    "High-Impact Strategies for Optimizing {} in Your Organization",
    "Future Trends in {}: Predictive Analysis and Strategic Forecasting",
    "Integrating {} into Your Business Strategy: Key Considerations and Tactics",
    "Leading the Way in {}: Innovations, Trends, and Best Practices"
    "Unlocking Opportunities in {}",
    "The Key Benefits of {}",
    "How to Enhance Your Skills in {}",
    "Expert Advice on Mastering {}",
    "The Essential Toolkit for {}",
    "How to Use {} Effectively",
    "The Latest Innovations in {}",
    "Understanding {}: Key Concepts and Ideas",
    "How to Achieve Mastery in {}",
    "The Complete Resource for {}",
    "How {} Can Improve Your Workflow",
    "Essential Techniques for Excelling in {}",
    "The Comprehensive Overview of {}",
    "Why {} is Essential for Your Success",
    "How to Implement {} in Your Projects",
    "Key Insights into the World of {}",
    "How to Overcome Challenges in {}",
    "The Importance of {} in Today's World",
    "How to Master {}: Key Strategies",
    "The Role of {} in Your Success",
    "How {} Can Transform Your Approach",
    "The Key Components of {}",
    "Understanding the Basics of {}",
    "Advanced Techniques for {}",
    "The Essential Guide to {}",
    "How to Get Ahead with {}",
    "Key Factors for Success in {}",
    "How to Excel at {}: Expert Tips",
    "Mastering the Basics of {}",
    "How to Implement {} Successfully",
    "The Comprehensive Guide to {}: From Start to Finish",
    "How to Succeed in {}",
    "The Future of {}: Trends and Predictions",
    "How to Master {}: A Step-by-Step Guide",
    "Key Strategies for Success in {}",
    "The Role of {} in Your Career",
    "How to Improve Your {} Skills",
    "The Complete Guide to {}: Everything You Need",
    "How to Master {}: Best Practices",
    "Understanding the Essentials of {}",
    "How to Achieve Success with {}",
    "The Ultimate Resource for {}",
    "How to Leverage {} for Success",
    "The Key Principles of {}",
    "How to Navigate the Challenges of {}",
    "Understanding {}: A Comprehensive Overview",
    "How to Implement Effective {} Strategies",
    "The Essential Skills for {}",
    "How to Succeed with {}",
    "Understanding the Impact of {}",
    "The Ultimate Guide to Succeeding in {}",
    "How to Optimize Your {} Skills",
    "Understanding the Core Concepts of {}",
    "How to Master the Fundamentals of {}",
    "Key Techniques for Mastering {}",
    "How to Excel in the Field of {}",
    "Mastering {}: Advanced Tips and Tricks",
    "The Ultimate Guide to Understanding {}",
    "How to Navigate the Complexities of {}",
    "The Key Elements of {}",
    "How to Improve Your Understanding of {}",
    "Understanding the Nuances of {}",
    "How to Master {} for Success",
    "The Essential Techniques for Succeeding in {}",
    "How to Achieve Mastery in the Field of {}",
    "Understanding the Key Aspects of {}",
    "The Ultimate Guide to Excelling in {}",
    "How to Leverage {} for Your Benefit",
    "Mastering the Essentials of {}",
    "How to Navigate {} Successfully",
    "Understanding the Impact of {} on Your Work",
    "How to Master {} in Simple Steps",
    "The Key Strategies for Succeeding in {}",
    "How to Overcome Challenges in the Field of {}",
    "Mastering {}: Key Concepts and Techniques",
    "How to Excel in {}: A Comprehensive Guide",
    "The Essential Guide to Excelling in {}",
    "How to Navigate the World of {} Successfully",
    "Understanding the Key Concepts of {}",
    "How to Achieve Success in the Field of {}",
    "The Ultimate Guide to Mastering {}",
    "How to Leverage the Power of {}",
    "Mastering the Art and Science of {}",
    "How to Navigate the Challenges of {} Successfully",
    "The Key Elements for Success in {}",
    "How to Improve Your Skills in the Field of {}",
    "Understanding the Fundamentals of Succeeding in {}",
    "How to Excel at {}: A Complete Guide",
    "The Essential Guide to Mastering the Art of {}",
    "How to Achieve Excellence in the Field of {}",
    "Mastering {}: A Step-by-Step Guide",
    "How to Navigate the Complexities of {} Effectively",
    "Understanding the Key Elements of Success in {}",
    "How to Master {} for Optimal Results",
    "Mastering the Essential Techniques of {}",
    "How to Achieve Mastery in the World of {}",
    "Understanding the Importance of {} in Your Career",
    "The Ultimate Guide to Mastering the Fundamentals of {}",
    "How to Leverage {} for Career Success",
    "Mastering the Art of {}: Key Strategies and Techniques",
    "How to Overcome Challenges in {} for Success",
    "Understanding the Key Techniques for Excelling in {}",
    "How to Achieve Success in the World of {}",
    "The Essential Guide to Navigating {} Successfully",
    "How to Improve Your {} Techniques",
    "Mastering the Essentials of Success in {}",
    "How to Navigate the World of {} with Ease",
    "Understanding the Key Principles of Success in {}",
    "How to Master {} for Career Advancement",
    "Mastering {}: The Ultimate Guide to Success",
    "How to Achieve Excellence in {}: Key Strategies",
    "The Essential Guide to Mastering {}: Tips and Techniques",
    "How to Navigate the Complexities of {}: A Comprehensive Guide",
    "Understanding the Core Elements of Success in {}",
    "How to Excel in the World of {}: Key Tips and Strategies",
    "Mastering the Art of {}: Essential Techniques for Success",
    "How to Achieve Mastery in {}: A Step-by-Step Approach",
    "Understanding the Key Concepts of Success in {}",
    "How to Leverage {} for Maximum Success",
    "Mastering {}: The Comprehensive Guide",
    "How to Navigate the Challenges of {}: Expert Advice",
    "Understanding the Fundamentals of Success in {}",
    "How to Excel in the Field of {}: A Complete Guide",
    "Mastering {}: Essential Techniques and Strategies",
    "How to Achieve Excellence in {}: Proven Methods",
    "The Ultimate Guide to Mastering the Art of {}",
    "How to Navigate the Complexities of {}: Key Insights",
    "Understanding the Core Concepts of {}: A Comprehensive Guide",
    "How to Achieve Success in the World of {}: Expert Tips",
    "Mastering {}: The Essential Guide to Success",
    "How to Leverage {} for Optimal Results",
    "Understanding the Key Elements of Success in {}",
    "How to Navigate the World of {}: A Complete Guide",
    "Mastering the Art of {}: Proven Techniques and Strategies",
    "How to Achieve Mastery in the Field of {}: Expert Advice",
    "Understanding the Importance of {} for Success",
    "How to Excel in {}: A Step-by-Step Guide",
    "Mastering {}: The Ultimate Resource for Success",
    "How to Navigate the Challenges of {}: Practical Tips",
    "Understanding the Core Principles of {}: A Comprehensive Guide",
    "How to Achieve Success in {}: Proven Strategies",
    "Mastering the Art and Science of {}: Key Insights",
    "How to Navigate the Complexities of {} Successfully",
    "Understanding the Fundamentals of {}: A Complete Guide",
    "How to Excel in the World of {}: Key Techniques",
    "Mastering the Essentials of {}: Proven Strategies",
    "How to Achieve Excellence in {}: Expert Advice",
    "The Ultimate Guide to Mastering {}: Tips and Tricks",
    "How to Navigate the Challenges of {}: Essential Advice",
    "Understanding the Core Elements of {}: A Comprehensive Guide",
    "How to Achieve Success in the Field of {}: Key Insights",
    "Mastering {}: The Essential Resource for Success",
    "How to Leverage the Power of {} for Success",
    "Understanding the Key Principles of {}: A Complete Guide",
    "How to Navigate the World of {}: Expert Tips and Techniques",
    "Mastering the Art of {}: A Step-by-Step Guide",
    "How to Achieve Mastery in the World of {}: Proven Methods",
]

templates_hindi = [
    "{} के लिए उन्नत रणनीतियाँ: सफलता के रहस्य",
    "{} को समझने के लिए गहन विश्लेषण",
    "कैसे {} [उद्योग/क्षेत्र] में क्रांति ला रहा है: प्रमुख विकास",
    "[लक्ष्य] को प्राप्त करने के लिए {} का लाभ उठाने के लिए विशेषज्ञ रणनीतियाँ",
    "कैसे {} [वर्तमान प्रवृत्ति या घटना] को प्रभावित कर रहा है",
    "विघटनकारी प्रौद्योगिकियों और नवाचारों के साथ {} में क्रांति लाना",
    "{} के बारे में आम भ्रांतियाँ और उन्हें कैसे दूर करें",
    "{} को मास्टर करने के लिए चरण-दर-चरण दृष्टिकोण",
    "{} के लिए आवश्यक उपकरण किट",
    "{} की शक्ति को अनलॉक करना: मुख्य अंतर्दृष्टि",
    "{} में नवाचार: उभरती तकनीकें और अंतर्दृष्टि",
    "{} का भविष्य: पूर्वानुमान और रुझान",
    "{} में माहिर कैसे बनें",
    "{} पर गहन विश्लेषण: फायदे और नुकसान",
    "{} के बारे में जानने योग्य शीर्ष रुझान",
    "{} की भूमिका: मुख्य घटनाक्रम",
    "{} के बारे में विशेषज्ञ की राय",
    "{} को कैसे समझें",
    "{} में {} का प्रभाव",
    "{} के साथ अपने परिणामों को अधिकतम कैसे करें",
    "{} को समझने के लिए आवश्यक अंतर्दृष्टि",
    "{}:सच्चाई और मिथक",
    "{}:शुरुआती गाइड",
    "{} के लिए अभिनव दृष्टिकोण: उभरती तकनीकें और अंतर्दृष्टि",
    "{} के लिए पूर्ण गाइड",
    "{} में सफल कैसे हों: सिद्ध रणनीतियाँ",
    "{} की व्यापक समीक्षा: आपको क्या जानना चाहिए",
    "{} के रहस्यों को अनलॉक करना: विशेषज्ञ सलाह",
    "{}: प्रभावी परिणामों के लिए प्रमुख तकनीकें",
    "{} में मास्टर करने के लिए अंतिम मार्गदर्शिका",
    "{}: आवश्यक सुझाव और सर्वोत्तम प्रथाएँ",
    "{} की चुनौतियों को कैसे नेविगेट करें",
    "{} के लाभ: विशेषज्ञ क्या कहते हैं",
    "{} का दैनिक जीवन पर प्रभाव",
    "{}: शुरुआत कैसे करें",
    "{} में उन्नत अवधारणाएँ: विस्तृत मार्गदर्शिका",
    "{} के मूल बातें: एक प्रारंभिक दृष्टिकोण",
    "{}: भविष्य के लिए रुझान और भविष्यवाणियाँ",
    "{} में सफल कैसे हों: एक चरण-दर-चरण गाइड",
    "{}: सामान्य नुकसान और उनसे कैसे बचें",
    "{} का विकास: अतीत, वर्तमान, और भविष्य",
    "{} को सबसे अच्छा कैसे बनाएं: व्यावहारिक सुझाव",
    "{}: प्रमुख नवाचार और विकास",
    "मास्टरिंग {}: एक व्यापक संसाधन",
    "{} का आधुनिक प्रथाओं पर प्रभाव",
    "{} प्रबंधन के लिए प्रमुख विचार",
    "{} का रणनीतिक लाभ: अंतर्दृष्टि और निहितार्थ",
    "{} रणनीति को ऊंचा उठाना: उत्कृष्टता के लिए प्रमुख रणनीतियाँ",
    "{} के साथ प्रभाव अधिकतम करना: उन्नत विधियाँ और प्रथाएँ",
    "{} में पैटर्न बदलाव: क्रांतिकारी दृष्टिकोण और तकनीकें",
    "{} के साथ प्रदर्शन को अनुकूलित करना: अग्रणी नवाचार",
    "{} में उन्नत विश्लेषण: डेटा को क्रियात्मक अंतर्दृष्टियों में बदलना",
    "{} के लिए प्रतिस्पर्धात्मक लाभ प्राप्त करना: सर्वोत्तम प्रथाएँ और केस स्टडी",
    "{} को फिर से परिभाषित करना: आधुनिक युग के लिए ब्रेकथ्रू रणनीतियाँ",
    "{} के डिजिटल युग में: श्रेष्ठ परिणामों के लिए प्रौद्योगिकी का उपयोग",
    "{} की कला और विज्ञान: रचनात्मकता को डेटा-संचालित अंतर्दृष्टियों के साथ मिलाना",
    "{} को रणनीतिक योजना और निष्पादन के माध्यम से सुधारना",
    "{} का विकास: ऐतिहासिक संदर्भ और भविष्य की प्रवृत्तियाँ",
    "{} के साथ सफलता प्राप्त करना: नेतृत्व, दृष्टि, और नवाचार",
    "{} की शक्ति को अनलॉक करना: उन्नत उपकरण और तकनीकें",
    "{} के लिए पूर्ण खेलपुस्तक",
    "{} की जटिलताओं को नेविगेट करना: विशेषज्ञ मार्गदर्शन और समाधान",
    "{} में रणनीतिक अंतर्दृष्टि: उद्योग के नेताओं से सबक",
    "अपने संगठन को {} के साथ सशक्त बनाना: सफलता के लिए एक ब्लूप्रिंट",
    "{} के भविष्य-प्रूफ रणनीति: कल की चुनौतियों के लिए तैयारी",
    "{} को बदलना: उन्नत प्रौद्योगिकियों और प्रक्रियाओं का एकीकरण",
    "{} को स्केल करने के लिए पूर्ण गाइड: सर्वोत्तम प्रथाएँ और नुकसान",
    "{} में नए अवसरों को अनलॉक करना: उभरती प्रवृत्तियाँ और रणनीतियाँ",
    "{} में उत्कृष्टता प्राप्त करना: प्रमुख मैट्रिक्स और प्रदर्शन संकेतक",
    "{} में नेतृत्व गाइड: परिवर्तन और नवाचार",
    "{} के लिए रणनीतिक दृष्टिकोण: दीर्घकालिक योजना और निष्पादन",
    "{} को विघटनकारी प्रौद्योगिकियों और नवाचारों के साथ क्रांतिकारी बनाना",
    "{} के उन्नत प्रैक्टिशनर की गाइड: तकनीकें और अंतर्दृष्टि",
    "{} सर्वोत्तम प्रथाएँ: सफलता के लिए सिद्ध तरीके और तकनीकें",
    "वैश्विक बाजारों और उद्योगों पर {} के प्रभाव को समझना",
    "{} के साथ विकास को तेज करना: बाजार के नेताओं के लिए रणनीतियाँ",
    "{} ढांचे को मजबूत करना: प्रमुख घटक और कार्यान्वयन कदम",
    "{} में अग्रणी प्रगति: अवधारणा से बाजार अपनाने तक",
    "{} में रणनीतिक दृष्टिकोण: जोखिम और लाभ का संतुलन",
    "{} के लिए नवाचारी मॉडल: आधुनिक दुनिया में सफलता की पुनर्परिभाषा",
    "आपकी संगठन में {} को उच्च प्रभावी रणनीतियाँ: प्रमुख रणनीतियाँ",
    "{} में भविष्यवाणी और रणनीतिक पूर्वानुमान: भविष्य के रुझान",
    "{} को आपके व्यावसायिक रणनीति में एकीकृत करना: प्रमुख विचार और रणनीतियाँ",
    "{} में मार्गदर्शक: नवाचार, रुझान, और सर्वोत्तम प्रथाएँ"
    "{} के बारे में आम भ्रांतियाँ और उन्हें कैसे दूर करें",
    "{} को मास्टर करने के लिए चरण-दर-चरण दृष्टिकोण",
    "{} के लिए आवश्यक उपकरण और संसाधन",
    "{} की शक्ति को अनलॉक करना: मुख्य अंतर्दृष्टि",
    "{} में नवाचार: उभरती प्रौद्योगिकियाँ और अंतर्दृष्टि",
    "{} का भविष्य: पूर्वानुमान और रुझान",
    "{} में मास्टर कैसे बनें",
    "{} पर गहन विश्लेषण: फायदे और नुकसान",
    "{} के बारे में जानने योग्य शीर्ष रुझान",
    "{} की भूमिका: प्रमुख विकास",
    "{} के बारे में विशेषज्ञ की राय",
    "{} में {} का प्रभाव",
    "{} के साथ अपने परिणामों को अधिकतम कैसे करें",
    "{} को समझने के लिए आवश्यक अंतर्दृष्टि",
    "{}: सच्चाई और मिथक",
    "{} को स्केल करने के लिए पूर्ण गाइड: सर्वोत्तम प्रथाएँ और नुकसान",
    "{} में नए अवसरों को अनलॉक करना: उभरती प्रवृत्तियाँ और रणनीतियाँ",
    "{} में उत्कृष्टता प्राप्त करना: प्रमुख मैट्रिक्स और प्रदर्शन संकेतक",
    "{} में नेतृत्व गाइड: परिवर्तन और नवाचार",
    "{} के लिए रणनीतिक दृष्टिकोण: दीर्घकालिक योजना और निष्पादन",
    "{} को विघटनकारी प्रौद्योगिकियों और नवाचारों के साथ क्रांतिकारी बनाना",
    "{} के उन्नत प्रैक्टिशनर की गाइड: तकनीकें और अंतर्दृष्टि",
    "{} सर्वोत्तम प्रथाएँ: सफलता के लिए सिद्ध तरीके और तकनीकें",
    "वैश्विक बाजारों और उद्योगों पर {} के प्रभाव को समझना",
    "{} के साथ विकास को तेज करना: बाजार के नेताओं के लिए रणनीतियाँ",
    "{} ढांचे को मजबूत करना: प्रमुख घटक और कार्यान्वयन कदम",
    "{} में अग्रणी प्रगति: अवधारणा से बाजार अपनाने तक",
    "{} में रणनीतिक दृष्टिकोण: जोखिम और लाभ का संतुलन",
    "{} के लिए नवाचारी मॉडल: आधुनिक दुनिया में सफलता की पुनर्परिभाषा",
]

generated_titles = {}

def generate_unique_titles(keywords, language):
    keywords_list = keywords.split(', ')

    if not keywords_list:
        return ["No suitable title can be generated."] * 4

    if language == "Hindi":
        templates = templates_hindi
    elif language == "English":
        templates = templates_english
    else:
        return ["Invalid language selected."] * 4

    # Generate unique titles
    unique_titles = set()
    while len(unique_titles) < 4:
        if (keywords, language) in generated_titles and len(generated_titles[(keywords, language)]) >= len(templates):
            # Reset if all titles have been used
            generated_titles[(keywords, language)] = []

        title = random.choice([template for template in templates if '{}' in template])
        title = title.format(keywords_list[0])
        
        if title not in unique_titles:
            unique_titles.add(title)
            if (keywords, language) in generated_titles:
                generated_titles[(keywords, language)].append(title)
            else:
                generated_titles[(keywords, language)] = [title]
    
    return list(unique_titles)

class TitleGeneratorGUI(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Title Generator')
        self.setGeometry(100, 100, 600, 400)

        # Set the overall background color
        self.setStyleSheet("background-color: #FFDFDD;")

        layout = QVBoxLayout()

        # Update the label style
        self.title_label = QLabel('SAARTHI : Title Generator', self)
        self.title_label.setStyleSheet("font-size: 30px; font-weight: bold; color: white; background-color: #a278f5; padding: 10px;")
        layout.addWidget(self.title_label)

        self.language_combo = QComboBox(self)
        self.language_combo.addItems(["Hindi", "English"])
        self.language_combo.setStyleSheet("font-size: 18px;")
        layout.addWidget(self.language_combo)

        self.keywords_input = QLineEdit(self)
        self.keywords_input.setPlaceholderText('Enter keywords separated by commas')
        self.keywords_input.setStyleSheet("font-size: 18px;")
        layout.addWidget(self.keywords_input)

        self.generate_button = QPushButton('Generate Titles', self)
        self.generate_button.setCursor(Qt.PointingHandCursor)
        self.generate_button.clicked.connect(self.generate_titles)
        self.generate_button.setStyleSheet("font-size: 18px; background-color: #4CAF50; color: white; padding: 10px; border-radius: 5px;")
        layout.addWidget(self.generate_button)

        self.result_box = QTextEdit(self)
        self.result_box.setReadOnly(True)
        self.result_box.setStyleSheet("font-size: 18px;")
        layout.addWidget(self.result_box)

        self.setLayout(layout)

    def generate_titles(self):
        language = self.language_combo.currentText()
        keywords = self.keywords_input.text()

        if not keywords:
            self.result_box.setText("Please enter keywords.")
            return

        titles = generate_unique_titles(keywords, language)
        self.result_box.setText('\n'.join(f"• {title}" for title in titles))

def generate_unique_titles(keywords, language):
    # This is a placeholder function for generating titles. Replace with your actual implementation.
    return [f"Title based on {keywords} in {language}"]

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = TitleGeneratorGUI()
    ex.show()
    sys.exit(app.exec_())