import  json

def response(prompt) :
    if prompt in ( "hello",  "hi",  "hey",  "howdy",  "helo",  "hiy") :
        return "Hi there!"
    elif "your name" in prompt:
        return "I'm a simple Chatbot!"
    else : 
        return "You asked: " + prompt

conversation_history = []

with open("chat_history.json", "r") as file:
    conversation_history = json.load(file)

while True:
    prompt = input("Ask (Ex. 'Hello') (to exit Type 'exit'): ").lower().strip()
    res = response(prompt)
    if prompt == "exit" :
        break
    elif prompt == "history" :
        for i in conversation_history :
            print(i)
    else: 
        print(res)
        conversation_history.append({"prompt":prompt,"response":res})
        with open("chat_history.json", "w") as file:
            json.dump(conversation_history,file)