import requests

#Necessário criar o bot do telegram para pegar as informações abaixo.
TOKEN = 'insira o token do bot telegram aqui.'
chat_id = 'Insira o id do chat aqui.'
message = 'Teste de alerta!'
url = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={chat_id}&text={message}"
requests.get(url)