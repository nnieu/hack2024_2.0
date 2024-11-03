from openai import OpenAI
import os 
import json
from dotenv import load_dotenv
import asyncio
# services/open_services.py
from scenarios import get_scenario, get_random_date_idea
from flask import Flask, jsonify, session



def get_api_key():

    load_dotenv()
    api_key = os.getenv('openapi_key')
    return api_key

client = OpenAI(
    api_key = get_api_key()
)

async def get_response_from_gf(user_input=None, character="pretty girl", mode="easy", conversation=[]):
    # scenario_type = "easy"
    scenario = get_scenario(mode) 
    date = get_random_date_idea()
    

    if not conversation:  # This checks if the conversation list is empty
        prompt = ( f"Imagine you are in {scenario}. You are {character}. Start a conversation with the user in a friendly and curious manner."
                    f"{'Start a conversation' if user_input is None else 'Respond to the user'}"
                f"For context you are on this date: {date}"
                )

            
        messages = [{"role": "system", "content": prompt}]

    else:
        messages = conversation


    if user_input:
        messages.append({"role": "user", "content": user_input})

    chat_completion = client.chat.completions.create(
        messages=messages,
        model="gpt-3.5-turbo"
    )

    chatbox_response = chat_completion.choices[0].message.content 

    conversation.append({"role": "assistant", "content": chatbox_response})

    # return jsonify({"response": chatbox_response})
    return {"response": chatbox_response}

# print(openai.api_key)


# Test the function
# import asyncio


test_input = "What do you like to do on weekends?"

# Run the async function
response = asyncio.run(get_response_from_gf(test_input))
print("Response from the girlfriend bot:", response)
