# coding: utf-8
# �N���X�Ƀ��\�b�h���`���悤


class Greeting:
    def __init__(self):
        self.msg = "hello"
        self.target = "paiza"

# �X�[�p�[�N���X�̃t�B�[���h�͎q�N���X���Ăяo����
class Hello(Greeting):
    # ���̉��ɁAsay_hello���\�b�h���L�q����
    def say_hello(self):
        print(self.msg + " " + self.target)


player = Hello()
player.say_hello()
