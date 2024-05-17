from langchain_community.llms import Ollama

llm = Ollama(model="mario")

print(llm.invoke("How are you?"))
