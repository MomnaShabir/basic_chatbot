def chatbot():
    print("Chatbot: Hello! Welcome to my chatbot.")
    print("Chatbot: You can say hello, ask how I am, or type 'bye' to exit.")

    while True:
        user_input = input("You: ").strip().lower()

        if user_input == "hello" or user_input == "hi":
            print("Chatbot: Hi! How can I help you?")

        elif user_input == "how are you":
            print("Chatbot: I'm fine, thanks!")

        elif user_input == "bye":
            print("Chatbot: Goodbye! Have a nice day!")
            break

        else:
            print("Chatbot: Sorry, I don't understand that.")

if __name__ == "__main__":
    chatbot()
