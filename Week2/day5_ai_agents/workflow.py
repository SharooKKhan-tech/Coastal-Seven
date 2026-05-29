from langchain_ollama import OllamaLLM
from langchain_core.prompts import PromptTemplate

# Load Model
llm = OllamaLLM(model="phi3:mini")

# First Prompt
explain_prompt = PromptTemplate(
    input_variables=["topic"],
    template="Explain {topic} in detail"
)

# Second Prompt
summary_prompt = PromptTemplate(
    input_variables=["text"],
    template="Summarize the following text in 3 lines:\n{text}"
)

# First Chain
explain_chain = explain_prompt | llm

# Second Chain
summary_chain = summary_prompt | llm


# Step 1: Generate Explanation
explanation = explain_chain.invoke({
    "topic": "Machine Learning"
})

print("\nDetailed Explanation:\n")
print(explanation)

print("\n====================\n")


# Step 2: Generate Summary
summary = summary_chain.invoke({
    "text": explanation
})

print("\nSummary:\n")
print(summary)