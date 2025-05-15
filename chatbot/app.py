from flask import Flask, request, jsonify
from flask_cors import CORS
import google.generativeai as genai

app = Flask(__name__)
CORS(app)

# Load Gemini API key
GEMINI_API_KEY = "YourAPI"
genai.configure(api_key=GEMINI_API_KEY)

# Load your custom dataset/instructions
with open("dataset.txt", "r") as f:
    custom_context = f.read()

# Create the model with context
model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
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

@app.route('/buddy', methods=['POST'])
def buddy():
    data = request.get_json()
    user_message = data.get('message')
    custom_instructions = data.get('instructions', '')  # Optional instructions
    
    try:
        # Combine instructions + message if instructions exist
        if custom_instructions:
            full_prompt = f"{custom_instructions}\n\nUser: {user_message}\nAI:"
        else:
            full_prompt = user_message

        # Get response from Gemini
        response = model.generate_content(full_prompt)
        
        bot_reply = response.text if hasattr(response, 'text') else "Sorry, I couldn't understand that."
        return jsonify({"reply": bot_reply})
    except Exception as e:
        print("Error:", str(e))
        return jsonify({"reply": "An error occurred. Please try again."}), 500

# @app.route('/buddy', methods=['POST'])
# def chat():
#     user_message = request.json.get('message')
    
#     try:
#         # Get response from Gemini
#         response = model.generate_content(user_message)
#         bot_reply = response.text if hasattr(response, 'text') else "Sorry, I couldn't understand that."
#         return jsonify({"reply": bot_reply})
#     except Exception as e:
#         print("Error:", str(e))
#         return jsonify({"reply": "An error occurred. Please try again."}), 500

if __name__ == "__main__":
    app.run(debug=True)
