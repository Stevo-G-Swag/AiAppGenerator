import streamlit as st

def apply_custom_styles():
    st.markdown("""
        <style>
        /* Main container */
        .main .block-container {
            padding-top: 2rem;
            padding-bottom: 2rem;
        }
        
        /* Headers */
        h1, h2, h3 {
            color: #FF4B4B;
            font-family: 'Monaco', monospace;
        }
        
        /* Code blocks */
        .stCodeBlock {
            border-radius: 5px;
            background-color: #1E1E1E;
        }
        
        /* Buttons */
        .stButton button {
            width: 100%;
            border-radius: 5px;
            background: linear-gradient(45deg, #FF4B4B, #FF8F8F);
            border: none;
            color: white;
            font-weight: bold;
            transition: all 0.3s ease;
        }
        
        .stButton button:hover {
            transform: translateY(-2px);
            box-shadow: 0 5px 15px rgba(255, 75, 75, 0.3);
        }
        
        /* Progress bars */
        .stProgress > div > div {
            background-color: #FF4B4B;
        }
        
        /* Text areas */
        .stTextArea textarea {
            border-radius: 5px;
            border: 1px solid #FF4B4B;
            background-color: #1E1E1E;
        }
        
        /* Expanders */
        .streamlit-expanderHeader {
            background-color: #262730;
            border-radius: 5px;
        }
        </style>
    """, unsafe_allow_html=True)
