import tkinter as tk
import random

respostas = {
    "oi": ["Olá!", "Oi! Tudo bem?", "E aí!"],
    "tudo bem": ["Tudo ótimo!", "Sim, e você?", "Indo bem!"],
    "python": ["Python é ótimo para IA!", "Você está estudando Python?"],
    "ia": ["IA é fascinante!", "Inteligência Artificial está em todo lugar!"]
}

def responder(msg):
    msg = msg.lower()
    for chave in respostas:
        if chave in msg:
            return random.choice(respostas[chave])
    return "Não entendi, pode reformular?"

def enviar():
    msg = entrada.get()
    
    if msg.strip() == "":
        return
    
    chat.insert(tk.END, "Você: " + msg + "\n")
    
    resposta = responder(msg)
    chat.insert(tk.END, "Bot: " + resposta + "\n\n")
    
    entrada.delete(0, tk.END)

# Interface
janela = tk.Tk()
janela.title("Chatbot IA - Simples")

chat = tk.Text(janela, height=50, width=90)
chat.pack()

entrada = tk.Entry(janela, width=40)
entrada.pack(side=tk.LEFT, padx=5, pady=5)

botao = tk.Button(janela, text="Enviar", command=enviar)
botao.pack(side=tk.LEFT)

janela.mainloop()