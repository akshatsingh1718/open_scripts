import os
from openai import OpenAI
from langchain_openai import ChatOpenAI
from langchain_openai import OpenAI


def langchain_response(message: str):
    llm = OpenAI()
    llm = ChatOpenAI(model="gpt-4o")

    return llm.invoke(message)


def openai_response(message: str):
    client = OpenAI(
        # This is the default and can be omitted
        api_key=os.environ.get("OPENAI_API_KEY"),
    )
    completion = client.chat.completions.create(
        model="gpt-4o", messages=[{"role": "user", "content": message}]
    )

    return completion
