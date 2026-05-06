import requests

url = "https://typicode.com"

reponse = requests.get(url)

if reponse.status_code == 200:
    donnees = reponse.json()
    print(f"Title: {donnees['title']}")
else:
    print(f"Error : {reponse.status_code}")
