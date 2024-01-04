import requests
import json
import pyttsx3
r = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')

# request part and response as r
data = json.loads(r.text)
price = data['bpi']['USD']['rate']
print(f'Bitcoin Price is : {price}')
price= int(float(price.replace(',','')))
engine = pyttsx3.init()
engine.say("Bitcoin price now is {}".format(price))
engine.runAndWait()
