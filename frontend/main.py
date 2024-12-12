import streamlit as st
from components import (
    render_header,
    render_input_section,
    render_agent_visualization,
    render_code_output,
)
from styles import apply_custom_styles
import asyncio
import httpx

# Configure page settings
st.set_page_config(
    page_title="AI App Generator",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Apply custom styles
apply_custom_styles()

async def main():
    # Initialize session state
    if 'generated_code' not in st.session_state:
        st.session_state.generated_code = {}
    if 'current_step' not in st.session_state:
        st.session_state.current_step = 'input'
    
    # Render header
    render_header()
    
    # Main content area
    col1, col2 = st.columns([2, 3])
    
    with col1:
        user_input = render_input_section()
        
        if st.button("Generate Application", type="primary"):
            st.session_state.current_step = 'generating'
            
            async with httpx.AsyncClient() as client:
                response = await client.post(
                    "http://localhost:8000/generate",
                    json={"description": user_input}
                )
                if response.status_code == 200:
                    st.session_state.generated_code = response.json()
                    st.session_state.current_step = 'complete'
                else:
                    st.error("Error generating application")
    
    with col2:
        if st.session_state.current_step == 'generating':
            render_agent_visualization()
        elif st.session_state.current_step == 'complete':
            render_code_output(st.session_state.generated_code)

if __name__ == "__main__":
    asyncio.run(main())
