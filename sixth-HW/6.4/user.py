BOOK_CAPACITY = 10007

def hash_function(author, title):
    return (hash(author) + hash(title)) % BOOK_CAPACITY

class HashTable:
    def __init__(self):
        self.table = [[] for _ in range(BOOK_CAPACITY)]

    def insert(self, author, title):
        index = hash_function(author, title)
        if (author, title) not in self.table[index]:
            self.table[index].append((author, title))

    def search(self, author, title):
        index = hash_function(author, title)
        return (author, title) in self.table[index]

    def remove(self, author, title):
        index = hash_function(author, title)
        if (author, title) in self.table[index]:
            self.table[index].remove((author, title))

hash_table = HashTable()
author_books = {}

def init():
    global hash_table, author_books
    hash_table = HashTable()
    author_books = {}

def addBook(author, title):
    hash_table.insert(author, title)
    if author not in author_books:
        author_books[author] = []
    author_books[author].append(title)
    author_books[author].sort()

def find(author, title):
    return hash_table.search(author, title)

def delete(author, title):
    hash_table.remove(author, title)
    if author in author_books and title in author_books[author]:
        author_books[author].remove(title)

def findByAuthor(author):
    return author_books.get(author, [])
