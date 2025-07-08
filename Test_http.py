import requests

# URL à recupérer

chemin = "httpbin.org/get" 
url = f"https://{chemin}"

response = requests.get(url)
print(response.status_code)
print(response.json())
