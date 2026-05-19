def start_chatbot():
    print("Chatbot Initialized. Type 'bye' to exit.")
    
    # Dictionary routing for exact matches
    responses = {
        "hello": "Hi! How can I assist you today?",
        "how are you": "I'm functioning within normal parameters, thanks!",
        "bye": "Goodbye! Shutting down."
    }
    
    while True:
        # Edge Case Handling: Normalizing input
        user_input = input("You: ").strip().lower()
        
        # Remove punctuation that might break exact dictionary matching
        for char in ["?", "!", ".", ","]:
            user_input = user_input.replace(char, "")
            
        if user_input == "bye":
            print(f"Bot: {responses['bye']}")
            break
            
        # Route the response or provide a fallback
        if user_input in responses:
            print(f"Bot: {responses[user_input]}")
        else:
            print("Bot: Command not recognized. Try 'hello', 'how are you', or 'bye'.")

if __name__ == "__main__":
    start_chatbot()
