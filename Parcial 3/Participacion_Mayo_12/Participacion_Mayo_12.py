from openai import OpenAI
import os
from dotenv import load_dotenv

SYSTEM_MESSAGE = "Responde en Español a menos que el usuario te hable en otro idioma. Usa respuestas cortas. Usa un tono muy amigable."

if __name__ == "__main__":
    load_dotenv()
    URL = os.environ.get('OPENAI_BASE_URL')
    KEY = os.environ.get('OPENAI_KEY')
    MODEL = os.environ.get('MODEL')

    client = OpenAI(
        base_url=URL,
        api_key=KEY,
    )

    print(f"Chatting with {MODEL} model at {URL}\n")

    messages_list = []
    messages_list.append({'role': 'system', 'content': SYSTEM_MESSAGE})

    while True:
        user_message = input("> ")

        messages_list.append({'role': 'user', 'content': user_message})

        response = client.chat.completions.create(
            model=MODEL,
            messages=messages_list
        )

        assistant_text = response.choices[0].message.content

        messages_list.append({"role": "assistant", "content": assistant_text})

        print(assistant_text)
