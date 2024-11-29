class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
    
    def displayDetails(self):
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"ISBN: {self.isbn}")
    
    def isSame(self, otherBook):
        if isinstance(otherBook, Book):
            return self.isbn == otherBook.isbn
        return False

if __name__ == "__main__":
    book1 = Book("To Kill a Mockingbird", "Harper Lee", "9780061120084")
    book2 = Book("1984", "George Orwell", "9780451524935")
    book3 = Book("To Kill a Mockingbird", "Harper Lee", "9780061120084")

    print("Book 1 details:")
    book1.displayDetails()
    print("\nBook 2 details:")
    book2.displayDetails()
    
    print("\nAre Book 1 and Book 2 the same? ", book1.isSame(book2))  
    print("Are Book 1 and Book 3 the same? ", book1.isSame(book3))