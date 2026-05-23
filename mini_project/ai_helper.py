import requests


class AIHelper:

    def __init__(self):
        self.url = "http://localhost:11434/api/generate"
        self.model = "llama3"

    def get_recommendations(self, task):

        prompt = f"""
        A student wants to complete this task:

        {task}

        Suggest 3 short learning recommendations.
        """

        payload = {
            "model": self.model,
            "prompt": prompt,
            "stream": False
        }

        try:
            response = requests.post(self.url, json=payload)

            data = response.json()

            return data["response"]

        except Exception as e:
            return f"Error connecting to Ollama: {e}"