import requests

# Define the API endpoint
url = "https://jsonplaceholder.typicode.com/posts"

# Sample data to send in the POST request
data = {
    "title": "Build and Test POST Request",
    "body": "This is a sample body content.",
    "userId": 1
}

# Make the POST request
response = requests.post(url, json=data)

# Print response status and data
print("Status Code:", response.status_code)
print("Response JSON:", response.json())

"""
POST REQUEST WITH EXCEPTION HANDLING:
"""

url = "https://jsonplaceholder.typicode.com/posts"
data = {
    "title": "Error-handled POST",
    "body": "Adding error handling example",
    "userId": 1
}

try:
    response = requests.post(url, json=data)
    response.raise_for_status()  # Raises HTTPError for bad status codes (4xx/5xx)
    print("✅ POST Success:", response.status_code)
    print("Response:", response.json())
except requests.exceptions.HTTPError as errh:
    print("❌ HTTP Error:", errh)
except requests.exceptions.ConnectionError as errc:
    print("❌ Connection Error:", errc)
except requests.exceptions.Timeout as errt:
    print("❌ Timeout Error:", errt)
except requests.exceptions.RequestException as err:
    print("❌ Unknown Error:", err)

