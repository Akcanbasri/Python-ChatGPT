import openai


openai.api_key = "your openai API key here"


def chat_with_gpt(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo", message=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content.strip()


if __name__ == "__main__":
    while True:
        user_input = input("You: ")
        if user_input.lower() == ["quit", "exit", "bye", "goodbye"]:
            break
        response = chat_with_gpt(user_input)
        print("GPT-3: " + response)

    