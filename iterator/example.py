"""
参考：https://qiita.com/ttsubo/items/97d7dd23e8f939c81d78
"""
import abc

class Iterator(abc.ABC):
    """
    Iteratorインターフェース
    """
    @abc.abstractmethod
    def has_next(self) -> bool:
        """
        次の要素が存在するかどうかを調べる
        :return: 次の要素が存在するか
        """
        pass

    @abc.abstractmethod
    def next(self) -> object:
        """
        集合体の要素を1個返し、次の要素へ進める
        :return: 集合体の要素
        """
        pass


class Aggregate:
    """
    Aggregateインターフェース
    """
    @abc.abstractmethod
    def iterator(self) -> Iterator:
        """
        集合体に対応するIteratorを1個生成する
        :return: 集合体に対応するIterator
        """
        pass


class Book:
    """
    本を表すクラス
    """
    def __init__(self, name: str):
        self.name = name

    def get_name(self):
        return self.name


class BookShelf(Aggregate):
    """
    ConcreteAggregate
    """
    def __init__(self, max_size: int):
        self.__books = [None for _ in range(max_size)]
        self.__last = 0

    def iterator(self) -> Iterator:
        return BookShelfIterator(self)

    def add(self, book: Book):
        self.__books[self.__last] = book
        self.__last += 1

    def get_length(self):
        return self.__last

    def get_book_at(self, index: int):
        return self.__books[index]


class BookShelfIterator(Iterator):
    """
    ConcreteIterator
    """
    def __init__(self, book_shelf: BookShelf):
        self.__book_shelf = book_shelf
        self.__index = 0

    def has_next(self):
        if self.__index < self.__book_shelf.get_length():
            return True
        else:
            return False

    def next(self) -> Book:
        book = self.__book_shelf.get_book_at(self.__index)
        self.__index += 1
        return book


def main():
    book_shelf = BookShelf(max_size = 3)

    book_shelf.add(Book("book a"))
    book_shelf.add(Book("book b"))
    book_shelf.add(Book("book c"))

    it = book_shelf.iterator()
    while it.has_next():
        book = it.next()
        print(book.get_name())


if __name__ == '__main__':
    main()
