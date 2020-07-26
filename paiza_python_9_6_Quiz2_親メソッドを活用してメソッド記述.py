# coding: utf-8
# 親クラスのメソッドを呼び出す

class Greeting:
    def __init__(self):
        self.msg = "hello"
        self.target = "paiza"

    def say_hello(self):
        print(self.msg + " " + self.target)

class Hello(Greeting):
    def say_hello(self):
        # 親クラスの記述を活用するメソッド作成方法
        super().say_hello()
        print("YEAH YEAH YEAH!")


player = Hello()
player.say_hello()
