from llm_client import OllamaProvider, LLMClient

# Initialize Ollama local provider
provider = OllamaProvider("llama3.2")
client = LLMClient(provider)

prompt = input("Enter your question: ")
answer = client.generate(prompt)

print("\nLLM Response:")
print(answer)
