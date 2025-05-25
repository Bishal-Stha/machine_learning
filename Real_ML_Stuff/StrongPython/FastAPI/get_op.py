import requests

# GET REQUEST WITHOUT EXCEPTION HANDLING

url = "https://jsonplaceholder.typicode.com/posts/1"

# response = requests.get(url)
# print(response.json())
# print(type(response))

response = requests.get(url)
data = response.json()
try:
    print("✅ GET Success:", response.status_code)
    print("Title:", data["title"])
    
except requests.exceptions.HTTPError as errh:
    print("❌ HTTP Error:", errh)
except requests.exceptions.ConnectionError as errc:
    print("❌ Connection Error:", errc)
except requests.exceptions.Timeout as errt:
    print("❌ Timeout Error:", errt)
except requests.exceptions.RequestException as err:
    print("❌ Unknown Error:", err)