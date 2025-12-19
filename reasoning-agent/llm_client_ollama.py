import ollama

class LLMClient:
  
    def __init__(self, model_name="phi3:mini"):
        self.model_name = model_name

    def generate(self, prompt: str) -> str:
        try:
            response = ollama.chat(
                model=self.model_name,
                messages=[
                    {"role": "user", "content": prompt}
                ]
            )
            return response["message"]["content"].strip()
        except Exception as e:
            return f"Error generating response: {e}"