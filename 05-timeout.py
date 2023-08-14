import requests

def test_api_response():
    # Set a very small timeout to provoke the Timeout exception
    response = requests.get('https://reqres.in/api/users', timeout=0.0001)

# Call the function to execute it and provoke the exception
test_api_response()
