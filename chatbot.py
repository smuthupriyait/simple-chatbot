import random  # Importing the random module for random response selection

# A simple chatbot class
class SimpleChatbot:
    def __init__(self):
        # Initialize the chatbot with predefined responses
        self.responses = {
            "hi": ["Hello!", "Hi there!", "Greetings!", "Howdy!"],
            "hello": ["Hello!", "Hi there!", "Greetings!", "Howdy!"],
            "how are you": ["I'm good, thank you!", "Doing well, how about you?", "I'm just a bunch of code, but thanks for asking!"],
            "what's your name": ["I'm a simple chatbot.", "You can call me Chatbot.", "I'm a bot without a name!"],
            "bye": ["Goodbye!", "See you later!", "Take care!"],
            "help": ["I can chat with you! Just say 'hi', 'bye', or ask me about myself!"],
            "what do you do": ["I chat with you!", "I am here to have conversations!", "I'm designed to chat!"],
            "tell me a joke": ["Why did the scarecrow win an award? Because he was outstanding in his field!", 
                               "Why don't scientists trust atoms? Because they make up everything!"],
            "how's the weather": ["I'm not sure, I don't have access to real-time weather data!", 
                                  "I can't check the weather, but I hope it's nice where you are!"]
        }

    # Get response based on user input
    def get_response(self, user_input):
        # Normalize the user input to lowercase and remove extra spaces
        user_input = user_input.lower().strip()
        
        # Check the user input against the predefined responses
        for key in self.responses:
            # If the key is found in the user input, return a random response
            if key in user_input:
                return random.choice(self.responses[key])
        
        # Default response if no keywords match
        return "Sorry, I don't understand that."

# Main function to run the chatbot
def main():
    # Create an instance of the chatbot
    chatbot = SimpleChatbot()
    print("Chatbot: Hi! I'm a chatbot. Type 'bye' to exit.")  # Welcome message
    
    # Infinite loop to keep the conversation going
    while True:
        user_input = input("You: ")  # Get input from the user
        if user_input.lower() == "bye":  # Check for exit command
            print("Chatbot: Goodbye!")  # Farewell message
            break  # Exit the loop
        response = chatbot.get_response(user_input)  # Get the chatbot's response
        print(f"Chatbot: {response}")  # Output the chatbot's response

# Entry point of the program
if __name__ == "__main__":
    main()  # Run the main function

