from langchain_ollama import OllamaLLM
from langchain_core.prompts import PromptTemplate

# Load Model
llm = OllamaLLM(model="phi3:mini")

# Prompt Template
prompt = PromptTemplate(
    input_variables=["topic"],
    template="Explain {topic} in simple words"
)

# Create Chain
chain = prompt | llm

# Invoke Chain
response = chain.invoke({"topic": "Deep Learning"})

# Print Response
print(response)