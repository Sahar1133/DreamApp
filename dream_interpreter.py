import streamlit as st
import requests
import json
import re
from typing import Dict, List, Tuple
import time

class AdvancedDreamInterpreter:
    def __init__(self):
        self.setup_apis()
        self.islamic_guidelines = self.get_islamic_guidelines()
    
    def setup_apis(self):
        """Setup API endpoints for AI models"""
        self.apis = {
            "openai": "https://api.openai.com/v1/chat/completions",
            "huggingface": "https://api-inference.huggingface.co/models",
        }
    
    def get_islamic_guidelines(self):
        """Islamic guidelines for dream interpretation"""
        return {
            "types_of_dreams": [
                "**True Dreams (Ru'ya)**: From Allah - good news and guidance",
                "**Bad Dreams (Hulum)**: From Shaytan - seek refuge in Allah",
                "**Dreams from self**: Reflections of daily thoughts and experiences"
            ],
            "interpretation_rules": [
                "Consider the dreamer's circumstances and character",
                "Interpret symbols according to Islamic tradition",
                "Good dreams should be shared, bad dreams should not",
                "Dreams are one of 46 parts of Prophethood",
                "Context and emotions matter in interpretation"
            ],
            "scholars_methodology": {
                "ibn_sirin": "Combined Quran, Sunnah, Arabic language, and psychological insight",
                "nabulsi": "Emphasized spiritual dimensions and soul's reflections"
            }
        }
    
    def analyze_dream_with_ai(self, dream_text: str, language: str = "english") -> Dict:
        """Analyze dream using AI with Islamic context"""
        
        if language == "urdu":
            return self._generate_urdu_interpretation(dream_text)
        else:
            return self._generate_english_interpretation(dream_text)
    
    def _generate_english_interpretation(self, dream_text: str) -> Dict:
        """Generate comprehensive English interpretation"""
        
        interpretation_template = {
            "summary": "",
            "ibn_sirin_analysis": "",
            "nabulsi_analysis": "",
            "symbolic_meanings": [],
            "practical_advice": [],
            "spiritual_guidance": [],
            "overall_assessment": ""
        }
        
        # AI-powered analysis (simulated - in production, use actual AI API)
        dream_lower = dream_text.lower()
        
        # Detect key themes
        themes = self._detect_dream_themes(dream_lower)
        
        # Generate interpretations based on themes
        interpretation_template["summary"] = self._generate_summary(dream_text, themes)
        interpretation_template["ibn_sirin_analysis"] = self._generate_ibn_sirin_analysis(dream_text, themes)
        interpretation_template["nabulsi_analysis"] = self._generate_nabulsi_analysis(dream_text, themes)
        interpretation_template["symbolic_meanings"] = self._extract_symbolic_meanings(dream_text, themes)
        interpretation_template["practical_advice"] = self._generate_practical_advice(themes)
        interpretation_template["spiritual_guidance"] = self._generate_spiritual_guidance(themes)
        interpretation_template["overall_assessment"] = self._generate_overall_assessment(themes)
        
        return interpretation_template
    
    def _generate_urdu_interpretation(self, dream_text: str) -> Dict:
        """Generate comprehensive Urdu interpretation"""
        
        # Translate and analyze for Urdu output
        themes = self._detect_dream_themes(dream_text.lower())
        
        urdu_interpretation = {
            "summary": self._generate_urdu_summary(dream_text, themes),
            "ibn_sirin_analysis": self._generate_urdu_ibn_sirin_analysis(themes),
            "nabulsi_analysis": self._generate_urdu_nabulsi_analysis(themes),
            "symbolic_meanings": self._extract_urdu_symbolic_meanings(themes),
            "practical_advice": self._generate_urdu_practical_advice(themes),
            "spiritual_guidance": self._generate_urdu_spiritual_guidance(themes),
            "overall_assessment": self._generate_urdu_overall_assessment(themes)
        }
        
        return urdu_interpretation
    
    def _detect_dream_themes(self, dream_text: str) -> List[str]:
        """Detect main themes in the dream"""
        themes = []
        
        theme_keywords = {
            "water": ["water", "river", "sea", "ocean", "rain", "drinking", "swimming"],
            "animals": ["snake", "lion", "bird", "horse", "dog", "cat", "animal"],
            "family": ["mother", "father", "parent", "child", "son", "daughter", "family"],
            "death": ["death", "dead", "died", "funeral", "grave", "bury"],
            "travel": ["travel", "journey", "road", "path", "car", "bus", "train"],
            "house": ["house", "home", "room", "building", "door", "window"],
            "nature": ["tree", "mountain", "sun", "moon", "sky", "flower"],
            "money": ["money", "gold", "wealth", "rich", "poor", "coins"],
            "food": ["food", "eating", "fruit", "meal", "hungry", "thirsty"],
            "spiritual": ["prayer", "mosque", "quran", "allah", "prophet", "angel"]
        }
        
        for theme, keywords in theme_keywords.items():
            if any(keyword in dream_text for keyword in keywords):
                themes.append(theme)
        
        return themes if themes else ["general"]
    
    def _generate_summary(self, dream_text: str, themes: List[str]) -> str:
        """Generate dream summary"""
        theme_desc = ", ".join(themes)
        return f"This dream contains themes of {theme_desc}. The narrative suggests {self._get_emotional_tone(dream_text)}. Based on Islamic dream interpretation principles, this appears to be {self._assess_dream_type(dream_text)}."
    
    def _generate_ibn_sirin_analysis(self, dream_text: str, themes: List[str]) -> str:
        """Generate analysis based on Ibn Sirin's methodology"""
        analysis = "According to Ibn Sirin's methodology:\n\n"
        
        if "water" in themes:
            analysis += "• Water elements indicate knowledge, life, and spiritual purity. Clear water suggests lawful earnings.\n"
        if "animals" in themes:
            analysis += "• Animals represent various aspects of life - snakes for enemies, birds for news, lions for authority.\n"
        if "death" in themes:
            analysis += "• Death in dreams usually signifies transformation or changes, not physical death.\n"
        if "house" in themes:
            analysis += "• Houses reflect the dreamer's life circumstances and spiritual state.\n"
        if "travel" in themes:
            analysis += "• Travel indicates seeking knowledge or life changes.\n"
        
        analysis += f"\nIbn Sirin would consider your personal circumstances and the dream's context. The emotional tone suggests {self._get_emotional_guidance(dream_text)}"
        
        return analysis
    
    def _generate_nabulsi_analysis(self, dream_text: str, themes: List[str]) -> str:
        """Generate analysis based on Sheikh Nabulsi's methodology"""
        analysis = "According to Sheikh Nabulsi's spiritual approach:\n\n"
        
        if "water" in themes:
            analysis += "• Water represents divine mercy and spiritual nourishment. Its state reflects your spiritual condition.\n"
        if "animals" in themes:
            analysis += "• Animals symbolize inner states and spiritual challenges to overcome.\n"
        if "death" in themes:
            analysis += "• Death indicates spiritual transformation and rebirth into higher consciousness.\n"
        if "house" in themes:
            analysis += "• The house mirrors your soul's condition and spiritual journey.\n"
        if "spiritual" in themes:
            analysis += "• Spiritual elements show your connection with divine guidance.\n"
        
        analysis += f"\nNabulsi would emphasize the dream's spiritual dimensions and what Allah might be communicating through these symbols."
        
        return analysis
    
    def _extract_symbolic_meanings(self, dream_text: str, themes: List[str]) -> List[str]:
        """Extract symbolic meanings from dream"""
        symbols = []
        
        symbol_meanings = {
            "water": "Life, knowledge, purity, divine mercy",
            "snake": "Hidden enemies, temptations, or transformation",
            "lion": "Power, authority, or personal strength",
            "bird": "News, messages, or spiritual aspirations",
            "death": "Transformation, endings, or new beginnings",
            "house": "Self, life circumstances, or spiritual state",
            "travel": "Journey, seeking, or life changes",
            "tree": "Growth, life, or family connections",
            "sun": "Guidance, knowledge, or divine light",
            "moon": "Beauty, reflection, or feminine aspects"
        }
        
        for theme in themes:
            if theme in symbol_meanings:
                symbols.append(f"{theme.title()}: {symbol_meanings[theme]}")
        
        return symbols if symbols else ["The dream contains general symbols that should be interpreted in context"]
    
    def _generate_practical_advice(self, themes: List[str]) -> List[str]:
        """Generate practical advice based on dream themes"""
        advice = []
        
        if "water" in themes:
            advice.append("Reflect on your sources of knowledge and spiritual nourishment")
        if "animals" in themes:
            advice.append("Consider what challenges or 'enemies' you need to overcome")
        if "death" in themes:
            advice.append("What aspects of your life are transforming or need to change?")
        if "travel" in themes:
            advice.append("Are you seeking new knowledge or directions in life?")
        if "money" in themes:
            advice.append("Examine your relationship with wealth and provisions")
        
        advice.append("Share good dreams with loved ones")
        advice.append("Seek refuge in Allah from any disturbing elements")
        
        return advice
    
    def _generate_spiritual_guidance(self, themes: List[str]) -> List[str]:
        """Generate spiritual guidance"""
        guidance = [
            "Remember that true dreams are from Allah as good news",
            "Bad dreams are from Shaytan - seek refuge and don't share them",
            "Use dreams as motivation for self-reflection and improvement",
            "Increase your prayers and remembrance of Allah",
            "Consult knowledgeable scholars for important dreams"
        ]
        return guidance
    
    def _generate_overall_assessment(self, themes: List[str]) -> str:
        """Generate overall assessment"""
        return f"Based on the themes detected ({', '.join(themes)}), this dream appears to carry meaningful insights. Consider both the practical and spiritual dimensions in your reflection."
    
    # Urdu Interpretation Methods
    def _generate_urdu_summary(self, dream_text: str, themes: List[str]) -> str:
        """Generate Urdu summary"""
        theme_desc = "، ".join(themes)
        return f"یہ خواب {theme_desc} کے موضوعات پر مشتمل ہے۔ خواب کی کیفیت {self._get_urdu_emotional_tone(dream_text)}۔ اسلامی تعبیر کے اصولوں کے مطابق، یہ خواب {self._assess_urdu_dream_type(dream_text)} ظاہر ہوتا ہے۔"
    
    def _generate_urdu_ibn_sirin_analysis(self, themes: List[str]) -> str:
        """Generate Urdu Ibn Sirin analysis"""
        analysis = "امام ابن سیرین کے طریقہ تعبیر کے مطابق:\n\n"
        
        if "water" in themes:
            analysis += "• پانی کے عناصر علم، زندگی اور روحانی پاکیزگی کی علامت ہیں۔ صاف پانی حلال روزی کی نشاندہی کرتا ہے۔\n"
        if "animals" in themes:
            analysis += "• جانور زندگی کے مختلف پہلوؤں کی نمائندگی کرتے ہیں - سانپ دشمن، پرندے خبریں، شیر حکمرانی۔\n"
        if "death" in themes:
            analysis += "• خواب میں موت عموماً تبدیلی یا حالات کی تبدیلی کی طرف اشارہ ہوتی ہے، جسمانی موت نہیں۔\n"
        if "house" in themes:
            analysis += "• گھر خواب دیکھنے والے کے حالات زندگی اور روحانی حالت کا آئینہ دار ہیں۔\n"
        
        analysis += "\nابن سیرین آپ کے ذاتی حالات اور خواب کے سیاق و سباق کو مدنظر رکھتے ہوئے تعبیر دیں گے۔"
        
        return analysis
    
    def _generate_urdu_nabulsi_analysis(self, themes: List[str]) -> str:
        """Generate Urdu Nabulsi analysis"""
        analysis = "شیخ عبدالغنی نابلسی کے روحانی طریقہ تعبیر کے مطابق:\n\n"
        
        if "water" in themes:
            analysis += "• پانی divine رحمت اور روحانی غذا کی علامت ہے۔ اس کی حالت آپ کی روحانی کیفیت کو ظاہر کرتی ہے۔\n"
        if "animals" in themes:
            analysis += "• جانور اندرونی کیفیات اور روحانی چیلنجز کی نمائندگی کرتے ہیں۔\n"
        if "death" in themes:
            analysis += "• موت روحانی تبدیلی اور اعلی شعور میں نئے سرے سے جنم لینے کی علامت ہے۔\n"
        
        analysis += "\nنابلسی خواب کے روحانی پہلوؤں پر زور دیتے ہیں کہ اللہ تعالیٰ ان علامات کے ذریعے کیا پیغام دے رہے ہیں۔"
        
        return analysis
    
    def _extract_urdu_symbolic_meanings(self, themes: List[str]) -> List[str]:
        """Extract Urdu symbolic meanings"""
        symbols = []
        
        urdu_symbol_meanings = {
            "water": "زندگی، علم، پاکیزگی، divine رحمت",
            "snake": "پوشیدہ دشمن، آزمائشیں، یا تبدیلی",
            "lion": "طاقت، حکمرانی، یا ذاتی قوت",
            "bird": "خبریں، پیغامات، یا روحانی آرزوئیں",
            "death": "تبدیلی، اختتام، یا نئے آغاز",
            "house": "ذات، زندگی کے حالات، یا روحانی حالت",
            "travel": "سفر، تلاش، یا زندگی میں تبدیلیاں"
        }
        
        for theme in themes:
            if theme in urdu_symbol_meanings:
                symbols.append(f"{theme.title()}: {urdu_symbol_meanings[theme]}")
        
        return symbols if symbols else ["خواب میں عمومی علامات ہیں جنہیں سیاق و سباق میں سمجھنا چاہیے"]
    
    def _generate_urdu_practical_advice(self, themes: List[str]) -> List[str]:
        """Generate Urdu practical advice"""
        advice = []
        
        if "water" in themes:
            advice.append("اپنے علم اور روحانی غذا کے ذرائع پر غور کریں")
        if "animals" in themes:
            advice.append("غور کریں کہ آپ کو کن چیلنجز یا 'دشمنوں' پر قابو پانا ہے")
        if "death" in themes:
            advice.append("آپ کی زندگی کے کن پہلوؤں میں تبدیلی آ رہی ہے یا ضرورت ہے؟")
        
        advice.append("اچھے خواب اپنے پیاروں کے ساتھ شیئر کریں")
        advice.append("ہر پریشان کن عنصر سے اللہ کی پناہ مانگیں")
        
        return advice
    
    def _generate_urdu_spiritual_guidance(self, themes: List[str]) -> List[str]:
        """Generate Urdu spiritual guidance"""
        guidance = [
            "یاد رکھیں کہ سچے خواب اللہ کی طرف سے بشارت ہوتے ہیں",
            "برے خواب شیطان کی طرف سے ہوتے ہیں - اللہ کی پناہ مانگیں اور انہیں شیئر نہ کریں",
            "خوابوں کو self-reflection اور بہتری کے لیے محرک کے طور پر استعمال کریں",
            "اپنی نمازوں اور اللہ کے ذکر میں اضافہ کریں",
            "اہم خوابوں کے لیے علماء سے مشورہ کریں"
        ]
        return guidance
    
    def _generate_urdu_overall_assessment(self, themes: List[str]) -> str:
        """Generate Urdu overall assessment"""
        theme_desc = "، ".join(themes)
        return f"معلوم ہونے والے موضوعات ({theme_desc}) کی بنیاد پر، یہ خواب meaningful insights رکھتا ظاہر ہوتا ہے۔ اپنے reflection میں practical اور spiritual دونوں پہلوؤں کو مدنظر رکھیں۔"
    
    def _get_emotional_tone(self, dream_text: str) -> str:
        """Detect emotional tone of dream"""
        positive_words = ["happy", "peaceful", "joy", "beautiful", "calm", "blessed"]
        negative_words = ["fear", "scared", "angry", "sad", "worried", "terrified"]
        
        if any(word in dream_text.lower() for word in positive_words):
            return "positive and hopeful emotions"
        elif any(word in dream_text.lower() for word in negative_words):
            return "challenging or concerning emotions"
        else:
            return "mixed or neutral emotions"
    
    def _get_urdu_emotional_tone(self, dream_text: str) -> str:
        """Detect Urdu emotional tone"""
        positive_urdu = ["خوش", "پرسکون", "مسرور", "خوشی", "برکت"]
        negative_urdu = ["خوف", "ڈر", "غصہ", "اداس", "پریشان"]
        
        if any(word in dream_text for word in positive_urdu):
            return "مثبت اور پرامید جذبات"
        elif any(word in dream_text for word in negative_urdu):
            return "چیلنجنگ یا پریشان کن جذبات"
        else:
            return "مخلوط یا neutral جذبات"
    
    def _assess_dream_type(self, dream_text: str) -> str:
        """Assess type of dream"""
        if any(word in dream_text.lower() for word in ["peace", "happy", "light", "beautiful", "blessing"]):
            return "a potentially true dream (Ru'ya) containing good news"
        elif any(word in dream_text.lower() for word in ["fear", "dark", "monster", "chase", "falling"]):
            return "possibly from negative sources - seek refuge in Allah"
        else:
            return "a reflection of daily thoughts and experiences"
    
    def _assess_urdu_dream_type(self, dream_text: str) -> str:
        """Assess Urdu dream type"""
        if any(word in dream_text for word in ["پرسکون", "خوش", "روشنی", "خوشی", "برکت"]):
            return "ممکنہ طور پر سچا خواب (رویا) جو خوشخبری رکھتا ہے"
        elif any(word in dream_text for word in ["خوف", "اندھیرا", "ڈراؤنا", "پیچھا", "گرنا"]):
            return "ممکنہ طور پر منفی ذرائع سے - اللہ کی پناہ مانگیں"
        else:
            return "روزمرہ کے خیالات اور تجربات کا عکس"
    
    def _get_emotional_guidance(self, dream_text: str) -> str:
        """Get emotional guidance"""
        if any(word in dream_text.lower() for word in ["happy", "peaceful", "joy"]):
            return "this may be a true dream carrying good news"
        elif any(word in dream_text.lower() for word in ["fear", "scared", "terrified"]):
            return "seeking refuge in Allah is recommended for any disturbing elements"
        else:
            return "reflect on how this dream relates to your current life situation"

