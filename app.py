from gtts import gTTS
import os
import random
import spacy
from flask import Flask, request, jsonify, render_template, send_file

# Load spaCy's English model
nlp = spacy.load("en_core_web_md")

app = Flask(__name__)

# Define intents and responses
intents = {
    "greeting": ["hello", "hi", "hey", "good morning", "good afternoon", "hey MithGpt"],
    "farewell": ["bye", "goodbye", "see you", "take care", "later MithGpt"],
    "joke": ["tell me a joke", "make me laugh", "joke", "humor me MithGpt"],
    "weather": ["what's the weather like", "weather", "how's the weather", "weather update MithGpt"],
    "advice": ["give me advice", "I need advice", "help me MithGpt"],
    "motivation": ["motivate me", "inspire me", "I need motivation", "give me a pep talk"],
    "fun_fact": ["tell me a fun fact", "fun fact", "amaze me MithGpt"]
}

responses = {
    "greeting": "Hey there! MithGpt at your service. How can I assist you today?",
    "farewell": "Catch you later! MithGpt signing off!",
    "joke": "Why did the scarecrow win an award? Because he was outstanding in his field!",
    "weather": "I can't check the weather for you, but I hope the sun is shining bright!",
    "advice": "Sometimes, the best advice is to trust yourself and keep pushing forward. You've got this!",
    "motivation": "Believe in yourself and all that you are. Know that there is something inside you that is greater than any obstacle.",
    "fun_fact": "Did you know? Honey never spoils. Archaeologists have found pots of honey in ancient Egyptian tombs that are over 3,000 years old and still perfectly edible!",
    "default": "Hmm, I’m not sure how to respond to that. Can you try asking something else?"
}

# Function to match user input to an intent
def get_intent(user_input):
    doc = nlp(user_input.lower())
    for intent, examples in intents.items():
        for example in examples:
            example_doc = nlp(example.lower())
            if doc.similarity(example_doc) > 0.75:
                return intent
    return "default"

# Function to generate speech from text
def generate_speech(text):
    tts = gTTS(text=text, lang='en')
    filename = f"response_{random.randint(0, 100000)}.mp3"
    filepath = os.path.join('static', filename)
    tts.save(filepath)
    return filepath

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/get_response', methods=['POST'])
def get_response():
    user_input = request.json.get('message')
    intent = get_intent(user_input)
    response_text = responses.get(intent, responses["default"])
    audio_path = generate_speech(response_text)
    return jsonify({"response": response_text, "audio": audio_path})

@app.route('/play_audio/<filename>')
def play_audio(filename):
    return send_file(os.path.join('static', filename))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
