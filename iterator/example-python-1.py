
class Book:
    def __init__(self, name: str):
        self.name = name

    def get_name(self):
        return self.name


class BookShelf:
    """
    ConcreteAggregate
    """
    def __init__(self, max_size: int):
        self.__books = [None for _ in range(max_size)]
        self.__last = 0
        self.__index = 0

    def __iter__(self):
        """
        Iteratorを返す
        インターフェースが定義されているため、Aggregateインターフェースが必要なくなる
        """
        self.__index = 0
        return self

    def __next__(self) -> Book:
        """
        Iteratorの役割を果たすため、Iterator / ConcreteIteratorが必要なくなる
        """
        # has_next
        if self.__index == self.__last:
            raise StopIteration()
        # next
        book = self.__books[self.__index]
        self.__index += 1
        return book

    def add(self, book: Book):
        self.__books[self.__last] = book
        self.__last += 1


def main():
    book_shelf = BookShelf(max_size=3)

    book_shelf.add(Book("book a"))
    book_shelf.add(Book("book b"))
    book_shelf.add(Book("book c"))

    for book in book_shelf:
        print(book.get_name())


if __name__ == '__main__':
    main()