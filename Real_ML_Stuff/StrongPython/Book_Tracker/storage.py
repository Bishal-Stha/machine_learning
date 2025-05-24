# storage.py
import json
import os

FILENAME = "favorites.json"

def load_favorites():
    if not os.path.exists(FILENAME):
        return []
    with open(FILENAME, "r") as file:
        return json.load(file)

def save_favorites(favorites):
    with open(FILENAME, "w") as file:
        json.dump(favorites, file, indent=4)

def add_to_favorites(book):
    favorites = load_favorites()
    # Avoid duplicates by book id
    if any(fav["id"] == book["id"] for fav in favorites):
        print("✅ Book already in favorites.")
        return
    favorites.append(book)
    save_favorites(favorites)
    print("✅ Book saved to favorites.")
