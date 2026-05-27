let historico = [];

async function enviarMensagem() { 
 const input = document.getElementById('input');  
 const mensagem = input.value.trim();
   
 if (!mensagem) return;
  
 input.value = '';
 
 const resposta = await fetch('/chat', { 
    method: 'POST',    
    headers: { 'Content-Type': 'application/json' },    
    body: JSON.stringify({ mensagem: mensagem, historico: historico })  
    });
 const dados = await resposta.json();
 console.log(dados.resposta)
 }               