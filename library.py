# ...existing code...
def main_run():
    class Library:
        def __init__(self):
            self.catalog = []
        def add_book(self, book):
            self.catalog.append(book)
            print("successfully added", book.title)
            print()
        def list_books(self):
            print("--BOOK LIST---------------------------¬")
            for book in self.catalog:
                print(book.title)
            print("---------------------------------------")
            print()
        def display_catalog(self):
            print()
            print("------------------------CATALOG------------------------")
            print()
            for book in self.catalog:
                book.display_info()
            print("--------------------------------------------------------")
    
    class Book:
        def __init__(self, title, author, isbn):
            self.title = title
            self.author = author
            self.isbn = isbn
        def display_info(self):
            print("**"+ self.title+ "**", "\nauthor:", self.author, "\nisbn:", self.isbn)
            print("\n")


    my_library = Library()

    book1 = Book("¦The Hitchhiker's Guide to the Galaxy ¦", "Douglas Adams", "978-0345391803")
    book2 = Book("¦Pride and Prejudice                  ¦", "Jane Austen", "978-0141439518")
    book3 = Book("¦Sapiens: A Brief History of Humankind¦", "Yuval Noah Harari", "978-0062316097")

    my_library.add_book(book1)
    my_library.add_book(book2)
    my_library.add_book(book3)

    my_library.list_books()
    my_library.display_catalog()

main_run()