import streamlit as st
import pandas as pd
import numpy as np
import re
import requests
from typing import Dict, List, Tuple
import json

class DreamInterpreter:
    def __init__(self):
        self.setup_models()
        self.setup_dream_databases()
        
    def setup_models(self):
        """Initialize AI models for dream interpretation"""
        try:
            # Using a simpler approach without heavy models for Streamlit Cloud compatibility
            self.models_loaded = True
        except Exception as e:
            st.error(f"Error loading models: {e}")
            self.models_loaded = False
    
    def setup_dream_databases(self):
        """Setup dream interpretation databases for both scholars"""
        # Ibn Sirin's interpretations (expanded dataset)
        self.ibn_sirin_db = {
            "water": "Seeing water in a dream indicates life, knowledge, and wealth. Clear water means lawful earnings, while murky water suggests difficulties.",
            "snake": "A snake represents a hidden enemy. Killing a snake means overcoming enemies or temptations.",
            "teeth": "Teeth falling out may indicate worries about family or the passing of time. Upper teeth represent male relatives, lower teeth female relatives.",
            "money": "Finding money means unexpected blessings. If taken unlawfully, it indicates worries.",
            "death": "Seeing death could mean long life, changes in circumstances, or spiritual rebirth.",
            "house": "A new house means new opportunities, marriage, or spiritual growth.",
            "travel": "Traveling indicates seeking knowledge, changes in life, or spiritual journey.",
            "fire": "Fire represents trials, purification, or anger. Controlled fire can mean useful knowledge.",
            "bird": "Birds symbolize news, messages, or spiritual aspirations. Color indicates nature of message.",
            "book": "Reading a book means acquiring knowledge, receiving guidance, or understanding life's purpose.",
            "ocean": "The ocean represents deep emotions, vast knowledge, or the subconscious mind.",
            "mountain": "Mountains symbolize challenges, strong support, or major obstacles in life.",
            "rain": "Rain indicates blessings, mercy, and spiritual nourishment from Allah.",
            "sun": "The sun represents authority, knowledge, enlightenment, or a powerful figure.",
            "moon": "The moon symbolizes beauty, femininity, reflection, or spiritual guidance.",
            "lion": "A lion represents a powerful ruler, authority, or personal strength. A tame lion means respect.",
            "king": "Seeing a king indicates honor, success, or divine favor in your endeavors.",
            "wedding": "Marriage symbolizes union, agreement, new beginnings, or spiritual harmony.",
            "child": "Children represent new ideas, projects, joys, or spiritual innocence.",
            "river": "A flowing river means continuous blessings, smooth life flow, and spiritual growth.",
            "storm": "Storms indicate difficulties, emotional turmoil, or major life changes ahead.",
            "gold": "Gold symbolizes pure knowledge, valuable insights, or spiritual wealth.",
            "food": "Eating good food means lawful earnings, blessings, and contentment.",
            "blood": "Blood represents family ties, life force, or money obtained through questionable means.",
            "tree": "A green tree means good life and happiness, while a dry tree indicates difficulties.",
            "fish": "Fish represent livelihood, blessings from the sea, or unexpected provisions.",
            "horse": "A horse symbolizes honor, status, or a good journey. Riding well means success.",
            "car": "Modern interpretation: A vehicle represents your life's journey and direction.",
            "school": "Learning in a dream means seeking knowledge or spiritual growth.",
            "prayer": "Praying in a dream indicates connection with Allah and spiritual fulfillment.",
        }
        
        # Sheikh Abdul Ghani Nabulsi's interpretations
        self.nabulsi_db = {
            "water": "Water signifies spiritual purity, divine blessings, and the flow of mercy. Its condition reflects one's spiritual state.",
            "snake": "Represents hidden enemies, temptations, or negative thoughts. Overcoming it means spiritual victory.",
            "teeth": "Symbolize family members, relationships, and social connections. Each tooth represents different aspects of life.",
            "money": "Wealth in dreams reflects spiritual richness, trust in divine provision, and inner contentment.",
            "death": "Indicates spiritual transformation, end of a phase, or rebirth into higher consciousness.",
            "house": "Represents the soul, spiritual condition, and inner world. Rooms symbolize different spiritual aspects.",
            "travel": "Spiritual journey, seeking higher knowledge, enlightenment, or moving to better states.",
            "fire": "Divine purification, spiritual tests that strengthen faith, or transformation through trials.",
            "bird": "Soul's aspirations, divine messages, or spiritual freedom. Color indicates nature of spiritual guidance.",
            "book": "Divine guidance, record of deeds, or spiritual knowledge. Reading means understanding divine will.",
            "ocean": "The ocean of divine knowledge, infinite mercy, and spiritual depth beyond comprehension.",
            "mountain": "Steadfastness in faith, major spiritual obstacles, or connection with higher realms.",
            "rain": "Divine mercy, spiritual nourishment, answers to prayers, and blessings from heaven.",
            "sun": "Divine light, guidance, spiritual illumination, or the light of faith in the heart.",
            "moon": "Spiritual beauty, inner light, reflection of divine attributes, or feminine wisdom.",
            "lion": "Spiritual strength, courage in facing challenges, or divine power protecting you.",
            "king": "Represents divine authority, your higher self, or spiritual sovereignty seeking guidance.",
            "wedding": "Spiritual union with divine truth, integration of personality, or harmony with destiny.",
            "child": "The inner child, new spiritual insights being born, or purity of intention.",
            "river": "Flow of divine grace, spiritual nourishment, and continuous blessings from Allah.",
            "storm": "Spiritual tests that cleanse and strengthen faith, or major transformations approaching.",
            "gold": "Divine wisdom, spiritual treasures, or the gold of sincere faith and good deeds.",
            "food": "Spiritual nourishment, acceptance of good deeds, or feeding the soul with remembrance of Allah.",
            "blood": "Life force, spiritual lineage, connection to ancestors, or the blood of spiritual sacrifice.",
            "tree": "Spiritual growth, connection to divine roots, or the tree of faith bearing fruits.",
            "fish": "Spiritual provisions, blessings from the unseen, or insights from the depths of consciousness.",
            "horse": "Spiritual journey, noble character, or the vehicle carrying you toward Allah.",
            "car": "Modern interpretation: Your spiritual path and the means of your spiritual progress.",
            "school": "Spiritual learning, lessons from Allah, or the school of life teaching divine wisdom.",
            "prayer": "Direct connection with the Divine, spiritual fulfillment, or answered supplications.",
        }
    
    def extract_dream_elements(self, dream_text: str) -> List[str]:
        """Extract key elements from dream text"""
        dream_text_lower = dream_text.lower()
        found_elements = []
        
        for element in self.ibn_sirin_db.keys():
            if element in dream_text_lower:
                found_elements.append(element)
        
        # Also check for partial matches
        words = dream_text_lower.split()
        for word in words:
            if len(word) > 3 and word not in found_elements:
                for element in self.ibn_sirin_db.keys():
                    if word in element or element in word:
                        if element not in found_elements:
                            found_elements.append(element)
                            break
        
        return found_elements[:8]  # Return top 8 elements
    
    def get_ibn_sirin_interpretation(self, elements: List[str]) -> str:
        """Get interpretation based on Ibn Sirin's teachings"""
        if not elements:
            return "Based on Ibn Sirin's teachings: Dreams should be interpreted by their most obvious meanings and context. Consider the emotions you felt and the overall narrative. Good dreams are from Allah, while bad dreams may be from Shaytan."
        
        interpretations = []
        for element in elements:
            if element in self.ibn_sirin_db:
                interpretations.append(f"**{element.capitalize()}:** {self.ibn_sirin_db[element]}")
        
        result = "### Ibn Sirin's Interpretation:\n\n" + "\n\n".join(interpretations)
        result += "\n\n*Note: Ibn Sirin emphasized that dream interpretation depends on the dreamer's circumstances and the dream's context.*"
        return result
    
    def get_nabulsi_interpretation(self, elements: List[str]) -> str:
        """Get interpretation based on Sheikh Nabulsi's teachings"""
        if not elements:
            return "Based on Sheikh Nabulsi's teachings: Reflect on your spiritual state and relationship with Allah. Dreams are mirrors of the soul and can indicate spiritual progress or areas needing attention."
        
        interpretations = []
        for element in elements:
            if element in self.nabulsi_db:
                interpretations.append(f"**{element.capitalize()}:** {self.nabulsi_db[element]}")
        
        result = "### Sheikh Nabulsi's Interpretation:\n\n" + "\n\n".join(interpretations)
        result += "\n\n*Note: Sheikh Nabulsi focused on the spiritual dimensions and symbolic meanings in dreams.*"
        return result
    
    def generate_comprehensive_interpretation(self, dream_text: str, elements: List[str]) -> str:
        """Generate comprehensive interpretation"""
        if not elements:
            elements = ["the overall dream"]
            
        element_list = ", ".join([elem.capitalize() for elem in elements])
        
        interpretation = f"""
## Comprehensive Dream Analysis

### Dream Summary:
{dream_text}

### Key Elements Identified:
{element_list}

### Overall Interpretation:

Based on Islamic dream interpretation principles:

**Spiritual Perspective:**
Your dream contains elements that reflect your spiritual state and relationship with Allah. Consider the emotions you experienced - peace indicates spiritual comfort, while fear may suggest spiritual concerns.

**Psychological Insight:**
Dreams often process daily experiences and subconscious thoughts. Reflect on what's currently happening in your life and how it might connect to these dream elements.

**Practical Guidance:**
- Remember that true dream interpretation requires considering your personal circumstances
- Good dreams are from Allah - give thanks
- Bad dreams are from Shaytan - seek refuge in Allah and don't share them
- Use the dream as motivation for self-reflection and improvement

**Islamic Context:**
In Islam, dreams can be of three types:
1. **True dreams** (Ru'ya) - from Allah
2. **Bad dreams** (Hulum) - from Shaytan  
3. **Dreams from one's self** - reflections of daily thoughts

*This analysis combines traditional Islamic scholarship with general dream interpretation principles.*
"""
        return interpretation

