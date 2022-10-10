import requests

parameters = {
        "product_type": 'blush'
    }
response = requests.get("http://makeup-api.herokuapp.com/api/v1/products.json", json=parameters)
# print(response.status_code)
# response.raise_for_status()
print(response.status_code)
data = response.json()
