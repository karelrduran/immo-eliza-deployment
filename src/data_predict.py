import requests


def predict(data: dict, property_type: str):
    if property_type == 'house':
        response = requests.post('https://property-price-predict-api.onrender.com/house/', json=data)
    else:
        response = requests.post('https://property-price-predict-api.onrender.com/apartment/', json=data)
    return response.json().get('predicted_price')
