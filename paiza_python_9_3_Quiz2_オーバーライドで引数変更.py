class Greeting:
    def __init__(self):
        self.msg = "hello"
        self.target = "paiza"

    def say_hello(self):
        print(self.msg + " " + self.target)

class Hello(Greeting):
    # �����ɃI�[�o���C�h���郁�\�b�h���L�q����
    # ������ύX���邱�Ƃ��ł���
    def say_hello(self, target):
        print(self.msg + " " + target)


player = Hello()
player.say_hello("python")
