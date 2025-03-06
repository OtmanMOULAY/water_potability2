import json 
import requests

url  = "https://water-potability-c0cb.onrender.com/predict"

x_news = dict (

    ph = 7,
    Hardness= 131,
    Solids= 12,
    Chloramines= 43,
    Sulfate= 123,
    Conductivity= 11,
    Organic_carbon= 44,
    Trihalomethanes=313,
    Turbidity= 12
    )

x_news_json = json.dumps(x_news)

response = requests.post(url, data=x_news_json)

print("the predction is that : ",response.text)
print("status: ",response.status_code)