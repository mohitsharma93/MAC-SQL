from functools import cache

from openai import OpenAI

@cache
def get_client() -> OpenAI:
    return OpenAI(api_key="EMPTY", base_url='http://0.0.0.0:8000/v1')


query = 'show me the quick sort in Python.'

completion = get_client().chat.completions.create(
  model="CodeLlama-7b-hf",
  messages=[
    {"role": "user", "content": query}
  ]
)
print(completion)

# print()
# print()
# print()

# print(openai.api_base)
# print(openai.api_key)
# print(openai.api_type)
# print(openai.api_version)
# completion = openai.Completion.create(
#   model="CodeLlama-7b-hf",
#   prompt=query,
#   max_tokens=300,
#   temperature=0
# )
# print(completion)
