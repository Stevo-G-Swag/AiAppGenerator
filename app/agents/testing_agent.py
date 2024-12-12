from app.utils.openai_client import get_completion
import json

class TestingAgent:
    async def validate(self, generated_code: dict) -> dict:
        validation_results = {
            "passed": True,
            "tests": []
        }
        
        for file_path, code in generated_code.items():
            prompt = f"""
            Analyze the following code and generate test cases:
            
            {code}
            
            Provide a JSON response with:
            {{
                "test_cases": [list of test cases],
                "security_checks": [security validation results],
                "code_quality": {{quality metrics}}
            }}
            """
            
            response = await get_completion(prompt)
            test_result = json.loads(response)
            
            validation_results["tests"].append({
                "file": file_path,
                "results": test_result
            })
            
            if test_result.get("security_checks", []):
                validation_results["passed"] &= all(test_result["security_checks"])
        
        return validation_results
