import streamlit as st
import time

def render_header():
    st.markdown("""
        <h1 style='text-align: center; margin-bottom: 2rem;'>
            🤖 AI Application Generator
        </h1>
    """, unsafe_allow_html=True)

def render_input_section():
    st.markdown("### Describe Your Application")
    user_input = st.text_area(
        "Enter your application requirements in natural language:",
        height=200,
        placeholder="Example: Create a todo list application with user authentication..."
    )
    
    with st.expander("Advanced Options"):
        st.selectbox(
            "Project Type",
            ["Web Application", "REST API", "Mobile App"],
            index=0
        )
        st.multiselect(
            "Features",
            ["Authentication", "Database", "API Integration", "File Upload"],
            default=["Authentication"]
        )
    
    return user_input

def render_agent_visualization():
    st.markdown("### AI Agents at Work")
    
    agents = {
        "Project Manager": "🎯",
        "Code Generator": "💻",
        "Testing": "🧪",
        "Documentation": "📝"
    }
    
    for agent, emoji in agents.items():
        col1, col2 = st.columns([1, 4])
        with col1:
            st.markdown(f"### {emoji}")
        with col2:
            progress = st.progress(0)
            for i in range(100):
                time.sleep(0.01)
                progress.progress(i + 1)
            st.success(f"{agent} completed!")

def render_code_output(generated_code):
    st.markdown("### Generated Application")
    
    tabs = st.tabs(["Project Structure", "Code", "Documentation"])
    
    with tabs[0]:
        st.json(generated_code.get("structure", {}))
    
    with tabs[1]:
        for file_path, code in generated_code.get("files", {}).items():
            with st.expander(file_path):
                st.code(code, language="python")
    
    with tabs[2]:
        st.markdown(generated_code.get("documentation", ""))
