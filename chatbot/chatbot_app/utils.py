import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import random

# Initialize NLTK's stopwords and WordNet lemmatizer
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')

stop_words = set(stopwords.words('english'))
lemmatizer = WordNetLemmatizer()

# Define some sample responses
responses = {
    "greeting": ["I am AI bot."],
    "farewell": ["Goodbye!", "See you later!", "Have a great day!"],   
    "fever": ["Chills or shivering", "cough"],
    "cancer": ["Difficulty swallowing", "Changes in the appearance of the breast."],
    "name":["my name is AI bot","my friends call me AI bot"],
    "dengue":["vomiting,muscle and join pain",],

    "default": ["That's interesting.", "Tell me more.", "I'm not sure I understand."],
   
}

# Define a function to preprocess user input
def preprocess_input(input_text):
    words = word_tokenize(input_text)
    words = [w for w in words if w not in stop_words]
    words = [lemmatizer.lemmatize(w) for w in words]
    return words

# Define a function to generate a response
def generate_response(input_text):
    input_words = preprocess_input(input_text)
    
    if any(word in input_words for word in ["hi", "hello", "hey"]):
        return random.choice(responses["greeting"])
    elif any(word in input_words for word in ["bye", "goodbye"]):
        return random.choice(responses["farewell"])
    elif any(word in input_words for word in ["name","you"]):
        return random.choice(responses["name"])
    elif any(word in input_words for word in ["fever","flu"]):
        return random.choice(responses["fever"])
    elif any(word in input_words for word in ["cancer"]):
        return random.choice(responses["cancer"])
    elif any(word in input_words for word in ["dengue"]):
        return random.choice(responses["cancer"])
    
    else:
        return random.choice(responses["default"])

# Main loop to interact with the chatbot
# user_input = input("You: ")
# response = generate_response(user_input)
# print("Bot:", response)

