import abc
from typing import List
from dataclasses import dataclass


class Product(abc.ABC):
    """
    Product
    """
    @abc.abstractmethod
    def use(self):
        pass


class Factory(abc.ABC):
    """
    Creator
    """
    def create(self, owner: str) -> Product:
        p = self.create_product(owner)
        self.register_product(p)

        return p

    @abc.abstractmethod
    def create_product(self, owner: str) -> Product:
        pass

    def register_product(self, product: Product):
        pass


@dataclass
class IDCard(Product):
    """
    ConcreteProduct
    """
    owner: str

    def use(self):
        print(f"{self.owner}のカードを使います")

    def get_owner(self):
        return self.owner


class IDCardFactory(Factory):
    """
    ConcreteCreator
    """
    def __init__(self):
        self.owners = []

    def create_product(self, owner: str) -> Product:
        return IDCard(owner)

    def register_product(self, product: Product):
        self.owners.add(product.get_owner())

    def get_owners(self) -> List[str]:
        return self.owners


def main():
    factory = IDCardFactory()
    card1 = factory.create("owner1")
    card2 = factory.create("owner2")
    card3 = factory.create("owner3")
    card1.use()
    card2.use()
    card3.use()



