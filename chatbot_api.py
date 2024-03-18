# Placeholder file - the call to AI model will be made here

from openai import OpenAI
import config

def query(user_message):
    try:
        # Load your API key from config.py file
        client = OpenAI(api_key=config.OPENAI_KEY)

        completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": "Your job is to provide feedback, improvements and help with students who are learning to code."
            },
            {
                "role": "user",
                "content": user_message
            }
        ]
        )

        # Extracting the analysis or suggestion provided by the model
        suggestion = completion.choices[0].message.content if completion.choices else "No suggestion could be generated."
    except:
        suggestion = "AI request was unable to complete, this is a placeholder response"

    return {'response': suggestion}