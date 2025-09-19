import os

print("""
  ____ _               _       _      
 / ___| |__   ___  ___| | __ _| |__   
| |   | '_ \ / _ \/ __| |/ _` | '_ \  
| |___| | | |  __/ (__| | (_| | |_) | 
 \____|_| |_|\___|\___|_|\__,_|_.__/  

Termux Chatbot - Type 'exit' to quit
""")

while True:
    user_input = input("You: ")
    if user_input.lower() == 'exit':
        print("Bot: Goodbye!")
        os.system('espeak "Goodbye!"')
        break

    bot_response = f"You said: {user_input}"
    print("Bot:", bot_response)
    os.system(f'espeak "{bot_response}"')

