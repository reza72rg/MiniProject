import requests
import json
r = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')

# request part and response as r
data = json.loads(r.text)
price = data['bpi']['USD']['rate']
print(f'Bitcoin Price is : {price}')
