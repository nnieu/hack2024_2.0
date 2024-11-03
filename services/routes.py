from flask import Flask, request, jsonify, session
import asyncio
# from . import get_response_from_gf

app = Flask(__name__)

@app.route('/api/chat', methods=['POST'])
async def chat():
    print("Chat route is hit")  # Debugging line
    data = request.get_json()
    user_input = data.get('user_input')
    character = data.get('character')
    print(user_input)
    print(character)
    bot_response = f"You said: {user_input}. (Character: {character})"
    print(bot_response)  # Check response in console
    return jsonify({'response': bot_response})

    # return jsonify(response)

