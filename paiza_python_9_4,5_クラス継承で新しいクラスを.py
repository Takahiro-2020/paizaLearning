class Player:
    def __init__(self, name):
        self.name = name

    def attack(self, enemy):
        print(self.name + "�́A" + enemy + "���U�������I")

# ���N���X���p������ƐV�����N���X�����₷��
class Wizard(Player):
    def attack(self, enemy):
        print("�Y�o�[���I")
        print(self.name + "�́A" + enemy + "�ɉ���������I")

print("=== �p�[�e�B�[�ŃX���C���Ɛ키 ===")
hero = Player("�E��")
# hero.attack("�X���C��")
warrior = Player("��m")
wizard = Wizard("���@�g��")

party = [hero, warrior, wizard]
for member in party:
    member.attack("�X���C��")
