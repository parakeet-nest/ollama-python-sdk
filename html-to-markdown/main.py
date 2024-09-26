#import ollama 
from ollama import Client

ollama_client = Client(host='http://host.docker.internal:11434')
#ollama_client = Client(host='http://ollama-service:11434')


def html_to_markdown(model: str, html: str):
    
    options = {
      'temperature': 0.0,
      'top_p': 0.5,
      'top_k': 10,
      'repeat_last_n': 2,
      'repeat_penalty': 2.0
    }

    stream = ollama_client.chat(
        model=model,
        messages=[
           {'role': 'user', 'content': html},
        ],
        stream=True,
        options= options,
    )

    for chunk in stream:
      print(chunk['message']['content'], end='', flush=True)

html_page = '''
<html>
  <body>
    <h3>Why is the sky blue?</h3>
    <p>The sky appears blue because of the way light from the sun is reflected by the atmosphere. The atmosphere is made up of gases, including nitrogen and oxygen, which scatter light in all directions. This scattering causes the sunlight to appear as a rainbow of colors, with red light scattered more than other colors.
    </p>
  </body>
</html>
'''

#html_to_markdown("reader-lm:1.5b", html_page)

html_to_markdown("reader-lm:0.5b", html_page)


print("\n")


