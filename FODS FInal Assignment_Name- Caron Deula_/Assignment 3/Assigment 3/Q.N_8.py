import json

class Book:
    def __init__(self, title, author, issued=False):
        self.title = title
        self.author = author
        self.issued = issued

    def to_dict(self):
        return {'title': self.title, 'author': self.author, 'issued': self.issued}

class Library:
    def __init__(self, filename="books.json"):
        self.filename = filename
        self.books = self.load_books()

    def load_books(self):
        try:
            with open(self.filename, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            return []

    def save_books(self):
        with open(self.filename, 'w') as file:
            json.dump(self.books, file, indent=4)

    def add_book(self, title, author):
        self.books.append(Book(title, author).to_dict())
        self.save_books()
        print(f"Book '{title}' added.")

    def issue_book(self, title):
        for book in self.books:
            if book['title'].lower() == title.lower() and not book['issued']:
                book['issued'] = True
                self.save_books()
                print(f"Book '{title}' issued.")
                return
        print("Book not available.")

    def return_book(self, title):
        for book in self.books:
            if book['title'].lower() == title.lower() and book['issued']:
                book['issued'] = False
                self.save_books()
                print(f"Book '{title}' returned.")
                return
        print("Book not found or wasn't issued.")

    def search_book(self, title):
        found = False
        for book in self.books:
            if title.lower() in book['title'].lower():
                status = "Issued" if book['issued'] else "Available"
                print(f"{book['title']} by {book['author']} - {status}")
                found = True
        if not found:
            print("No matching book found.")

# Example menu-based usage
lib = Library()

while True:
    print("\n1. Add Book\n2. Issue Book\n3. Return Book\n4. Search Book\n5. Exit")
    choice = input("Choose an option: ")

    if choice == '1':
        title = input("Book Title: ")
        author = input("Author: ")
        lib.add_book(title, author)
    elif choice == '2':
        title = input("Enter book title to issue: ")
        lib.issue_book(title)
    elif choice == '3':
        title = input("Enter book title to return: ")
        lib.return_book(title)
    elif choice == '4':
        title = input("Enter book title to search: ")
        lib.search_book(title)
    elif choice == '5':
        break
    else:
        print("Invalid option.")
