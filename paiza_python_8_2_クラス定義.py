# coding: utf-8
# �N���X���쐬����

# �N���X���w��
class Player:
    # ���\�b�h��
    # �N���X���̃��\�b�h�͕K��self������`
    def walk(self):
        print("�E�҂͍r�������Ă���")
    
    def attack(self, enemy):
        print("�E�҂�" + enemy + "���U������")

# �N���X����I�u�W�F�N�g���C���X�^���X��
player1 = Player()
player1.walk()
player1.attack("�X���C��")