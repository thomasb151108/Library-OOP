def main_run():
    class Library:
        def __init__(self):
            self.catalog = []
        def add_item(self, item):
            self.catalog.append(item)
            print("successfully added", item.title)
            print()
        def list_items(self):
            print("--ITEM LIST---------------------------¬")
            for item in self.catalog:
                print(item.title)
            print("---------------------------------------")
            print()
        def display_catalog(self):
            print()
            print("------------------------CATALOG------------------------")
            print()
            for item in self.catalog:
                item.display_info()
            print("--------------------------------------------------------")

    class Item:
        def __init__(self, title, type):
            self.title = title
            self.type = type

    class Book(Item):
        def __init__(self, title, author, isbn, type):
            super().__init__(title, type)
            self.author = author
            self.isbn = isbn
        def display_info(self):
            print("**"+ self.title+ "**", "\nauthor:", self.author, "\nisbn:", self.isbn, "\ntype:", self.type)
            print("\n")
    
    class DVD(Item):
        def __init__(self, title, director, runtime, type):
            super().__init__(title, type)
            self.director = director
            self.runtime = runtime
            self.type = "DVD"
        def display_info(self):
            print("**"+ self.title+ "**", "\ndirector:", self.director, "\nruntime:", self.runtime, "\ntype:", self.type)
            print("\n")

    class Game(Item):
        def __init__(self, title, developer, type):
            super().__init__(title, type)
            self.developer = developer
            self.type = "game"
        def display_info(self):
            print("**"+ self.title+ "**", "\ndeveloper:", self.developer, "\ntype:", self.type)
            print("\n")

    my_library = Library()

    book1 = Book("¦The Hitchhiker's Guide to the Galaxy ¦", "Douglas Adams", "978-0345391803", "book")
    book2 = Book("¦Pride and Prejudice                  ¦", "Jane Austen", "978-0141439518", "book")
    book3 = Book("¦Sapiens: A Brief History of Humankind¦", "Yuval Noah Harari", "978-0062316097", "book")
    dvd1 = DVD(  "¦Thundercats collection               ¦", "Katsuhito Akiyama and Jules Bass", "47 hours and 39 minutes", "DVD")
    game1 = Game("¦Zelda                                ¦", "Nintendo", "game")

    my_library.add_item(book1)
    my_library.add_item(book2)
    my_library.add_item(book3)
    my_library.add_item(dvd1)
    my_library.add_item(game1)

    my_library.list_items()
    my_library.display_catalog()

main_run()