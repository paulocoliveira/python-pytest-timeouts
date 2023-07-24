import requests

def test_api_response():
    # Set a timeout of 5 seconds for the API request
    response = requests.get('https://reqres.in/api/users', timeout=5)
    # Perform assertions on the response
    # ...