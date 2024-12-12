from app.utils.openai_client import get_completion
import json

class ProjectManager:
    async def create_specification(self, description: str) -> dict:
        prompt = f"""
        Act as a senior project manager and create a detailed specification for the following application:
        
        {description}
        
        Please provide the specification in a valid JSON format. Return a JSON object with the following structured format:
        {{
            "structure": {{
                "directories": {{
                    "frontend": ["List of frontend files and their purposes"],
                    "backend": ["List of backend files and their purposes"],
                    "database": ["Database related files"],
                    "utils": ["Utility modules"]
                }}
            }},
            "components": [
                {{
                    "name": "Component name",
                    "path": "File path where this component should be created",
                    "purpose": "Component's main purpose",
                    "dependencies": ["Required dependencies"],
                    "code_structure": {{
                        "imports": ["Required imports"],
                        "classes": ["Classes to implement"],
                        "functions": ["Functions to implement"]
                    }}
                }}
            ],
            "dependencies": {{
                "frontend": ["Frontend dependencies"],
                "backend": ["Backend dependencies"],
                "development": ["Development dependencies"]
            }},
            "features": [
                {{
                    "name": "Feature name",
                    "description": "Detailed feature description",
                    "implementation_steps": ["Step by step implementation guide"],
                    "required_components": ["Components needed for this feature"]
                }}
            ],
            "api_endpoints": [
                {{
                    "path": "Endpoint path",
                    "method": "HTTP method",
                    "purpose": "Endpoint purpose",
                    "request_body": "Expected request structure",
                    "response": "Expected response structure"
                }}
            ]
        }}
        
        Ensure the specification is detailed and follows modern best practices for the specified project type.
        Include error handling, testing requirements, and security considerations in the JSON response.
        """
        
        response = await get_completion(prompt)
        return json.loads(response)
