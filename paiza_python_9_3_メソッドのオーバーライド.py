class Box:
    def __init__(self, item):
        self.item = item

    def open(self):
        print("�󔠂��J�����B" + self.item + "����ɓ��ꂽ�B")

# �q�N���X
class MagicBox(Box):
    def look(self):
        print("�󔠂́A�������P���Ă���B")

    # �e�N���X��open���\�b�h���I�[�o�[���C�h
    def open(self):
        print("�󔠂��J�����B" + self.item + "���P���Ă����I")

box = Box("�|�S�̌�")
box.open()

magicbox = MagicBox("���m�}�l�����X�^�[")
magicbox.look()
magicbox.open()