import requests

url = "https://jsonplaceholder.typicode.com/posts/1"

# Data to update
updated_data = {
    "id": 1,
    "title": "Updated Title",
    "body": "Updated content",
    "userId": 1
}

# PUT request
response = requests.put(url, json=updated_data)

print("Status Code:", response.status_code)
print("Response JSON:", response.json())


#Delete request
response2 = requests.delete(url)

print("Status Code:", response2.status_code)
if response2.status_code ==200:
    print("Deleted Successfully")
