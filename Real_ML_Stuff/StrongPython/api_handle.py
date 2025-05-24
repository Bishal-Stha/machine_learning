import requests

max_results = 5
query = str(input("Enter the name of book: "))
url = f"https://www.googleapis.com/books/v1/volumes?q={query}&maxResults={max_results}"


response = requests.get(url)

if(response.status_code ==200):
    data = response.json()
    for value in data:
        print(f"{value}: {data[value]}")
else: print(f"Error Fetching Book: {response.status_code}")