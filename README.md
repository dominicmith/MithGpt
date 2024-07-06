# MithGpt

MithGpt is a chatbot application that provides text and voice responses to user queries. It uses Flask for the backend and Spacy for natural language processing. The chatbot can handle various intents such as greetings, farewells, jokes, weather, advice, motivation, and fun facts.

## Features

- Text and voice responses to user queries
- Natural language processing using Spacy
- Multiple intents supported:
  - Greetings
  - Farewells
  - Jokes
  - Weather
  - Advice
  - Motivation
  - Fun facts

## Requirements

- Python 3.6+
- Flask
- Spacy
- gtts (Google Text-to-Speech)

## Installation

1. Clone the repository:

    ```sh
    git clone https://github.com/yourusername/MithGpt.git
    cd MithGpt
    ```

2. Create and activate a virtual environment (optional but recommended):

    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. Install the required packages:

    ```sh
    pip install -r requirements.txt
    ```

4. Download the Spacy English model:

    ```sh
    python -m spacy download en_core_web_md
    ```

## Usage

1. Run the Flask application:

    ```sh
    python app.py
    ```

2. Open your web browser and go to:

    ```
    http://127.0.0.1:5000
    ```

3. Type a message in the input box and press Enter or click Send. The chatbot will respond with text and voice.

## Project Structure

```
MithGpt/
├── static/
│   ├── style.css       # CSS file for styling
│   └── app.js          # JavaScript file for handling user interactions
├── templates/
│   └── index.html      # HTML file for the chatbot interface
├── app.py              # Main Flask application
└── README.md           # Project README file
```

## Intents and Responses

Here are the supported intents and their corresponding responses:

- Greeting:
  - Examples: "hello", "hi", "hey", "good morning", "good afternoon", "hey MithGpt"
  - Response: "Hey there! MithGpt at your service. How can I assist you today?"

- Farewell:
  - Examples: "bye", "goodbye", "see you", "take care", "later MithGpt"
  - Response: "Catch you later! MithGpt signing off!"

- Joke:
  - Examples: "tell me a joke", "make me laugh", "joke", "humor me MithGpt"
  - Response: "Why did the scarecrow win an award? Because he was outstanding in his field!"

- Weather:
  - Examples: "what's the weather like", "weather", "how's the weather", "weather update MithGpt"
  - Response: "I can't check the weather for you, but I hope the sun is shining bright!"

- Advice:
  - Examples: "give me advice", "I need advice", "help me MithGpt"
  - Response: "Sometimes, the best advice is to trust yourself and keep pushing forward. You've got this!"

- Motivation:
  - Examples: "motivate me", "inspire me", "I need motivation", "give me a pep talk"
  - Response: "Believe in yourself and all that you are. Know that there is something inside you that is greater than any obstacle."

- Fun Fact:
  - Examples: "tell me a fun fact", "fun fact", "amaze me MithGpt"
  - Response: "Did you know? Honey never spoils. Archaeologists have found pots of honey in ancient Egyptian tombs that are over 3,000 years old and still perfectly edible!"

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

---
