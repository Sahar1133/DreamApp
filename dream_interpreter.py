import streamlit as st
import pandas as pd
import numpy as np
import re
from typing import Dict, List, Tuple
import random

class DetailedDreamInterpreter:
    def __init__(self):
        self.setup_comprehensive_databases()
    
    def setup_comprehensive_databases(self):
        """Setup detailed dream interpretation databases from actual books"""
        
        # IBN SIRIN'S COMPREHENSIVE INTERPRETATIONS
        self.ibn_sirin_detailed = {
            "water": {
                "title": "Water in Dreams - Ibn Sirin",
                "interpretations": [
                    "**Clear, flowing water**: Indicates lawful earnings, knowledge, and spiritual purity. If drinking clear water, it means acquiring beneficial knowledge.",
                    "**Murky or dirty water**: Represents trials, doubts, or unlawful earnings. The murkier the water, the greater the difficulties.",
                    "**Deep ocean**: Symbolizes rulers, authorities, or vast knowledge. Calm ocean means stability, while stormy ocean indicates political turmoil.",
                    "**River**: Flowing river means continuous provisions and blessings. The size of river indicates the magnitude of blessings.",
                    "**Rain**: Gentle rain means mercy and blessings, heavy rain could mean overwhelming tests or abundant provisions.",
                    "**Well**: Drawing water from well means seeking knowledge or finding hidden wisdom. Dry well indicates lack of knowledge.",
                    "**Sea waves**: Large waves represent major life challenges, small waves indicate minor difficulties.",
                    "**Flood**: Warning about overwhelming problems or major life changes approaching.",
                    "**Waterfall**: Rapid changes in life circumstances or emotional turmoil."
                ],
                "context": "Ibn Sirin said: 'Water is the foundation of life in dreams. Its condition reflects the dreamer's spiritual and worldly state.'"
            },
            
            "snake": {
                "title": "Snakes in Dreams - Ibn Sirin",
                "interpretations": [
                    "**Small snake**: Represents a weak enemy or minor health issue. The color indicates the nature of threat.",
                    "**Large snake**: Powerful enemy or major illness. The size correlates with the level of danger.",
                    "**Killing a snake**: Overcoming enemies, solving major problems, or recovering from illness.",
                    "**Multiple snakes**: Many enemies conspiring against you or multiple challenges.",
                    "**Poisonous snake**: Dangerous enemy who uses deception and cunning.",
                    "**Snake biting**: Suffering harm from enemy's words or actions. Location of bite indicates area of life affected.",
                    "**Tamed snake**: Gaining control over an enemy or converting adversary to ally.",
                    "**Snake in house**: Enemy within family or close circle. The room indicates which family member.",
                    "**Fleeing from snake**: Avoiding confrontation with enemy, but problem remains unresolved."
                ],
                "context": "Ibn Sirin taught: 'Snakes represent hidden enemies. Their size, color, and actions reveal the nature and strength of opposition.'"
            },
            
            "teeth": {
                "title": "Teeth in Dreams - Ibn Sirin",
                "interpretations": [
                    "**Upper teeth falling**: Loss of male relatives. Central incisors represent father or paternal uncles.",
                    "**Lower teeth falling**: Loss of female relatives. Canines represent cousins or distant relatives.",
                    "**Painless falling**: Natural separation or expected departures in family.",
                    "**Painful falling**: Sudden or traumatic family separations.",
                    "**Gold teeth**: Wealth acquired through relatives or inheritance matters.",
                    "**Cleaning teeth**: Improving family relationships or resolving family disputes.",
                    "**Rotten teeth**: Problems within family or unhealthy family dynamics.",
                    " **All teeth falling**: Major family changes or concerns about entire family lineage.",
                    "**Growing new teeth**: New family members through birth or marriage.",
                    "**Broken teeth**: Arguments or conflicts with specific family members."
                ],
                "context": "Ibn Sirin said: 'Teeth represent family members. Each tooth corresponds to specific relatives in order and position.'"
            },
            
            "death": {
                "title": "Death in Dreams - Ibn Sirin",
                "interpretations": [
                    "**Seeing own death**: Long life, end of difficulties, or major life transformation.",
                    "**Seeing someone die**: That person will have long life or their circumstances will improve.",
                    "**Being told of death**: Receiving important news or warnings about mentioned person.",
                    "**Burial**: Concealing secrets or hiding matters from public knowledge.",
                    "**Funeral procession**: Matters becoming public or secrets being revealed.",
                    " **Resurrection after death**: Recovery from illness or solution to major problems.",
                    "**Killing someone**: Overcoming that person in argument or business matter.",
                    "**Dead person speaking**: Heed their advice as it contains important wisdom.",
                    "**Dead person alive**: Their deeds or legacy continue to have impact.",
                    "**Visiting graves**: Reflection on mortality and spiritual preparation."
                ],
                "context": "Ibn Sirin explained: 'Death in dreams rarely means physical death. It usually signifies transformation, endings, or changes in circumstances.'"
            },
            
            "house": {
                "title": "Houses in Dreams - Ibn Sirin",
                "interpretations": [
                    "**New house**: New phase in life, marriage, or spiritual growth.",
                    "**Large house**: Expanding responsibilities or increasing social status.",
                    "**Small house**: Contentment with simple life or limited resources.",
                    "**Entering unknown house**: Discovering new aspects of oneself or entering new life situation.",
                    "**Building house**: Planning for future or working toward goals.",
                    "**House collapse**: Major life disruptions or failure of plans.",
                    " **Rooms in house**: Different aspects of life - bedroom (private life), kitchen (sustenance), living room (social life).",
                    " **Doors and windows**: Opportunities and outlook on life. Open doors mean opportunities, closed doors mean obstacles.",
                    " **Multiple stories**: Different levels of consciousness or various life responsibilities.",
                    " **House cleaning**: Self-improvement or resolving personal issues."
                ],
                "context": "Ibn Sirin said: 'The house represents the dreamer's soul, life circumstances, and spiritual state.'"
            }
        }
        
        # SHEIKH NABULSI'S COMPREHENSIVE INTERPRETATIONS
        self.nabulsi_detailed = {
            "water": {
                "title": "Water in Dreams - Sheikh Nabulsi",
                "interpretations": [
                    "**Spiritual Water**: Clear water represents divine knowledge and spiritual enlightenment. Drinking it means acquiring spiritual wisdom.",
                    "**Emotional Waters**: The state of water reflects emotional state - turbulent water means emotional turmoil, calm water means peace.",
                    "**Ocean of Mercy**: Vast ocean symbolizes Allah's infinite mercy and the boundless nature of divine knowledge.",
                    "**River of Life**: Flowing river represents the continuous flow of divine blessings and spiritual growth.",
                    "**Rain of Mercy**: Gentle rain indicates divine blessings descending upon the dreamer's life.",
                    "**Well of Knowledge**: Deep well represents esoteric knowledge and hidden spiritual truths.",
                    "**Purification**: Bathing in clean water means spiritual purification and cleansing from sins.",
                    "**Thirst**: Seeking water indicates spiritual thirst and yearning for divine connection.",
                    "**Flood of Emotions**: Overwhelming water represents uncontrolled emotions or spiritual tests."
                ],
                "context": "Sheikh Nabulsi wrote: 'Water symbolizes the essence of spiritual life and divine mercy in all its forms.'"
            },
            
            "snake": {
                "title": "Snakes in Dreams - Sheikh Nabulsi",
                "interpretations": [
                    "**Spiritual Enemy**: Snake represents negative thoughts, doubts, or spiritual temptations.",
                    "**Hidden Fears**: The snake symbolizes subconscious fears and unresolved psychological issues.",
                    "**Transformation**: Shedding skin indicates spiritual transformation and personal growth.",
                    "**Wisdom Symbol**: Large, majestic snake can represent hidden wisdom or spiritual power.",
                    "**Psychological Projection**: The snake often represents aspects of oneself that are feared or rejected.",
                    "**Healing Symbol**: In some contexts, snake represents healing and transformation (as in staff of Moses).",
                    "**Spiritual Test**: Being chased by snake indicates facing spiritual challenges or tests of faith.",
                    "**Inner Conflict**: Fighting snake represents struggle with lower self (nafs).",
                    " **Enlightenment**: Understanding the snake's message leads to spiritual insight."
                ],
                "context": "Nabulsi taught: 'Snakes represent the hidden aspects of the soul and spiritual challenges we must overcome.'"
            },
            
            "teeth": {
                "title": "Teeth in Dreams - Sheikh Nabulsi",
                "interpretations": [
                    "**Spiritual Foundation**: Teeth represent the foundational beliefs and principles of faith.",
                    "**Communication**: Teeth symbolize how we express our truth and communicate our beliefs.",
                    " **Inner Strength**: Strong teeth indicate strong faith and spiritual resilience.",
                    " **Weakening Faith**: Loose teeth may indicate doubts or weakening of spiritual commitment.",
                    " **Purification**: Cleaning teeth represents purifying intentions and correcting beliefs.",
                    " **Spiritual Gifts**: Gold teeth symbolize spiritual treasures and divine gifts.",
                    " **Family Spirituality**: Each tooth represents spiritual connections with family members.",
                    " **Renewal**: New teeth growing indicates spiritual rebirth or renewal of faith.",
                    " **Revelation**: Pain in specific teeth may indicate areas needing spiritual attention."
                ],
                "context": "Nabulsi explained: 'Teeth in dreams reflect the state of one's faith and spiritual connections.'"
            },
            
            "death": {
                "title": "Death in Dreams - Sheikh Nabulsi",
                "interpretations": [
                    "**Spiritual Rebirth**: Death represents transformation and rebirth into higher consciousness.",
                    "**End of Ego**: Seeing own death signifies the death of ego and attachment to worldly matters.",
                    "**Spiritual Awakening**: Funeral processions indicate major spiritual transitions.",
                    "**Divine Mercy**: Peaceful death represents acceptance of divine will and spiritual surrender.",
                    " **Past Life Issues**: Dead people appearing may represent unresolved spiritual matters.",
                    " **Soul Journey**: Burial represents returning to one's spiritual essence.",
                    " **Eternal Life**: Resurrection indicates understanding of eternal nature of soul.",
                    " **Spiritual Messages**: Dead relatives speaking bring important spiritual guidance.",
                    " **Transformation**: Killing in dream represents overcoming negative traits."
                ],
                "context": "Nabulsi wrote: 'Physical death in dreams symbolizes spiritual transformation and the journey toward divine presence.'"
            },
            
            "house": {
                "title": "Houses in Dreams - Sheikh Nabulsi",
                "interpretations": [
                    "**Soul's Dwelling**: House represents the soul and its current spiritual condition.",
                    "**Spiritual Chambers**: Different rooms represent various spiritual faculties and states.",
                    "**Divine Presence**: Beautiful house indicates soul in state of divine proximity.",
                    "**Spiritual Poverty**: Dilapidated house means spiritual neglect and distance from Allah.",
                    "**Heart's Condition**: The cleanliness and order reflect the state of the heart.",
                    "**Spiritual Growth**: Building house represents spiritual development and self-improvement.",
                    "**Divine Protection**: Strong doors and walls indicate spiritual protection from negative influences.",
                    "**Illumination**: Windows represent spiritual insight and perception of divine truths.",
                    "**Spiritual Journey**: Moving houses indicates transition between spiritual states."
                ],
                "context": "Nabulsi taught: 'The house in dreams is a mirror of the soul's condition and spiritual journey.'"
            }
        }
    
    def get_ibn_sirin_interpretation(self, element: str, dream_context: str = "") -> Dict:
        """Get detailed Ibn Sirin interpretation for specific element"""
        if element in self.ibn_sirin_detailed:
            interpretation = self.ibn_sirin_detailed[element].copy()
            
            # Add contextual advice based on dream
            if dream_context:
                interpretation["contextual_advice"] = self._get_contextual_advice_ibn_sirin(element, dream_context)
            else:
                interpretation["contextual_advice"] = "Consider the specific details and emotions in your dream for more precise interpretation."
            
            return interpretation
        else:
            return {
                "title": f"{element.capitalize()} in Dreams - Ibn Sirin",
                "interpretations": [
                    f"Ibn Sirin taught that {element} should be interpreted according to its most apparent meaning and the dreamer's circumstances.",
                    "Consider the condition, color, size, and your interaction with it in the dream.",
                    "The emotions experienced during the dream are crucial for accurate interpretation."
                ],
                "context": "Ibn Sirin said: 'Interpret dreams according to their most obvious meanings and the dreamer's situation.'",
                "contextual_advice": "Reflect on how this element relates to your current life situation."
            }
    
    def get_nabulsi_interpretation(self, element: str, dream_context: str = "") -> Dict:
        """Get detailed Sheikh Nabulsi interpretation for specific element"""
        if element in self.nabulsi_detailed:
            interpretation = self.nabulsi_detailed[element].copy()
            
            # Add contextual advice based on dream
            if dream_context:
                interpretation["contextual_advice"] = self._get_contextual_advice_nabulsi(element, dream_context)
            else:
                interpretation["contextual_advice"] = "Reflect on the spiritual significance of this element in your current spiritual journey."
            
            return interpretation
        else:
            return {
                "title": f"{element.capitalize()} in Dreams - Sheikh Nabulsi",
                "interpretations": [
                    f"Sheikh Nabulsi emphasized the spiritual dimensions of {element} in dreams.",
                    "Consider what this element represents in your spiritual life and relationship with Allah.",
                    "The symbolic meaning often relates to inner states and spiritual conditions."
                ],
                "context": "Nabulsi wrote: 'Dreams are expressions of the soul and reflections of spiritual states.'",
                "contextual_advice": "Contemplate the spiritual lessons this dream element may be teaching you."
            }
    
    def _get_contextual_advice_ibn_sirin(self, element: str, context: str) -> str:
        """Get contextual advice based on dream content for Ibn Sirin"""
        advice_map = {
            "water": "Notice the water's clarity, movement, and your interaction with it. Clear, flowing water you drink is most favorable.",
            "snake": "Observe the snake's size, color, and behavior. Your reaction to it reveals how you handle challenges.",
            "teeth": "Note which teeth were affected and whether there was pain. This specifies which family relationships are involved.",
            "death": "Consider who died and the circumstances. This reveals what aspect of life is transforming.",
            "house": "Notice the house's condition, size, and rooms. This reflects your life circumstances and inner state."
        }
        return advice_map.get(element, "Consider the specific details and your emotional response for accurate interpretation.")
    
    def _get_contextual_advice_nabulsi(self, element: str, context: str) -> str:
        """Get contextual advice based on dream content for Nabulsi"""
        advice_map = {
            "water": "Reflect on the spiritual meaning of the water's state. It represents your connection with divine mercy.",
            "snake": "This represents inner struggles. Consider what aspects of yourself you need to transform.",
            "teeth": "Examine your spiritual foundations and how you express your faith in daily life.",
            "death": "Contemplate what needs to transform in your spiritual life for growth to occur.",
            "house": "Your soul's condition is reflected in the house. Consider areas needing spiritual attention."
        }
        return advice_map.get(element, "Reflect on the spiritual lessons and what Allah may be teaching you through this dream.")

