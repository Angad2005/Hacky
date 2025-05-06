from flask import Flask, request, jsonify
from flask_cors import CORS
import google.generativeai as genai

app = Flask(__name__)
CORS(app)

# Load Gemini API key
GEMINI_API_KEY = "Enter your Gemini Key"
genai.configure(api_key=GEMINI_API_KEY)

# Load your custom dataset/instructions
with open("dataset.txt", "r") as f:
    custom_context = f.read()

# Create the model with context
model = genai.GenerativeModel(
    model_name="gemini-2.0-flash",
    system_instruction=custom_context
)

@app.route('/chat', methods=['POST'])
def chat():
    try:
        user_input = request.json.get("message", "")
        if not user_input:
            return jsonify({"error": "No message provided"}), 400

        response = model.generate_content(user_input)
        return jsonify({"response": response.text})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
