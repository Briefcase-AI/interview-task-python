from openai import OpenAI
from dotenv import load_dotenv
from typing import List, Dict
from openai.types.chat import ChatCompletion

import os

load_dotenv()

openai_client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)

def call_openai(messages: List[Dict[str, str]]) -> ChatCompletion:
    return openai_client.chat.completions.create(
        model="gpt-4o",
        messages=messages,
        temperature=0
    )

def extract_data_from_images():
    print("implement me")

if __name__ == "__main__":
    extract_data_from_images()