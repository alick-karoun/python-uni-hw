class Book:
    def __init__(self, title, author, page_num):
        self.title=title
        self.author=author
        self.page_num=page_num

    def describe(self):
        return f"{self.title} by {self.author} ({self.page_num} pages)"
        
def main():
    book = Book("Atomic Habits", "James Clear", 320)
    print(book.describe())
main()