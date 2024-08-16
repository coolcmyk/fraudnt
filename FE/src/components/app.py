from flask import Flask, request, jsonify
from flask_cors import CORS
from aiko import LLM

app = Flask(__name__)
CORS(app)

llm = LLM()

@app.route('/chat', methods=['POST'])
def chat_function():
    if request.method != 'POST':
        return 'Send a POST request'
    
    request_json = request.get_json(silent=True)
    user_input = request_json['message']
    
    # This is where the LLM generates a response
    response = llm.chat_single_turn(user_input)
    
    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(debug=True)