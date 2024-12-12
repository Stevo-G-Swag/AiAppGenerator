from utils.openai_client import get_completion
import json

class ProjectManager:
    async def create_specification(self, description: str) -> dict:
        prompt = f"""
        Act as a project manager and create a detailed specification for the following application:
        
        {description}
        
        Generate a JSON response with the following structure:
        {{
            "structure": {{directory structure}},
            "components": [list of required components],
            "dependencies": [required dependencies],
            "features": [detailed feature specifications]
        }}
        """
        
        response = await get_completion(prompt)
        return json.loads(response)
