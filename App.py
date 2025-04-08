from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS  # Enable CORS
import google.generativeai as genai

app = Flask(__name__)
CORS(app)  # Allow all origins

# Configure Gemini API
genai.configure(api_key="AIzaSyACs27id08grEM8zZ3V44vNfIprnoh9nHs")  # Replace with your API key

# Route for the chatbot
@app.route('/chat', methods=['POST'])
def chat():
    try:
        user_input = request.json.get('message')
        if not user_input:
            return jsonify({"error": "No message provided"}), 400

        model = genai.GenerativeModel("gemini-1.5-flash")
        response = model.generate_content(user_input)
        return jsonify({"response": response.text})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)