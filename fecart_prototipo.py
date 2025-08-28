from google import genai


client = genai.Client(api_key='AIzaSyClaR5XlKEjT6KUComKEK8MjAMOaKjso1g')
chat = client.chats.create(model="gemini-2.5-flash")
print('''
1- Einstein
2- Marie Curie
3- Alexandre, O grande
4- Rosa Parks
5- Alexander Fleming
                ''')
persona = input("Digite (entre os listados acima) o qual deseja conversar: ")
while True:
    pergunta = input(f"Digite a pergunta que você quer fazer para {persona}. (Digite 'sair' se quiser parar de fazer perguntas): ")

    if pergunta.lower() == 'sair':
        break 

    context_response = chat.send_message(f"Finja que você é o {persona} e responda as perguntas como se fosse ele. E responda como se estivesse em uma conversa com uma pessoas porém de forma curta e objetiva")
    response = chat.send_message(pergunta)

    print(response.text)
    
print("Conversa encerrada. Até logo!")