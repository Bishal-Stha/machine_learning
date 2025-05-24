# main.py
from book_api import search_books
from storage import add_to_favorites, load_favorites

def display_books(books):
    print("\nTop Results:")
    for i, book in enumerate(books):
        print(f"{i + 1}. {book['title']} by {', '.join(book['authors'])}")

def main():
    while True:
        print("\n--- Personal Book Tracker ---")
        print("1. Search for a book")
        print("2. View saved books")
        print("3. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            query = input("Enter book title or keyword: ")
            results = search_books(query)
            if results:
                display_books(results)
                try:
                    index = int(input("\nEnter number to save to favorites (0 to skip): "))
                    if 1 <= index <= len(results):
                        add_to_favorites(results[index - 1])
                    else:
                        print("Skipped saving.")
                except ValueError:
                    print("Invalid input.")
            else:
                print("No books found.")

        elif choice == "2":
            favorites = load_favorites()
            if favorites:
                print("\n--- Saved Books ---")
                display_books(favorites)
            else:
                print("No favorites yet.")
        
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
