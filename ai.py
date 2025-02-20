import google.generativeai as ai
API_KEY = 'AIzaSyBfD1WCnKKdIA2vVrveX-lkoNcmaV9kO3c'
ai.configure(api_key=API_KEY)
model=ai.GenerativeModel("gemini-pro")
chat=model.start_chat()
while True:
    message=input("You : ")
    if message.islower() == 'bye':
        print("Chatbot : Goodbye")
        break
    response=chat.send_message(message)
    print("Chatbot :",response.text) 