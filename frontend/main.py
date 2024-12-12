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
            
            try:
                async with httpx.AsyncClient(timeout=120.0) as client:
                    with st.spinner('Generating your application...'):
                        # Get the advanced options
                        col = st.columns(1)[0]
                        with col:
                            project_type = st.session_state.get('project_type', 'Web Application')
                            features = st.session_state.get('features', ['Authentication'])
                        
                        # Make the API request
                        response = await client.post(
                            "http://0.0.0.0:8000/generate",
                            json={
                                "description": user_input,
                                "project_type": project_type,
                                "features": features
                            },
                            timeout=120.0
                        )
                        
                        # Handle the response
                        if response.status_code == 200:
                            st.session_state.generated_code = response.json()
                            st.session_state.current_step = 'complete'
                            st.success('Application generated successfully!')
                        else:
                            error_detail = "Unknown error"
                            try:
                                error_response = response.json()
                                error_detail = error_response.get('detail', str(response.text))
                            except:
                                error_detail = str(response.text)
                            st.error(f"Error generating application: {error_detail}")
                            st.session_state.current_step = 'input'
                            
            except httpx.TimeoutError:
                st.error("Request timed out. The server took too long to respond. Please try again.")
                st.session_state.current_step = 'input'
            except httpx.ConnectError:
                st.error("Could not connect to the backend server. Please ensure the server is running.")
                st.session_state.current_step = 'input'
            except Exception as e:
                st.error(f"An unexpected error occurred: {str(e)}")
                st.session_state.current_step = 'input'
    
    with col2:
        if st.session_state.current_step == 'generating':
            render_agent_visualization()
        elif st.session_state.current_step == 'complete':
            render_code_output(st.session_state.generated_code)

if __name__ == "__main__":
    asyncio.run(main())
