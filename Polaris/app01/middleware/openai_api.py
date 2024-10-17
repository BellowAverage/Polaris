import os
from openai import OpenAI

prompt = "the capital of the u.s is "

client = OpenAI(

    api_key="",
)

chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "system",
            "content": "You are an AI text completion assistant. You are called through api, to help with users' text completion. When the user is writting something, you will predict what he or she is goint to write next. You will respond with the suggestion and the suggestion only to the user's text, excluding what the user has written previously.",
        },
        {"role": "user","content": prompt},
        # previous context
        # {"role": "assistant", "content": "The Los Angeles Dodgers won the World Series in 2020."},
    ],
    model="gpt-3.5-turbo",
)