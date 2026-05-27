from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
client = OpenAI(
    api_key=os.getenv("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1",
)

SYSTEM_PROMPT = 'Você é um assistente de programação educacional.'


historico = [{'role': 'system', 'content': SYSTEM_PROMPT}]

print('Chatbot iniciado! Digite "sair" para encerrar.\n')

while True:
    entrada = input('Você: ').strip()

    if entrada.lower() == 'sair':
        print('Encerrando. Até logo!')
        break

    if not entrada:
        continue

    historico.append({'role': 'user', 'content': entrada})

    try:
        resposta = client.chat.completions.create(
            model='openai/gpt-oss-20b',
            messages=historico,
            max_tokens=800
        )
        texto = resposta.choices[0].message.content

        historico.append({'role': 'assistant', 'content': texto})

        print(f'\nAssistente: {texto}\n')
    
    except Exception as e:
        print(f'Erro ao contactar a API: {e}')