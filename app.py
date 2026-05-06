import os
import google.generativeai as genai
from flask import Flask, request, jsonify

# הגדרת המודל - הקוד ימשוך את המפתח מהגדרות השרת שנבצע בהמשך
genai.configure(api_key=os.environ.get("GOOGLE_API_KEY"))
model = genai.GenerativeModel('gemini-1.5-flash')

app = Flask(__name__)

@app.route('/')
def home():
    return "האפליקציה שלי באוויר!"

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get('message')
    response = model.generate_content(user_input)
    return jsonify({"response": response.text})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
