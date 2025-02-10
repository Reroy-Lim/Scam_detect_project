import nltk
import re
from nltk.tokenize import word_tokenize
nltk.download('punkt')

# Define common scam keywords and patterns
scam_keywords = [
    "urgent", "lottery", "free", "prize", "winner", "claim", 
    "bank account", "cash prize", "click here", "congratulations", 
    "exclusive offer", "offer expires soon", "credit card", "social security number", "fast approval"
]

# Regex patterns for detecting suspicious URLs and amounts
url_pattern = r"http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+"
money_pattern = r"\d+[Kk]x60"  # Detects patterns like 10Kx60 or 100Kx60

# Function to get emergency number based on country (case-insensitive)
def get_emergency_number(country):
    country = country.lower()  # Convert input to lowercase
    
    # Dictionary mapping both full country names and abbreviations to emergency numbers
    emergency_numbers = {
        'singapore': '999 (Police), 995 (Ambulance and Fire)',
        'sg': '999 (Police), 995 (Ambulance and Fire)',  # For abbreviation
        'uk': '999 or 112 (Police, Ambulance, Fire, and other emergencies)',
        'united kingdom': '999 or 112 (Police, Ambulance, Fire, and other emergencies)',
        'us': '911 (Police, Ambulance, Fire, and other emergencies)',
        'united states': '911 (Police, Ambulance, Fire, and other emergencies)',
        'australia': '000 (Police, Ambulance, Fire, and other emergencies)',
        'aus': '000 (Police, Ambulance, Fire, and other emergencies)',  # Abbreviation
        'canada': '911 (Police, Ambulance, Fire, and other emergencies)',
        'india': '112 (All Emergencies)',
        'germany': '112 (Fire and Medical Emergencies), 110 (Police)',
        'france': '112 (All Emergencies)',
        'japan': '110 (Police), 119 (Fire and Ambulance)',
        'brazil': '190 (Police), 192 (Ambulance), 193 (Fire)',
        'mexico': '911 (All Emergencies)',
        'south africa': '10111 (Police), 10177 (Ambulance and Fire)',
        'new zealand': '111 (All Emergencies)',
        'italy': '112 (All Emergencies)',
        'spain': '112 (All Emergencies)',
        'russia': '112 (All Emergencies)',
        'south korea': '112 (Police), 119 (Fire and Ambulance)',
        'saudi arabia': '999 (Police), 997 (Ambulance)',
        'argentina': '911 (All Emergencies)',
        'egypt': '122 (Police), 123 (Ambulance), 180 (Fire)',
        'belgium': '112 (All Emergencies)',
        'netherlands': '112 (All Emergencies)',
        'sweden': '112 (All Emergencies)',
        'denmark': '112 (All Emergencies)',
        'norway': '112 (All Emergencies)',
        'finland': '112 (All Emergencies)',
        'switzerland': '112 (All Emergencies)',
        'portugal': '112 (All Emergencies)',
        'poland': '112 (All Emergencies)',
        'greece': '112 (All Emergencies)',
        'turkey': '112 (All Emergencies)',
        'romania': '112 (All Emergencies)',
        'belize': '911 (All Emergencies)',
        'philippines': '911 (Police), 160 (Fire), 162 (Ambulance)'
    }
    
    return emergency_numbers.get(country, 'Unknown emergency number')

# Function to check if message contains a scam
def check_scam(text):
    tokens = word_tokenize(text.lower())  # Tokenize the text and convert to lowercase
    scam_detected = any(keyword in tokens for keyword in scam_keywords)
    
    # Check for suspicious URLs
    url_found = re.search(url_pattern, text)
    if url_found:
        print(f"Suspicious URL detected: {url_found.group()}")

    # Check for money patterns like "10Kx60"
    money_found = re.findall(money_pattern, text)
    if money_found:
        print(f"Suspicious money pattern detected: {', '.join(money_found)}")

    return scam_detected or bool(url_found) or bool(money_found)

# Chatbot logic
def chatbot():
    print("Hello! I'm your Scam Detector Bot. Type a message, and I'll check if it's a scam.")
    country = input("Please enter your country (e.g., Singapore, UK, US or other): ").strip()
    emergency_number = get_emergency_number(country)
    
    print(f"Bot: In case of a scam, please call the emergency number for {country}: {emergency_number}")
    
    while True:
        user_input = input("You: ")
        
        if user_input.lower() == "quit":
            print("Bot: Goodbye!")
            break
        
        # Check if the message is a scam
        scam_detected = check_scam(user_input)
        
        if scam_detected:
            print("Bot: This message looks like a scam. Please be cautious!")
            print(f"Bot: If you believe this is a scam, please call the police at {emergency_number}.")
        else:
            print("Bot: This seems safe, but always double-check before responding.")

# Run the chatbot
chatbot()
