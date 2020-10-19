# Template Method

## 概要

インスタンス生成のテンプレ（雛形）をスーパークラスで定義し、具体的な生成処理をサブクラスで定義することで、処理とインターフェースの共通化を行う

Template Methodをインスタンス生成に適用したもの

## クラス図

![Wikipediaより](https://upload.wikimedia.org/wikipedia/commons/2/2a/W3sDesign_Template_Method_Design_Pattern_UML.jpg)

## 登場人物

### Product

生成されるインスタンスが持つインターフェースを定義する抽象クラス

### Creator

Productを生成するインターフェースを定義する抽象クラス

生成処理の実装に関しては、以下の方法が考えられる

- 抽象メソッドとしてインターフェースのみを実装
- 生成のデフォルト処理を実装
- 生成処理をマストにするために抽象メソッドにエラー処理を組み込んで実装

### ConcreteProduct

Productの具体的な処理を定義する

### ConcreteCreator

Factoryの具体的な処理を定義する


## メリット

クラス間のロジックが共通化できるため、

- コードの重複をなくすことができる
- 処理を呼び出す側は、同じAbstract Classから生成されたものであれば、どのサブクラスであるかを意識せずに処理を呼び出すことができる

FactoryとProductを分けることで、互いに知る必要のない処理を知る必要がなくなる

例えば、データから生成されるConcreteProductがあった場合、データの読み込みをConcreteFactoryで定義することでConcreteProductをデータに依存しないようにすることができる