class Player:
    def __init__(self, name):
        self.name = name

    def attack(self, enemy):
        print(self.name + "�́A" + enemy + "���U�������I")

class Wizard(Player):
    # ��s�X�[�p�[�N���X�̃��\�b�h�Ăяo��
    # super().���\�b�h��
    def __init__(self):
        super().__init__("���@�g��")

    def attack(self, enemy):
        # ���N���X�̕ʂ̃��\�b�h�Ăׂ�
        # ��self.���\�b�h���I�I
        self.__spell()
        print(self.name + "�́A" + enemy + "�ɉ���������I")
    
    # �ŗL�̃��\�b�h������v���C�x�[�g��
    def __spell(self):
        print("�Y�o�[���I")

print("=== �p�[�e�B�[�ŃX���C���Ɛ키 ===")
hero = Player("�E��")
# hero.attack("�X���C��")
warrior = Player("��m")
#wizard = Wizard("���@�g��") ���p�������R���X�g���N�^
wizard = Wizard()

party = [hero, warrior, wizard]
for member in party:
    member.attack("�X���C��")

# �l�[���}���O�����O�i���\�b�h���A�N���X����ύX�ł���j
# ����ȌĂяo���Ńv���C�x�[�g���\�b�h�Ăׂ�
wizard._Wizard__spell()