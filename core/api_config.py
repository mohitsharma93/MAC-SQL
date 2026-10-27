import os
# set your OPENAI_API_BASE, OPENAI_API_KEY here!
OPENAI_API_BASE = os.getenv("OPENAI_API_BASE", "your_own_api_base")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "your_own_api_key")

from functools import cache

from openai import AzureOpenAI
# set your own api_version
OPENAI_API_VERSION = "2023-07-01-preview"


@cache
def get_client() -> AzureOpenAI:
    return AzureOpenAI(api_key=OPENAI_API_KEY, api_version=OPENAI_API_VERSION, azure_endpoint=OPENAI_API_BASE)

MODEL_NAME = 'gpt-4-1106-preview' # 128k 版本
# MODEL_NAME = 'CodeLlama-7b-hf'
# MODEL_NAME = 'gpt-4-32k' # 0613版本
# MODEL_NAME = 'gpt-4' # 0613版本
# MODEL_NAME = 'gpt-35-turbo-16k' # 0613版本