import abc
from typing import Tuple

class AbstractDisplay(abc.ABC):
    """
    AbstractClass
    """
    @abc.abstractmethod
    def open(self):
        """
        抽象メソッド
        """
        pass

    @abc.abstractmethod
    def print_l(self):
        """
        抽象メソッド
        """
        pass

    @abc.abstractmethod
    def close(self):
        """
        抽象メソッド
        """
        pass

    def display(self):
        """
        テンプレートメソッド
        """
        self.open()
        for i in range(5):
            self.print_l()
        self.close()


class CharDisplay(AbstractDisplay):
    """
    ConcreteClass
    """
    def __init__(self, char):
        self.char = char

    # 抽象メソッドを実装する
    def open(self):
        print("<<", end='')

    def close(self):
        print(">>")

    def print_l(self):
        print(self.char, end='')


class StringDisplay(AbstractDisplay):
    """
    ConcreteClass
    """

    def __init__(self, string):
        self.string = string

    # 抽象メソッドを実装する
    def open(self):
        print("-------start------")

    def close(self):
        print("-------end------")

    def print_l(self):
        print(self.string)

def exec_display(displays = Tuple[AbstractDisplay]):
    # AbstractClassとして指定可能、ロジックが共通化しているため、呼び出し元がConcreteClassについて知る必要がない
    for display in displays:
        display.display()


def main():
    string_display = StringDisplay('aaaaaaaaa')
    char_display = CharDisplay('b')
    exec_display((string_display, char_display))


if __name__ == '__main__':
    main()

"""
実行結果

```
-------start------
aaaaaaaaa
aaaaaaaaa
aaaaaaaaa
aaaaaaaaa
aaaaaaaaa
-------end------
<<bbbbb>>
```
"""
