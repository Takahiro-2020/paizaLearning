# coding: utf-8
# �A�N�Z�X�����𗝉�����
# �v���C�x�[�g�ϐ��A�v���C�x�[�g���\�b�h__
# �����ʂȌĂѕ��������Python�ł͊O����Ăׂ�

class Player:
    def __init__(self, job, weapon):
        self.job = job
        # �v���C�x�[�g�ϐ��A�v���C�x�[�g�v���p�e�B
        self.__weapon = weapon

    def walk(self):
        print(self.job + "�͍r�������Ă���")
        self.__attack("�X���C��")

    # �v���C�x�[�g���\�b�h��
    def __attack(self, enemy):
        print(self.__weapon + "��" + enemy + "���U��")


player1 = Player("��m", "��")
player1.walk()
# player1.attack("�X���C��")
# print(player1.__weapon)
