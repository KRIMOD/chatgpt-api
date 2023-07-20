import openai

# Replace 'YOUR_API_KEY' with your actual API key
openai.api_key = 'YOUR_API_KEY'


def chat_with_gpt(prompt, context):
    try:
        # Send the prompt and context to ChatGPT
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # You can change the model if needed
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt},
                {"role": "assistant", "content": context}
            ]
        )

        # Extract the assistant's reply from the response
        reply = response['choices'][0]['message']['content']

        return reply
    except Exception as e:
        return str(e)


def main():
    print("Welcome to ChatGPT!")
    context = ""  # Initialize the context as an empty string

    while True:
        user_input = input("You: ")

        if user_input.lower() in ('exit', 'quit'):
            print("Goodbye!")
            break

        # Call the chat_with_gpt function to get the assistant's reply
        assistant_reply = chat_with_gpt(user_input, context)

        print("ChatGPT:", assistant_reply)
        context = assistant_reply  # Update the context with the assistant's reply


if __name__ == "__main__":
    main()