def main():
    # Configure Streamlit page
    st.set_page_config(
        page_title="Islamic Dream Interpreter",
        page_icon="🌙",
        layout="wide",
        initial_sidebar_state="expanded"
    )
    
    # Custom CSS for better styling
    st.markdown("""
    <style>
    .main-header {
        font-size: 3rem;
        color: #2E86AB;
        text-align: center;
        margin-bottom: 2rem;
        font-weight: bold;
        padding: 20px;
    }
    .scholar-header {
        font-size: 1.8rem;
        color: #A23B72;
        margin-bottom: 1rem;
        font-weight: bold;
    }
    .dream-input {
        font-size: 1.2rem;
    }
    .interpretation-box {
        background-color: #f8f9fa;
        padding: 25px;
        border-radius: 10px;
        border-left: 5px solid #2E86AB;
        margin: 15px 0;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    .element-badge {
        background-color: #2E86AB;
        color: white;
        padding: 5px 10px;
        border-radius: 15px;
        margin: 5px;
        display: inline-block;
        font-weight: bold;
    }
    .footer {
        text-align: center;
        margin-top: 3rem;
        color: #666;
        font-size: 0.9rem;
        padding: 20px;
    }
    </style>
    """, unsafe_allow_html=True)
    
    # Header
    st.markdown('<div class="main-header">🌙 Islamic Dream Interpreter</div>', unsafe_allow_html=True)
    st.markdown("### Based on the Works of Ibn Sirin and Sheikh Abdul Ghani Nabulsi")
    
    # Initialize interpreter
    if 'interpreter' not in st.session_state:
        st.session_state.interpreter = DreamInterpreter()
    
    # Dream input section
    st.markdown("---")
    st.markdown("### 📝 Describe Your Dream")
    
    col1, col2 = st.columns([3, 1])
    with col1:
        dream_text = st.text_area(
            "Write your dream in detail:",
            height=200,
            placeholder="Describe your dream here... Include details about people, objects, colors, emotions, and events. Be as specific as possible.",
            key="dream_input",
            help="The more details you provide, the better the interpretation will be."
        )
    
    with col2:
        st.markdown("**Tips for better interpretation:**")
        st.markdown("""
        - Write immediately after waking
        - Include emotions felt
        - Note colors and numbers
        - Describe people involved
        - Mention the setting
        """)
    
    # Interpretation button
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        interpret_btn = st.button("🔮 Interpret My Dream", use_container_width=True, type="primary")
    
    if interpret_btn and dream_text:
        with st.spinner("🔍 Analyzing your dream with Islamic scholarship..."):
            # Extract dream elements
            elements = st.session_state.interpreter.extract_dream_elements(dream_text)
            
            # Get interpretations
            ibn_sirin = st.session_state.interpreter.get_ibn_sirin_interpretation(elements)
            nabulsi = st.session_state.interpreter.get_nabulsi_interpretation(elements)
            comprehensive = st.session_state.interpreter.generate_comprehensive_interpretation(dream_text, elements)
        
        # Display dream elements
        if elements:
            st.markdown("### 🔍 Elements Identified in Your Dream")
            elements_html = " ".join([f'<span class="element-badge">{elem.capitalize()}</span>' for elem in elements])
            st.markdown(f'<div style="margin: 20px 0;">{elements_html}</div>', unsafe_allow_html=True)
        
        # Display results in tabs
        st.markdown("---")
        st.markdown("## 📖 Dream Interpretations")
        
        tab1, tab2, tab3 = st.tabs([
            "🧔 Ibn Sirin's View", 
            "📚 Sheikh Nabulsi's View", 
            "🌟 Comprehensive Analysis"
        ])
        
        with tab1:
            st.markdown(ibn_sirin, unsafe_allow_html=True)
        
        with tab2:
            st.markdown(nabulsi, unsafe_allow_html=True)
        
        with tab3:
            st.markdown(comprehensive, unsafe_allow_html=True)
    
    elif interpret_btn and not dream_text:
        st.warning("⚠️ Please describe your dream first!")
    
    # Sidebar with information
    with st.sidebar:
        st.markdown("## 🌟 About This App")
        st.info("""
        This Islamic Dream Interpreter is based on the authoritative works of:
        
        **• Ibn Sirin** (8th century)
        - Famous classical Islamic scholar
        - Pioneer of Islamic dream interpretation
        - Known for his comprehensive approach
        
        **• Sheikh Abdul Ghani Nabulsi** (17th century)
        - Renowned Sufi scholar and mystic
        - Author of extensive dream interpretation works
        - Emphasized spiritual dimensions
        """)
        
        st.markdown("## 📚 Interpretation Guidelines")
        st.write("""
        **Islamic Dream Types:**
        1. **True Dreams** - Good news from Allah
        2. **Bad Dreams** - From Shaytan
        3. **Daily Reflections** - From one's thoughts
        
        **Best Practices:**
        - Share only good dreams
        - Seek refuge from bad dreams
        - Consider personal context
        - Consult scholars for important dreams
        """)
        
        st.markdown("## ⚠️ Important Disclaimer")
        st.warning("""
        This tool provides general interpretations based on Islamic scholarship. 
        
        **For personal guidance:**
        - Consult knowledgeable scholars
        - Consider your personal circumstances
        - Dreams should not be used for major life decisions without proper consultation
        
        *"True dreams are one of the forty-six parts of Prophethood."* - Sahih Muslim
        """)
        
        st.markdown("## 🔮 Common Dream Meanings")
        common_elements = st.selectbox(
            "Quick reference:",
            ["Select an element", "Water", "Snake", "Teeth", "Money", "House", "Travel", "Fire", "Birds"]
        )
        
        if common_elements != "Select an element":
            element_lower = common_elements.lower()
            if element_lower in st.session_state.interpreter.ibn_sirin_db:
                st.write(f"**Ibn Sirin:** {st.session_state.interpreter.ibn_sirin_db[element_lower]}")
                st.write(f"**Nabulsi:** {st.session_state.interpreter.nabulsi_db[element_lower]}")
    
    # Footer
    st.markdown("---")
    st.markdown("""
    <div class="footer">
    <p>🌙 Islamic Dream Interpreter • Based on Authentic Islamic Scholarship</p>
    <p><em>May Allah guide us to understand the wisdom behind our dreams and use them for spiritual growth</em></p>
    <p style="font-size: 0.8rem; margin-top: 10px;">Note: This application combines traditional Islamic dream interpretation with modern technology for educational purposes.</p>
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
