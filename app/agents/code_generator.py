from app.utils.openai_client import get_completion
from app.utils.code_validator import validate_syntax
import json

class CodeGenerator:
    async def generate(self, project_spec: dict) -> dict:
        generated_files = {}
        
        for component in project_spec["components"]:
            prompt = f"""
            Generate code for the following component:
            {json.dumps(component)}
            
            Follow these guidelines:
            - Use modern best practices
            - Include error handling
            - Add comprehensive comments
            - Follow PEP 8 style guide
            
            Response should be valid Python code.
            """
            
            code = await get_completion(prompt)
            
            # Validate syntax
            if validate_syntax(code):
                generated_files[component["path"]] = code
            else:
                raise Exception(f"Invalid syntax in generated code for {component['path']}")
        
        return generated_files
