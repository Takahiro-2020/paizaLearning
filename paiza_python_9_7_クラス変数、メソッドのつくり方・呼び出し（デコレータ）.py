class Player:
    # ���@���ʂ̃N���X�ϐ��@static�ɂȂ�݂���
    __charactor_count = 0
    
    # ���@�N���X���\�b�h�@cls�̓N���X���g
#     def summary(cls):
#         print(str(Player.__charactor_count) + "�l�ŁA�X���C�����U�������B")

    # ���@�N���X���\�b�h��@classmethod�ŊȒP�ɍ���
    # ���@������f�R���[�^�Ƃ���
    @classmethod
    def summary(cls):
        print(str(Player.__charactor_count) + "�l�ŁA�X���C�����U�������B")

    
    def __init__(self, name):
        self.name = name
        Player.__charactor_count += 1
        print(str(Player.__charactor_count) + "�Ԗڂ̃v���[���[" + self.name + "���o�ꂵ���B")

    def attack(self, enemy):
        print(self.name + "�́A" + enemy + "���U�������I")
    
    # ���@classmethod�֐��̓N���X���\�b�h���O���񋟂���
    # ���@python�ł̓��\�b�h���I�u�W�F�N�g
    # summary = classmethod(summary)

class Wizard(Player):
    def __init__(self):
        super().__init__("���@�g��")

    def attack(self, enemy):
        self.__spell()
        print(self.name + "�́A" + enemy + "�ɉ���������I")

    def __spell(self):
        print("�Y�o�[���I")

print("=== �p�[�e�B�[�ŃX���C���Ɛ키 ===")
hero = Player("�E��")
warrior = Player("��m")
wizard = Wizard()

party = [hero, warrior, wizard]
for member in party:
    member.attack("�X���C��")

# print(str(Player.charactor_count) + "�l�ŁA�X���C�����U�������B")
# �N���X���\�b�h�̌Ăяo��
Player.summary()