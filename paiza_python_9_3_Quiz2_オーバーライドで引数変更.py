class Greeting:
    def __init__(self):
        self.msg = "hello"
        self.target = "paiza"

    def say_hello(self):
        print(self.msg + " " + self.target)

class Hello(Greeting):
    # ここにオーバライドするメソッドを記述する
    # 引数を変更することもできる
    def say_hello(self, target):
        print(self.msg + " " + target)


player = Hello()
player.say_hello("python")
