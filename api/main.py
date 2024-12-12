from fastapi import FastAPI, HTTPException
from api.models import AppRequest, AppResponse
from agents.project_manager import ProjectManager
from agents.code_generator import CodeGenerator
from agents.testing_agent import TestingAgent
from agents.documentation_agent import DocumentationAgent

app = FastAPI(title="AI App Generator API")

@app.post("/generate", response_model=AppResponse)
async def generate_application(request: AppRequest):
    try:
        # Initialize agents
        project_manager = ProjectManager()
        code_generator = CodeGenerator()
        testing_agent = TestingAgent()
        documentation_agent = DocumentationAgent()
        
        # Project planning phase
        project_spec = await project_manager.create_specification(request.description)
        
        # Code generation phase
        generated_code = await code_generator.generate(project_spec)
        
        # Testing phase
        test_results = await testing_agent.validate(generated_code)
        if not test_results["passed"]:
            raise HTTPException(status_code=400, detail="Code validation failed")
        
        # Documentation phase
        documentation = await documentation_agent.generate(
            project_spec,
            generated_code
        )
        
        return AppResponse(
            structure=project_spec["structure"],
            files=generated_code,
            documentation=documentation,
            test_results=test_results
        )
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
