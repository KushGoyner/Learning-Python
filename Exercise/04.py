# Library Management Software

class Library:
    def __init__(self):
        self.noBooks = 0
        self.books = []

    def adddBook(self,book):
        self.books.append(book)
        self.noBooks = len(self.books)

    def showInfo(self):
        print(f"The library has {self.noBooks} books")
        for book in self.books:
            print(book)


l1 = Library()

l1.adddBook("harry potter")
l1.adddBook("Gulivers Travels")
l1.adddBook("Maze runner")
l1.showInfo()

