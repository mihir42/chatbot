# SIMPLE CHATBOT

#json for saving chat history.
import  json

def response(prompt) :
    if prompt in ( "hello", "hi", "hey", "howdy", "helo") :
        return "Hi there!"
    elif "your name" in prompt:
        return "I'm a simple Chatbot!"
    else : 
        return f"You asked: {prompt}"

conversation_history = []

#try/except for the first time the progran is run.
try:
    with open("chat_history.json", "r") as file:
        conversation_history = json.load(file)
except FileNotFoundError:
    conversation_history = []

print("This is a simple chatbot, Say Hi, Hello, What's your name? or type 'exit' to leave.")

while True:
    prompt = input("Ask: ").lower().strip()

    if prompt == "exit" :
        break
    elif prompt == "history" :
        for i in conversation_history:
            print(f"\nYou: {i['Prompt']}")
            print(f"Bot: {i['Response']}")
    else: 
        res = response(prompt)
        print(res)
        conversation_history.append({"Prompt":prompt, "Response":res})
        with open("chat_history.json", "w") as file:
            json.dump(conversation_history, file, indent=2)