class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

book1 = Book("The Great Gatsby", "F. Scott Fitzgerald")
print(f"Book 1 Title: {book1.title}, Author: {book1.author}")

del book1.author

try:
    print(f"Book 1 Author: {book1.author}")
except AttributeError:
    print("The author attribute has been deleted.")

book2 = Book("1984", "George Orwell")
print(f"Book 2 Title: {book2.title}, Author: {book2.author}")

print(f"Book 1 Title: {book1.title}")