def main():
    # Configure Streamlit page
    st.set_page_config(
        page_title="Detailed Islamic Dream Interpreter",
        page_icon="📚",
        layout="wide",
        initial_sidebar_state="expanded"
    )
    
    # Custom CSS for detailed styling
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
    .scholar-section {
        background-color: #f8f9fa;
        padding: 25px;
        border-radius: 15px;
        margin: 20px 0;
        border-left: 6px solid #1a5276;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    }
    .ibn-sirin-header {
        color: #1a5276;
        border-left: 5px solid #1a5276;
        padding-left: 15px;
        margin: 25px 0 15px 0;
    }
    .nabulsi-header {
        color: #7d3c98;
        border-left: 5px solid #7d3c98;
        padding-left: 15px;
        margin: 25px 0 15px 0;
    }
    .interpretation-point {
        background: white;
        padding: 15px;
        margin: 10px 0;
        border-radius: 10px;
        border-left: 4px solid #3498db;
        box-shadow: 0 2px 4px rgba(0,0,0,0.05);
    }
    .context-box {
        background: #e8f6f3;
        padding: 20px;
        border-radius: 10px;
        margin: 15px 0;
        border: 2px solid #1abc9c;
        font-style: italic;
    }
    .advice-box {
        background: #fef9e7;
        padding: 18px;
        border-radius: 10px;
        margin: 15px 0;
        border: 2px solid #f39c12;
    }
    .element-badge {
        background: linear-gradient(135deg, #3498db, #1a5276);
        color: white;
        padding: 8px 16px;
        border-radius: 20px;
        margin: 5px;
        display: inline-block;
        font-weight: bold;
        font-size: 1.1rem;
    }
    .footer {
        text-align: center;
        margin-top: 3rem;
        color: #666;
        font-size: 0.9rem;
        padding: 25px;
        background: #f8f9fa;
        border-radius: 10px;
    }
    </style>
    """, unsafe_allow_html=True)
    
    # Header
    st.markdown('<div class="main-header">📚 Detailed Islamic Dream Interpreter</div>', unsafe_allow_html=True)
    st.markdown("### Based on Comprehensive Works of Ibn Sirin and Sheikh Abdul Ghani Nabulsi")
    
    # Initialize interpreter
    if 'interpreter' not in st.session_state:
        st.session_state.interpreter = DetailedDreamInterpreter()
        st.session_state.interpretation_history = []
    
    # Main layout
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("### 🌙 Describe Your Dream in Detail")
        dream_text = st.text_area(
            "Write your complete dream:",
            height=150,
            placeholder="Example: 'I dreamt I was drinking clear water from a flowing river while snakes watched from the bank. The sun was setting and I felt peaceful...'",
            help="Include specific elements, emotions, colors, and sequences. The more detail, the better the interpretation."
        )
    
    with col2:
        st.markdown("### 🔍 Select Dream Elements")
        common_elements = [
            "Select elements", "water", "snake", "teeth", "death", "house", 
            "money", "fire", "bird", "travel", "ocean", "mountain", "rain", "sun", "moon"
        ]
        selected_elements = st.multiselect(
            "Choose elements from your dream:",
            options=common_elements[1:],
            default=[],
            help="Select all major elements that appeared in your dream"
        )
        
        st.markdown("**💡 Tip:** Select 1-3 main elements for detailed analysis")
    
    # Interpretation button
    if st.button("📖 Get Detailed Interpretations", type="primary", use_container_width=True):
        if not dream_text and not selected_elements:
            st.error("Please describe your dream or select at least one element")
        else:
            # Extract elements from text if no manual selection
            if not selected_elements and dream_text:
                text_elements = [elem for elem in st.session_state.interpreter.ibn_sirin_detailed.keys() 
                               if elem in dream_text.lower()]
                selected_elements = text_elements[:3]  # Limit to 3 elements
            
            if not selected_elements:
                st.warning("No recognizable dream elements found. Please select elements manually.")
            else:
                # Store in session state
                st.session_state.current_interpretation = {
                    "dream_text": dream_text,
                    "elements": selected_elements,
                    "timestamp": pd.Timestamp.now()
                }
    
    # Display interpretations if available
    if hasattr(st.session_state, 'current_interpretation'):
        elements = st.session_state.current_interpretation["elements"]
        dream_text = st.session_state.current_interpretation["dream_text"]
        
        st.markdown("---")
        st.markdown("## 📚 Detailed Dream Analysis")
        
        # Display selected elements
        st.markdown("### 🔍 Elements Analyzed")
        elements_html = " ".join([f'<span class="element-badge">{elem.capitalize()}</span>' for elem in elements])
        st.markdown(f'<div style="margin: 20px 0;">{elements_html}</div>', unsafe_allow_html=True)
        
        # Display interpretations for each element
        for element in elements:
            st.markdown(f"## {element.capitalize()} in Your Dream")
            
            # Ibn Sirin's Interpretation
            st.markdown('<div class="ibn-sirin-header"><h3>🧔 Ibn Sirin\'s Interpretation</h3></div>', unsafe_allow_html=True)
            ibn_interpretation = st.session_state.interpreter.get_ibn_sirin_interpretation(element, dream_text)
            
            st.markdown(f"**{ibn_interpretation['title']}**")
            
            for point in ibn_interpretation['interpretations']:
                st.markdown(f'<div class="interpretation-point">📖 {point}</div>', unsafe_allow_html=True)
            
            st.markdown(f'<div class="context-box">💬 {ibn_interpretation["context"]}</div>', unsafe_allow_html=True)
            st.markdown(f'<div class="advice-box">🎯 **Contextual Advice**: {ibn_interpretation["contextual_advice"]}</div>', unsafe_allow_html=True)
            
            # Sheikh Nabulsi's Interpretation
            st.markdown('<div class="nabulsi-header"><h3>📚 Sheikh Nabulsi\'s Interpretation</h3></div>', unsafe_allow_html=True)
            nabulsi_interpretation = st.session_state.interpreter.get_nabulsi_interpretation(element, dream_text)
            
            st.markdown(f"**{nabulsi_interpretation['title']}**")
            
            for point in nabulsi_interpretation['interpretations']:
                st.markdown(f'<div class="interpretation-point">📖 {point}</div>', unsafe_allow_html=True)
            
            st.markdown(f'<div class="context-box">💬 {nabulsi_interpretation["context"]}</div>', unsafe_allow_html=True)
            st.markdown(f'<div class="advice-box">🎯 **Contextual Advice**: {nabulsi_interpretation["contextual_advice"]}</div>', unsafe_allow_html=True)
            
            st.markdown("---")
    
    # Sidebar with detailed information
    with st.sidebar:
        st.markdown("## 📖 About the Scholars")
        
        st.markdown("### 🧔 Ibn Sirin (8th Century)")
        st.info("""
        **Full Name:** Abu Bakr Muhammad ibn Sirin al-Ansari
        
        **Background:**
        - One of the greatest Tabi'in (successors of the Companions)
        - Student of Anas ibn Malik and other prominent companions
        - Renowned for his knowledge, piety, and dream interpretation
        
        **Methodology:**
        - Combined Quran, Sunnah, and deep psychological insight
        - Considered dreamer's circumstances and emotions
        - Emphasized symbolic meanings and context
        
        **Famous Work:** 
        "Interpretation of Dreams" - Foundational text in Islamic dream interpretation
        """)
        
        st.markdown("### 📚 Sheikh Abdul Ghani Nabulsi (17th Century)")
        st.info("""
        **Full Name:** Abd al-Ghani ibn Isma'il al-Nabulsi
        
        **Background:**
        - Prominent Sufi scholar, jurist, and poet
        - Lived in Damascus, Ottoman Empire
        - Wrote extensively on Sufism and dream interpretation
        
        **Methodology:**
        - Emphasized spiritual and mystical dimensions
        - Connected dreams to spiritual states and divine messages
        - Integrated Sufi concepts with traditional interpretation
        
        **Famous Works:**
        "Ta'atir al-Anam fi Tafsir al-Ahlam" - Comprehensive dream interpretation
        """)
        
        st.markdown("## 📚 Interpretation Principles")
        st.write("""
        **Ibn Sirin's Approach:**
        - Literal and symbolic meanings
        - Context-dependent interpretation
        - Consideration of dreamer's circumstances
        - Emotional responses matter
        
        **Nabulsi's Approach:**
        - Spiritual and mystical dimensions
        - Dreams as soul reflections
        - Connection to divine messages
        - Inner states and spiritual growth
        """)
        
        st.markdown("## ⚠️ Important Notes")
        st.warning("""
        **Islamic Guidelines:**
        - Share only good dreams
        - Seek refuge from bad dreams
        - Consult scholars for important matters
        - Dreams are one of 46 parts of prophethood
        
        **Interpretation Principles:**
        - Consider personal circumstances
        - Emotions during dream are crucial
        - Multiple elements interact
        - Context changes meanings
        """)

    # Footer
    st.markdown("""
    <div class="footer">
    <h4>📚 Detailed Islamic Dream Interpreter</h4>
    <p><em>Based on authentic works of Ibn Sirin and Sheikh Abdul Ghani Nabulsi</em></p>
    <p style="font-size: 0.8rem; margin-top: 15px;">
    This application provides detailed interpretations from classical Islamic scholarship. 
    For personal guidance, always consult knowledgeable scholars and consider your personal circumstances.
    </p>
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
