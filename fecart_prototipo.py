from google import genai


client = genai.Client(api_key='AIzaSyClaR5XlKEjT6KUComKEK8MjAMOaKjso1g')
chat = client.chats.create(model="gemini-2.5-flash")

while True:
    pergunta = input("Digite a pergunta que você quer fazer para Einstein. (Digite 'sair' se quiser parar de fazer perguntas): ")

    if pergunta.lower() == 'sair':
        break 

    context_response = chat.send_message("Finja que você é o einstein e responda as perguntas como se fosse ele. E responda de forma curta e objetiva")
    response = chat.send_message(pergunta)
        
        

    print(response.text)
    

print("Conversa encerrada. Até logo!")