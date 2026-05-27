from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()
client = Groq(api_key=os.getenv('GROQ_API_KEY'))

resposta = client.chat.completions.create(
    model='openai/gpt-oss-120b',        
    max_tokens=2000,                     
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