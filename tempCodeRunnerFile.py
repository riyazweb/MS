from openai.api import OpenAI



client = OpenAI(
    # This is the default and can be omitted
    api_key="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",
)

chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": f"hello   ",
        }
    ],
    model="gpt-3.5-turbo",
)

OP = chat_completion.choices[0].message.content

OP = OP.replace('"', '')

print(OP)
