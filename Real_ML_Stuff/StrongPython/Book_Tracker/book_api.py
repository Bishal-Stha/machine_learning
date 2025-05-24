# book_api.py
import requests

def search_books(query, max_results=5):
    url = f"https://www.googleapis.com/books/v1/volumes?q={query}&maxResults={max_results}"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        books = []
        for item in data.get("items", []):
            volume_info = item.get("volumeInfo", {})
            book = {
                "title": volume_info.get("title"),
                "authors": volume_info.get("authors", ["Unknown"]),
                "description": volume_info.get("description", "No description available."),
                "id": item.get("id")
            }
            books.append(book)
        return books
    else:
        print("Error fetching books:", response.status_code)
        return []
