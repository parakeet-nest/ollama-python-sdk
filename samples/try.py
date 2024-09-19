import os
import ollama 
from ollama import Client


ollama_client = Client(host='http://host.docker.internal:11434')
#ollama_client = Client(host='http://ollama-service:11434')


stream = ollama_client.chat(
    model='qwen:0.5b',
    messages=[{'role': 'user', 'content': '[Brief]What is the best pizza of the world'}],
    stream=True,
)


for chunk in stream:
  print(chunk['message']['content'], end='', flush=True)

print("\n🍕")
