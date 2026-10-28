# SIMPLE CHATBOT

#json for saving chat history.
import  json
import random

def response(prompt) :
    if prompt in ( "Hello", "Hi", "Hey", "Howdy", "Helo") :
        return random.choice (["Hi there!", "Hello!","Hey!"])
    elif "your name" in prompt:
        return "I'm a simple Chatbot!"
    elif "how are you" in prompt or "How are you" in prompt:
        return "I can't feel things :)"
    else : 
        return f"You asked: {prompt}"

conversation_history = []

#try/except for the first time the program is run.
try:
    with open("chat_history.json", "r") as file:
        conversation_history = json.load(file)
except FileNotFoundError:
    conversation_history = []

print("\nSIMPLE CHATBOT")
print("Say Hi, Hello, How are you?, What's your name? or type 'Exit' to leave.")

while True:
    prompt = input("\nAsk: ").lower().strip().capitalize()

    if prompt == "Exit" :
        print("BYE")
        break
    elif prompt == "":
        print("No prompt entered.")
    elif prompt == "History" :
        for i in conversation_history:
            print(f"\nYou: {i['Prompt']}")
            print(f"Bot: {i['Response']}")
    else: 
        res = response(prompt)
        print(res)
        conversation_history.append({"Prompt":prompt, "Response":res})
        with open("chat_history.json", "w") as file:
            json.dump(conversation_history, file, indent=2)