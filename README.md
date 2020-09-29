# practice-design-pattern-python

Pythonでのデザインパターンの勉強

## Reference

- [増補改訂版Java言語で学ぶデザインパターン入門](https://www.amazon.co.jp/%E5%A2%97%E8%A3%9C%E6%94%B9%E8%A8%82%E7%89%88Java%E8%A8%80%E8%AA%9E%E3%81%A7%E5%AD%A6%E3%81%B6%E3%83%87%E3%82%B6%E3%82%A4%E3%83%B3%E3%83%91%E3%82%BF%E3%83%BC%E3%83%B3%E5%85%A5%E9%96%80-%E7%B5%90%E5%9F%8E-%E6%B5%A9/dp/4797327030)
- [実践 Python 3](https://www.amazon.co.jp/%E5%AE%9F%E8%B7%B5-Python-3-Mark-Summerfield/dp/4873117399/ref=sr_1_1?__mk_ja_JP=%E3%82%AB%E3%82%BF%E3%82%AB%E3%83%8A&dchild=1&keywords=%E5%AE%9F%E8%B7%B5Python&qid=1601364716&s=books&sr=1-1)

## デザインパターンの目的

プログラムを再利用可能にすること

※ クリーンアーキテクチャ読み直して修正する

- プログラムは作って終わりではなく、常に変更・拡張されるものという前提を置いて、
- 変更・拡張時に、追加機能の実装だけして既存機能の修正は最小限になるようにすることを目指す
- 例）データの取得元が変更になった→既存のDAOの抽象クラス継承した新しいDAO作って呼び出し元で指定のDAOそれにして作業終わり

## UMLの基礎知識

### 各種矢印

矢印＝視線、対象のことを知っているかどうか

知っている場合、その対象が変更された時に変更する必要がある

#### クラスの階層関係

クラスを継承しているため、その対象について知っている

![Wikiprediaより](https://upload.wikimedia.org/wikipedia/commons/thumb/6/66/KP-UML-Generalization-20060325.svg/600px-KP-UML-Generalization-20060325.svg.png)

#### インターフェースと実装

対象クラスのインターフェースを実装しているため、その対象について知っている

![Wikiprediaより](https://upload.wikimedia.org/wikipedia/commons/f/f8/Class_Dependency.png)

#### 集約

対象クラスのインスタンスを持っているため、その対象について知っている

![Wikiprediaより](https://upload.wikimedia.org/wikipedia/commons/thumb/2/2a/KP-UML-Aggregation-20060420.svg/600px-KP-UML-Aggregation-20060420.svg.png)

### アクセス制御

メソッドやフィールドのアクセス元の制限を表す

- +：public、どこからでもアクセス可能
- -：private、同じクラスの内からのみアクセス可能
- \#：protected、同じクラス / サブクラス / 同じパッケージ内のクラス からのみアクセス可能
- ~：同じパッケージ内からのみアクセス可能
