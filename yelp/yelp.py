import requests
import config

url = 'https://api.yelp.com/v3/businesses/search'

headers = {
    "Authorization": "Bearer " + config.API_KEY,
}
params = {
    "term": "Barber",
    "location": "USA"
}

response = requests.get(url, headers=headers, params=params)
businesses = response.json()["businesses"]

high_rated_names = [business["name"] for business in businesses if business["rating"] > 4.5]

print(high_rated_names, "\n")

for business in businesses:
    print(business["name"])
