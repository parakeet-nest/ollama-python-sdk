import os
import ollama 
from ollama import Client 

ollama_client = Client(host='http://host.docker.internal:11434')
#ollama_client = Client(host='http://ollama-service:11434')

with open('./instructions.md', 'r') as file:
    instructions = file.read()
with open('./description.md', 'r') as file:
    description = file.read()

while True:
    user_input = input("🤖 (type 'bye' to exit):> ")
    if user_input.lower() == "bye":
        print("👋 Goodbye!")
        break
    else:
        stream = ollama_client.chat(
            model='nemotron-mini',
            messages=[
              {'role': 'system', 'content': instructions},
              {'role': 'system', 'content': description},
              {'role': 'user', 'content': user_input},
            ],
            options={"temperature":0.8},
            stream=True,
            keep_alive=-1,
        )

        for chunk in stream:
          print(chunk['message']['content'], end='', flush=True)

        print("\n")


# some questions to ask:
# what is your name?
# give me the list without detail of your qualities
# where are you from?
# where are you located?
# where are you living?
# where did you grow up?
# who is your best friend?
# who is your worst enemy?
# give me the list without detail of all your friends
# give me the list without detail of all your enemies