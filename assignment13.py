import requests
req=requests.get("https://api.forismatic.com/api/1.0/?method=getQuote&format=json&lang=en")
print(req.status_code)
import json
data=req.json()
print(type(data))
print(data["quoteText"])
