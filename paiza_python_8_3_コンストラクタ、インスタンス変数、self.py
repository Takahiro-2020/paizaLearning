# coding: utf-8
# �ϐ����N���X�ŊǗ�����
# �R���X�g���N�^�A�C���X�^���X�ϐ�

class Player:
    # �R���X�g���N�^
    # �Ăяo�����w�肵�Ȃ��Ă�����ɌĂ΂��
    def __init__(self, job):
        # �C���X�^���X�ϐ�
        self.job = job
    
    # self�̓C���X�^���X�ϐ��������@job��
    def walk(self):
        print(self.job + "�͍r�������Ă���")

player1 = Player("��m")
player1.walk()

player2 = Player("���@�g��")
player2.walk()

# �C���X�^���X�������I�u�W�F�N�g
player1.walk()