import os
import openai
openai.api_key = "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"
response = openai.Completion.create(
    engine="ada",
    prompt="Write chess logic on Python",
    temperature=0.3,
    max_tokens=64,
    top_p=1,
    frequency_penalty=0.5,
    presence_penalty=0)
print(response)
