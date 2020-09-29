# Iterator

## 概要

何らかの集合体に対して、要素を一つずつ順番に指し示し、最終的に全体をスキャンする処理を行うもの

## クラス図

![Wikipediaより](https://upload.wikimedia.org/wikipedia/commons/c/c5/W3sDesign_Iterator_Design_Pattern_UML.jpg)


## 登場人物

### Iterator

要素を順番にスキャンしていくインターフェース（API）を定める役

基本的なインターフェースは以下
- 次の要素があるか確認し（has_next）
- 次の要素を得る（next）

### ConcreteIterator

Iteratorが定めたインターフェースを実際に実装する

集合体のスキャンのために必要な情報を持つ

### Aggregate

集合体のインターフェース

Iteratorを作り出すインターフェースを持つ

### ConcreteAggregate

Aggregateの定めたインターフェースを実際に実装する

ConcreteIteratorを作り出す

## メリット

Iteratorが数え上げのインターフェースを持つため、ConcreteAggregate（集合体）の実装に依存せず、数え上げを行うことができる。

例えば、以下のような実装はConcreteAggregateの実装に依存せず実行可能

```Python
it = SomeConcreteAggregare.iterator()
while it.has_next():
    object_of_concrete_aggregate = it.next()
```

数え上げのインターフェースをIteratorとして定め、実装の依存先として独立させることで、どの集合体に対しても同じインターフェースで数え上げを行うことができる