from openai import OpenAI
from dotenv import load_dotenv
from typing import Iterable
from openai.types.chat import ChatCompletion, ChatCompletionMessageParam

import os

load_dotenv()

openai_client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)

def call_openai(messages: Iterable[ChatCompletionMessageParam]) -> ChatCompletion:
    return openai_client.chat.completions.create(
        model="gpt-4o",
        messages=messages,
        temperature=0
    )

def extract_data_from_images():
    print("implement me")

if __name__ == "__main__":
    extract_data_from_images()