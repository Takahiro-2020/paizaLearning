# coding: utf-8
# �e�N���X�̃��\�b�h���Ăяo��

class Greeting:
    def __init__(self):
        self.msg = "hello"
        self.target = "paiza"

    def say_hello(self):
        print(self.msg + " " + self.target)

class Hello(Greeting):
    def say_hello(self):
        # �e�N���X�̋L�q�����p���郁�\�b�h�쐬���@
        super().say_hello()
        print("YEAH YEAH YEAH!")


player = Hello()
player.say_hello()
