import requests

url = "https://google-search72.p.rapidapi.com/search"

querystring = {"q":"word cup","lr":"en-US","num":"10"}

headers = {
	"x-rapidapi-key": "624eba1ea4msh4999a337320ec34p1ee061jsn74d6042dc343",
	"x-rapidapi-host": "google-search72.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

print(response.json())