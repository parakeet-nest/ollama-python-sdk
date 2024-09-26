import os
import ollama 
from ollama import Client


ollama_client = Client(host='http://host.docker.internal:11434')
#ollama_client = Client(host='http://ollama-service:11434')


stream = ollama_client.chat(
    model='qwen2.5-coder:1.5b',
    messages=[
      {'role': 'user', 'content': '''generate a Dockerfile for a golang application, 
               using the nulti stage build and the final image is a scratch image'''
      }
    ],
    stream=True,
)


for chunk in stream:
  print(chunk['message']['content'], end='', flush=True)

print("\n🍕")
