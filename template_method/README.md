# Template Method

## 概要

クラスのテンプレ（雛形）をまず定義し、クラスごとに異なる処理をサブクラスで実装することで、処理とインターフェースの共通化を行う

## クラス図

![Wikipediaより](https://upload.wikimedia.org/wikipedia/commons/2/2a/W3sDesign_Template_Method_Design_Pattern_UML.jpg)

## 登場人物

### AbstractClass

- テンプレートメソッド（クラス共通で行われる処理）を実装
- 抽象メソッド（クラスごとに内容は異なるがインターフェースは同じになる処理）を実装

実行時にはテンプレートメソッドが抽象メソッドを呼び出す

### ConcreteClass

AbstractClassで定義されている抽象メソッドを実装


## メリット

クラス間のロジックが共通化できるため、

- コードの重複をなくすことができる
- 処理を呼び出す側は、同じAbstract Classから生成されたものであれば、どのサブクラスであるかを意識せずに処理を呼び出すことができる