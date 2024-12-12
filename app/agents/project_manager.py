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
                    "frontend": ["Streamlit UI files", "Component files", "Style definitions"],
                    "backend": ["FastAPI endpoints", "Business logic", "Data models"],
                    "database": ["Schema definitions", "Migration files"],
                    "utils": ["Helper functions", "Common utilities"]
                }},
                "files": [
                    {{
                        "path": "Path to the file",
                        "purpose": "Main purpose of this file",
                        "dependencies": ["Required dependencies"]
                    }}
                ]
            }},
            "components": [
                {{
                    "name": "Component name",
                    "path": "File path where this component should be created",
                    "purpose": "Detailed description of component's functionality",
                    "dependencies": ["Required dependencies"],
                    "code_structure": {{
                        "imports": ["Required imports with versions"],
                        "classes": [
                            {{
                                "name": "Class name",
                                "purpose": "Class purpose",
                                "attributes": ["List of attributes"],
                                "methods": ["List of methods"]
                            }}
                        ],
                        "functions": [
                            {{
                                "name": "Function name",
                                "purpose": "Function purpose",
                                "parameters": ["Expected parameters"],
                                "return_type": "Return type"
                            }}
                        ],
                        "error_handling": ["List of error scenarios to handle"]
                    }}
                }}
            ],
            "dependencies": {{
                "frontend": ["Frontend packages with versions"],
                "backend": ["Backend packages with versions"],
                "development": ["Development tools and testing packages"]
            }},
            "features": [
                {{
                    "name": "Feature name",
                    "description": "Detailed feature description",
                    "requirements": ["Functional requirements"],
                    "implementation_steps": [
                        {{
                            "step": "Step description",
                            "details": "Implementation details",
                            "validation": "How to validate this step"
                        }}
                    ],
                    "required_components": ["Components needed"],
                    "testing_strategy": ["Test cases to implement"]
                }}
            ],
            "api_endpoints": [
                {{
                    "path": "Endpoint path",
                    "method": "HTTP method",
                    "purpose": "Detailed endpoint purpose",
                    "request_body": {{
                        "type": "request type",
                        "fields": ["required fields"]
                    }},
                    "response": {{
                        "success": "Success response structure",
                        "error": "Error response structure"
                    }},
                    "validation": ["Validation rules"],
                    "authorization": "Required authorization level"
                }}
            ],
            "security": {{
                "authentication": ["Auth requirements"],
                "authorization": ["Access control rules"],
                "data_validation": ["Input validation rules"],
                "error_handling": ["Security-related error handling"]
            }}
        }}
        
        Ensure the specification is detailed, follows modern best practices, and includes:
        1. Comprehensive error handling strategies
        2. Security considerations and implementation
        3. Testing requirements and validation approaches
        4. Performance optimization guidelines
        5. Scalability considerations
        6. Maintainability best practices
        
        Format the response as a valid JSON object that can be parsed.
        """
        
        response = await get_completion(prompt)
        return json.loads(response)
