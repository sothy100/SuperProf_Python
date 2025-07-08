import requests

<<<<<<< HEAD
# URL à recupérer (sothy)
=======
# URL à recupérer
>>>>>>> 73c92ae0c8ca99deee33fc0dd73b3b5b076a58e5
chemin = "httpbin.org/get" 
url = f"https://{chemin}"

response = requests.get(url)
print(response.status_code)
print(response.json())
