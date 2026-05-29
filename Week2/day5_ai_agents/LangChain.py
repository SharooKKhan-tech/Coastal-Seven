from langchain_ollama import OllamaLLM
from langchain_core.prompts import PromptTemplate
# Load Model
llm = OllamaLLM(model="phi3:mini")

# Create Prompt Template
template = PromptTemplate(
    input_variables=["topic"],
    template="Explain {topic} in simple words"
)

# Create Prompt
prompt = template.format(topic="Neural Networks")

# Generate Response
response = llm.invoke(prompt)

print(response)