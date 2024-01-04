import requests
import pyttsx3

# Fetch current Bitcoin price from Coindesk API
response = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
data = response.json()
price = data['bpi']['USD']['rate']
print(f'Bitcoin Price is: {price}')

# Convert the price to an integer value
price = int(float(price.replace(',', '')))

# Initialize pyttsx3 engine
engine = pyttsx3.init()

# Configure the voice properties for Windows
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)  # Select the first voice

# Speak the price
engine.say(f"The current Bitcoin price is {price} USD.")
engine.runAndWait()