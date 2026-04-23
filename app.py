import os
from openai import OpenAI
from retriever import build_store_from_file, retrieve
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

store = build_store_from_file("sample.txt")

messages = [
    {"role": "system", "content": "You are a helpful AI assistant. Use provided context to answer."}
]

while True:
    user_input = input("You: ")

    if user_input.lower() == "exit":
        break

    context = retrieve(user_input, store)

    prompt = f"""
    Context:
    {context}

    Question:
    {user_input}
    """

    messages.append({"role": "user", "content": prompt})

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=messages
    )

    reply = response.choices[0].message.content
    print("Bot:", reply)

    messages.append({"role": "assistant", "content": reply})