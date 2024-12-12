from utils.openai_client import get_completion

class DocumentationAgent:
    async def generate(self, project_spec: dict, generated_code: dict) -> str:
        prompt = f"""
        Generate comprehensive documentation for the following project:
        
        Specification:
        {project_spec}
        
        Include:
        1. Project Overview
        2. Installation Instructions
        3. Usage Guide
        4. API Documentation
        5. Component Documentation
        6. Troubleshooting Guide
        
        Format the response in Markdown.
        """
        
        documentation = await get_completion(prompt)
        return documentation
