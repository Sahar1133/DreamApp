# Install required packages
!pip install streamlit transformers torch sentence-transformers faiss-cpu scikit-learn

# Download the script
%%writefile dream_interpreter.py
import streamlit as st
import pandas as pd
import numpy as np
import re
from transformers import pipeline, AutoTokenizer, AutoModelForSeq2SeqLM
from sentence_transformers import SentenceTransformer
import faiss
import json
import requests
from typing import Dict, List, Tuple

class DreamInterpreter:
    def __init__(self):
        self.setup_models()
        self.setup_dream_databases()
        
    def setup_models(self):
        """Initialize AI models for dream interpretation"""
        try:
            # Translation model for Arabic text
            self.translator = pipeline("translation", model="Helsinki-NLP/opus-mt-ar-en")
            
            # Text generation model for interpretations
            self.generator = pipeline("text-generation", 
                                    model="microsoft/DialoGPT-medium", 
                                    max_length=500,
                                    do_sample=True,
                                    temperature=0.7)
            
            # Sentence similarity model
            self.similarity_model = SentenceTransformer('all-MiniLM-L6-v2')
            
        except Exception as e:
            st.error(f"Error loading models: {e}")
    
    def setup_dream_databases(self):
        """Setup dream interpretation databases for both scholars"""
        # Ibn Sirin's interpretations (sample data - in real app, use full books)
        self.ibn_sirin_db = {
            "water": "Seeing water in a dream indicates life, knowledge, and wealth. Clear water means lawful earnings.",
            "snake": "A snake represents an enemy. Killing a snake means overcoming enemies.",
            "teeth": "Teeth falling out may indicate worries or the passing of time.",
            "money": "Finding money means unexpected blessings or worries if taken unlawfully.",
            "death": "Seeing death in a dream could mean long life or changes in circumstances.",
            "house": "A new house means new opportunities or marriage.",
            "travel": "Traveling indicates seeking knowledge or changes in life.",
            "fire": "Fire represents trials or purification through difficulties.",
            "bird": "Birds symbolize news or messages from afar.",
            "book": "Reading a book means acquiring knowledge or receiving guidance.",
            "ocean": "The ocean represents deep emotions or vast knowledge.",
            "mountain": "Mountains symbolize challenges or strong support.",
            "rain": "Rain indicates blessings and mercy from Allah.",
            "sun": "The sun represents authority, knowledge, or a powerful person.",
            "moon": "The moon symbolizes beauty, leadership, or feminine qualities."
        }
        
        # Sheikh Abdul Ghani Nabulsi's interpretations
        self.nabulsi_db = {
            "water": "Water signifies spiritual purity and divine blessings. Its condition reflects spiritual state.",
            "snake": "Represents hidden enemies or temptations. Color and size indicate danger level.",
            "teeth": "Symbolize family members and relationships. Each tooth represents a relative.",
            "money": "Wealth in dreams reflects spiritual richness and trust in divine provision.",
            "death": "Indicates spiritual transformation or end of a phase, not physical death.",
            "house": "Represents the soul and spiritual condition. Rooms symbolize different aspects.",
            "travel": "Spiritual journey or seeking higher knowledge and enlightenment.",
            "fire": "Divine purification or tests that strengthen faith and character.",
            "bird": "Soul's aspirations or divine messages. Color indicates nature of message.",
            "book": "Divine guidance or record of deeds. Reading means understanding divine will.",
            "ocean": "The ocean of divine knowledge and infinite mercy.",
            "mountain": "Steadfastness in faith or major obstacles in spiritual path.",
            "rain": "Divine mercy, spiritual nourishment, and answers to prayers.",
            "sun": "Divine light, guidance, or spiritual illumination.",
            "moon": "Spiritual beauty, inner light, or reflection of divine attributes."
        }
        
        # Create FAISS index for similarity search
        self.setup_similarity_index()
    
    def setup_similarity_index(self):
        """Create FAISS index for dream element matching"""
        all_elements = list(set(list(self.ibn_sirin_db.keys()) + list(self.nabulsi_db.keys())))
        self.dream_elements = all_elements
        
        # Generate embeddings
        embeddings = self.similarity_model.encode(all_elements)
        self.index = faiss.IndexFlatL2(embeddings.shape[1])
        self.index.add(embeddings.astype('float32'))
    
    def extract_dream_elements(self, dream_text: str) -> List[str]:
        """Extract key elements from dream text"""
        # Simple keyword extraction (in production, use more sophisticated NLP)
        words = dream_text.lower().split()
        elements = []
        
        for element in self.dream_elements:
            if element in dream_text.lower():
                elements.append(element)
        
        return elements[:5]  # Return top 5 elements
    
    def get_ibn_sirin_interpretation(self, elements: List[str]) -> str:
        """Get interpretation based on Ibn Sirin's teachings"""
        interpretations = []
        for element in elements:
            if element in self.ibn_sirin_db:
                interpretations.append(f"• {element.capitalize()}: {self.ibn_sirin_db[element]}")
        
        if interpretations:
            return "\n\n".join(interpretations)
        else:
            return "Ibn Sirin teaches that dreams should be interpreted by their most obvious meanings. Consider the context and your current life situation."
    
    def get_nabulsi_interpretation(self, elements: List[str]) -> str:
        """Get interpretation based on Sheikh Nabulsi's teachings"""
        interpretations = []
        for element in elements:
            if element in self.nabulsi_db:
                interpretations.append(f"• {element.capitalize()}: {self.nabulsi_db[element]}")
        
        if interpretations:
            return "\n\n".join(interpretations)
        else:
            return "Sheikh Nabulsi emphasizes the spiritual dimensions of dreams. Reflect on your spiritual state and relationship with Allah."
    
    def generate_comprehensive_interpretation(self, dream_text: str, elements: List[str]) -> str:
        """Generate AI-powered comprehensive interpretation"""
        base_prompt = f"""
        Dream: {dream_text}
        
        Key elements identified: {', '.join(elements)}
        
        Based on Islamic dream interpretation principles from Ibn Sirin and Sheikh Nabulsi, provide a comprehensive analysis considering:
        1. Spiritual significance
        2. Psychological aspects  
        3. Practical implications
        4. Islamic perspective
        
        Interpretation:
        """
        
        try:
            response = self.generator(base_prompt, max_length=600, num_return_sequences=1)
            return response[0]['generated_text'].split('Interpretation:')[-1].strip()
        except:
            return "AI interpretation is currently unavailable. Please refer to the scholars' interpretations above."

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
    }
    .scholar-header {
        font-size: 1.8rem;
        color: #A23B72;
        margin-bottom: 1rem;
        font-weight: bold;
    }
    .dream-input {
        font-size: 1.2rem;
        font-weight: bold;
    }
    .interpretation-box {
        background-color: #f0f8ff;
        padding: 20px;
        border-radius: 10px;
        border-left: 5px solid #2E86AB;
        margin: 10px 0;
    }
    .footer {
        text-align: center;
        margin-top: 3rem;
        color: #666;
        font-size: 0.9rem;
    }
    </style>
    """, unsafe_allow_html=True)
    
    # Header
    st.markdown('<div class="main-header">🌙 Islamic Dream Interpreter</div>', unsafe_allow_html=True)
    
    # Initialize interpreter
    if 'interpreter' not in st.session_state:
        st.session_state.interpreter = DreamInterpreter()
    
    # Dream input section
    st.markdown("### 📝 Describe Your Dream")
    dream_text = st.text_area(
        "Write your dream in detail:",
        height=200,
        placeholder="Describe your dream here... Be as detailed as possible about people, objects, colors, emotions, and events.",
        key="dream_input"
    )
    
    # Interpretation button
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        interpret_btn = st.button("🔮 Interpret Dream", use_container_width=True)
    
    if interpret_btn and dream_text:
        with st.spinner("Analyzing your dream..."):
            # Extract dream elements
            elements = st.session_state.interpreter.extract_dream_elements(dream_text)
            
            # Get interpretations
            ibn_sirin = st.session_state.interpreter.get_ibn_sirin_interpretation(elements)
            nabulsi = st.session_state.interpreter.get_nabulsi_interpretation(elements)
            ai_interpretation = st.session_state.interpreter.generate_comprehensive_interpretation(dream_text, elements)
        
        # Display results in tabs
        tab1, tab2, tab3 = st.tabs(["🧔 Ibn Sirin", "📚 Sheikh Nabulsi", "🤖 Comprehensive Analysis"])
        
        with tab1:
            st.markdown('<div class="scholar-header">Interpretation based on Ibn Sirin\'s Teachings</div>', unsafe_allow_html=True)
            st.markdown(f'<div class="interpretation-box">{ibn_sirin}</div>', unsafe_allow_html=True)
        
        with tab2:
            st.markdown('<div class="scholar-header">Interpretation based on Sheikh Abdul Ghani Nabulsi\'s Teachings</div>', unsafe_allow_html=True)
            st.markdown(f'<div class="interpretation-box">{nabulsi}</div>', unsafe_allow_html=True)
        
        with tab3:
            st.markdown('<div class="scholar-header">AI-Powered Comprehensive Analysis</div>', unsafe_allow_html=True)
            st.markdown(f'<div class="interpretation-box">{ai_interpretation}</div>', unsafe_allow_html=True)
        
        # Dream elements identified
        if elements:
            st.info(f"**Key elements identified:** {', '.join([elem.capitalize() for elem in elements])}")
    
    elif interpret_btn and not dream_text:
        st.warning("Please describe your dream first!")
    
    # Sidebar with information
    with st.sidebar:
        st.markdown("## ℹ️ About")
        st.info("""
        This Islamic Dream Interpreter is based on the works of:
        
        **• Ibn Sirin** - Famous 8th-century Islamic scholar
        **• Sheikh Abdul Ghani Nabulsi** - 17th-century Sufi scholar
        
        Both are renowned authorities in Islamic dream interpretation.
        """)
        
        st.markdown("## 📖 Dream Interpretation Tips")
        st.write("""
        1. Write dreams immediately after waking
        2. Include details about emotions
        3. Note colors, numbers, and people
        4. Consider your current life situation
        5. Remember that not all dreams have interpretations
        """)
        
        st.markdown("## ⚠️ Disclaimer")
        st.write("""
        This tool provides general interpretations based on Islamic scholarship. 
        For personal guidance, consult knowledgeable scholars.
        Dreams should be understood in their proper Islamic context.
        """)
    
    # Footer
    st.markdown("""
    <div class="footer">
    <hr>
    <p>🌙 Islamic Dream Interpreter • Based on Authentic Islamic Scholarship • May Allah guide us to understand the wisdom behind our dreams</p>
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()