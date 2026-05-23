import requests


class AIHelper:

    def __init__(self):

        self.url = "http://localhost:11434/api/generate"
        self.model = "phi3:mini"

    def explain_topic(self, topic):

        prompt = f"""
        Explain {topic} for a beginner in simple words.
        Give short and easy explanation.
        """

        return self.ask_ollama(prompt)

    def generate_roadmap(self, topic):

        prompt = f"Give 5 short steps to learn {topic}."

        return self.ask_ollama(prompt)

    def ask_ollama(self, prompt):

        payload = {
            "model": self.model,
            "prompt": prompt,
            "stream": False,
            "options": {
                "num_predict": 220
            }
        }

        try:

            response = requests.post(
                self.url,
                json=payload,
                timeout=180
            )

            response.raise_for_status()

            data = response.json()

            return data["response"]

        except requests.exceptions.ConnectionError:
            return "Error: Ollama is not running."

        except requests.exceptions.Timeout:
            return "Error: AI response timed out."

        except Exception as e:
            return f"Error: {e}"