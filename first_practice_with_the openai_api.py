from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

resposta = client.chat.completions.create(
    model='gpt-4o-mini',
    max_tokens=500,                     
    temperature=0.7,                    
    messages=[
        {
            'role': 'system',
            'content': 'Você é um assistente educacional.'
        },
        {
            'role': 'user',
            'content': 'O que é Python em uma frase?'
        }
    ]
)

texto = resposta.choices[0].message.content
print(texto)

print(f'Tokens usados: {resposta.usage.total_tokens}')