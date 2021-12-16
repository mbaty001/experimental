class Book():

    ebook = 'ebook'
    hardcover = 'hardcover'

    def __init__(self, name, type, pages):
        self.name = name
        self.type = type
        self.pages = pages

    def __str__(self):
        return f"Book: {self.name}, {self.type}, {self.pages}"

    @classmethod
    def hardcover(cls, name, pages):
        return Book(name, Book.hardcover, pages)