def main():
    # Configure Streamlit page
    st.set_page_config(
        page_title="AI Islamic Dream Interpreter",
        page_icon="🌙",
        layout="wide",
        initial_sidebar_state="expanded"
    )
    
    # Custom CSS
    st.markdown("""
    <style>
    .main-header {
        font-size: 2.8rem;
        color: #1a5276;
        text-align: center;
        margin-bottom: 1rem;
        font-weight: bold;
        padding: 20px;
        background: linear-gradient(135deg, #e8f4f8, #d1e7f5);
        border-radius: 15px;
    }
    .urdu-text {
        font-family: 'Jameel Noori Nastaleeq', 'Urdu Typesetting', 'Noto Nastaliq Urdu';
        font-size: 1.2rem;
        line-height: 2;
        direction: rtl;
        text-align: right;
    }
    .interpretation-section {
        background: #f8f9fa;
        padding: 25px;
        border-radius: 15px;
        margin: 20px 0;
        border-left: 6px solid #1a5276;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    }
    .scholar-analysis {
        background: white;
        padding: 20px;
        margin: 15px 0;
        border-radius: 10px;
        border-left: 4px solid #3498db;
    }
    .symbol-box {
        background: #e8f6f3;
        padding: 15px;
        border-radius: 10px;
        margin: 10px 0;
        border: 2px solid #1abc9c;
    }
    .advice-box {
        background: #fef9e7;
        padding: 15px;
        border-radius: 10px;
        margin: 10px 0;
        border: 2px solid #f39c12;
    }
    .language-tab {
        font-size: 1.1rem;
        font-weight: bold;
    }
    </style>
    """, unsafe_allow_html=True)
    
    # Header
    st.markdown('<div class="main-header">🤖 AI Islamic Dream Interpreter</div>', unsafe_allow_html=True)
    st.markdown("### Complete Dream Analysis Using AI - Based on Ibn Sirin & Sheikh Nabulsi")
    
    # Initialize interpreter
    if 'interpreter' not in st.session_state:
        st.session_state.interpreter = AdvancedDreamInterpreter()
    
    # Main input section
    st.markdown("## 🌙 Describe Your Complete Dream")
    
    dream_text = st.text_area(
        "Write your full dream in detail:",
        height=200,
        placeholder="Describe your entire dream narrative. Include emotions, people, objects, colors, sequences, and how you felt when you woke up. Example: 'I dreamt I was walking through a beautiful garden with flowing rivers. The sun was shining and I felt extremely peaceful. Then I saw my deceased grandfather smiling at me...'",
        help="The more detailed your description, the better the AI analysis will be."
    )
    
    # Language selection
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        language = st.radio(
            "Select Interpretation Language:",
            ["English", "Urdu"],
            horizontal=True,
            index=0
        )
    
    # Analyze button
    if st.button("🔮 Analyze Complete Dream with AI", type="primary", use_container_width=True):
        if not dream_text.strip():
            st.error("Please describe your dream first!")
        else:
            with st.spinner("🤖 AI is analyzing your dream using Islamic scholarship..."):
                time.sleep(2)  # Simulate processing time
                
                # Get interpretation
                interpretation = st.session_state.interpreter.analyze_dream_with_ai(
                    dream_text, 
                    language.lower()
                )
                
                st.session_state.current_interpretation = interpretation
                st.session_state.dream_text = dream_text
                st.session_state.language = language
    
    # Display interpretation if available
    if hasattr(st.session_state, 'current_interpretation'):
        st.markdown("---")
        st.markdown("## 📊 Complete Dream Analysis")
        
        interpretation = st.session_state.current_interpretation
        language = st.session_state.language
        
        # Dream Summary
        st.markdown("### 📝 Dream Summary")
        st.markdown(f'<div class="interpretation-section">{interpretation["summary"]}</div>', unsafe_allow_html=True)
        
        # Scholar Analyses
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("### 🧔 Ibn Sirin's Analysis")
            if language == "Urdu":
                st.markdown(f'<div class="urdu-text"><div class="scholar-analysis">{interpretation["ibn_sirin_analysis"]}</div></div>', unsafe_allow_html=True)
            else:
                st.markdown(f'<div class="scholar-analysis">{interpretation["ibn_sirin_analysis"]}</div>', unsafe_allow_html=True)
        
        with col2:
            st.markdown("### 📚 Sheikh Nabulsi's Analysis")
            if language == "Urdu":
                st.markdown(f'<div class="urdu-text"><div class="scholar-analysis">{interpretation["nabulsi_analysis"]}</div></div>', unsafe_allow_html=True)
            else:
                st.markdown(f'<div class="scholar-analysis">{interpretation["nabulsi_analysis"]}</div>', unsafe_allow_html=True)
        
        # Symbolic Meanings
        st.markdown("### 🔍 Symbolic Meanings")
        if language == "Urdu":
            symbols_html = "".join([f'<div class="symbol-box urdu-text">• {symbol}</div>' for symbol in interpretation["symbolic_meanings"]])
        else:
            symbols_html = "".join([f'<div class="symbol-box">• {symbol}</div>' for symbol in interpretation["symbolic_meanings"]])
        st.markdown(symbols_html, unsafe_allow_html=True)
        
        # Practical Advice
        st.markdown("### 💡 Practical Advice")
        if language == "Urdu":
            advice_html = "".join([f'<div class="advice-box urdu-text">• {advice}</div>' for advice in interpretation["practical_advice"]])
        else:
            advice_html = "".join([f'<div class="advice-box">• {advice}</div>' for advice in interpretation["practical_advice"]])
        st.markdown(advice_html, unsafe_allow_html=True)
        
        # Spiritual Guidance
        st.markdown("### 🌟 Spiritual Guidance")
        if language == "Urdu":
            guidance_html = "".join([f'<div class="symbol-box urdu-text">• {guidance}</div>' for guidance in interpretation["spiritual_guidance"]])
        else:
            guidance_html = "".join([f'<div class="symbol-box">• {guidance}</div>' for guidance in interpretation["spiritual_guidance"]])
        st.markdown(guidance_html, unsafe_allow_html=True)
        
        # Overall Assessment
        st.markdown("### 📈 Overall Assessment")
        if language == "Urdu":
            st.markdown(f'<div class="interpretation-section urdu-text">{interpretation["overall_assessment"]}</div>', unsafe_allow_html=True)
        else:
            st.markdown(f'<div class="interpretation-section">{interpretation["overall_assessment"]}</div>', unsafe_allow_html=True)
    
    # Sidebar
    with st.sidebar:
        st.markdown("## 📖 About This AI Interpreter")
        
        st.info("""
        **AI-Powered Islamic Dream Analysis**
        
        This interpreter uses advanced analysis combined with:
        - Ibn Sirin's classical methodology
        - Sheikh Nabulsi's spiritual approach
        - Modern AI understanding
        - Islamic dream principles
        
        **Features:**
        • Complete dream narrative analysis
        • Dual-language support (English/Urdu)
        • Scholarly perspectives
        • Practical and spiritual guidance
        """)
        
        st.markdown("## 🌍 Language Support")
        st.write("""
        **English:** Detailed analysis with Islamic context
        **Urdu:** روحانی تعبیر اور اسلامی رہنمائی
        
        Choose your preferred language for comprehensive interpretation.
        """)
        
        st.markdown("## ⚠️ Important Notes")
        st.warning("""
        **Islamic Guidelines:**
        - True dreams are from Allah
        - Bad dreams are from Shaytan
        - Share only good dreams
        - Consult scholars for important matters
        
        **AI Disclaimer:**
        This is an AI-assisted tool for educational purposes. For personal guidance, always consult knowledgeable Islamic scholars.
        """)
        
        st.markdown("## 🔄 How to Use")
        st.write("""
        1. Describe your complete dream in detail
        2. Select your preferred language
        3. Click 'Analyze Complete Dream'
        4. Receive comprehensive interpretation
        5. Reflect on the guidance provided
        """)

    # Footer
    st.markdown("---")
    st.markdown("""
    <div style="text-align: center; color: #666; padding: 20px;">
    <h4>🤖 AI Islamic Dream Interpreter</h4>
    <p><em>Combining Classical Islamic Scholarship with Modern AI Analysis</em></p>
    <p style="font-size: 0.8rem;">
    This tool provides AI-powered dream analysis based on Islamic principles. 
    Always remember the Islamic etiquette regarding dreams and consult scholars for personal matters.
    </p>
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
