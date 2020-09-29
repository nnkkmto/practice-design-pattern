"""
継承によるAdapterパターン
"""
import abc

class Banner:
    """
    Adaptee：呼び出したい機能があるが、必要なインターフェースを持っていないもの
    """
    def __init__(self, string: str):
        self.string = string

    def show_with_paren(self):
        print(f"( {self.string} )")

    def show_with_aster(self):
        print(f"* {self.string} *")


class Print(abc.ABC):
    """
    Target：必要なインターフェースを定める
    """
    @abc.abstractmethod
    def print_weak(self):
        pass

    def print_strong(self):
        pass


class PrintBannerClass(Banner, Print):
    """
    ※ 継承によるadapterパターン
    Adapter：Targetのインターフェースを守りつつAdapteeのメソッドを使用する
    →　adapteeのメソッドを持つようになるため、pythonでは委譲によるadapterパターンを使うべき
    """
    def __init__(self, string: str):
        super(PrintBannerClass, self).__init__(string)

    def print_weak(self):
        self.show_with_paren()

    def print_strong(self):
        self.show_with_aster()


class PrintBannerObject(Print):
    """
    ※ 委譲によるadapterパターン
    Adapter：Targetのインターフェースを守りつつAdapteeのメソッドを使用する
    """
    def __init__(self, string: str):
        super(PrintBannerObject, self).__init__()
        self.banner = Banner(string)

    def print_weak(self):
        self.banner.show_with_paren()

    def print_strong(self):
        self.banner.show_with_aster()

def main():
    # 継承によるadapterパターン
    p = PrintBannerClass("Hello")
    p.print_weak()
    p.print_strong()

    # adapteeのメソッドが使えてしまうため、pythonでは委譲によるadapterパターンを使用する
    p.show_with_paren()
    p.show_with_aster()

    # 委譲によるadapterパターン
    p = PrintBannerObject("Hello")
    p.print_weak()
    p.print_strong()