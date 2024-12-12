import os
from openai import OpenAI

# the newest OpenAI model is "gpt-4o" which was released May 13, 2024.
# do not change this unless explicitly requested by the user
MODEL = "gpt-4o"

client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY", "sk-bks-345a5718b2ca468315468beaff14415da14fd8c1dfcd131a"),
    base_url="https://api.trybricks.ai/api/providers/openai/v1"
)

async def get_completion(prompt: str) -> str:
    try:
        response = client.chat.completions.create(
            model=MODEL,
            messages=[
                {"role": "system", "content": "You are an expert software developer assistant."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,
            response_format={"type": "json_object"}
        )
        return response.choices[0].message.content
    except Exception as e:
        raise Exception(f"OpenAI API error: {str(e)}")
