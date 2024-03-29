import requests


def predict(data: dict, property_type: str):
    """
    Predicts the price of a property based on the provided data using an API.

    Args:
    data (dict): A dictionary containing the data related to the property.
    property_type (str): The type of property ('house' or 'apartment').

    Returns:
    float: The predicted price of the property.

    Raises:
    ValueError: If property_type is not 'house' or 'apartment'.
    """
    if property_type == 'house':
        response = requests.post('https://property-price-predict-api.onrender.com/house/', json=data)
    else:
        response = requests.post('https://property-price-predict-api.onrender.com/apartment/', json=data)
    return response.json().get('predicted_price')
