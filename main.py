class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
    def get_info(self):
        print(f'title: {self.title}, author: {self.author}')
Student = Book(title="blablabla", author="bububu")
Student.get_info()