from openai import OpenAI

# api_key = ""
# api_base="https://api.aiproxy.io/v1"

api_key =""
api_base="https://api.deerapi.com/v1"


client = OpenAI(
    api_key=api_key,  # This is the default and can be omitted
    base_url=api_base
)
completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "Hello!"}
  ]
)

print(completion.choices[0].message)