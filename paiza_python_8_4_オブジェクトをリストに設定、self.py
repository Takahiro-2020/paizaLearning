# coding: utf-8
# RPG�̓G�N���X�����
# �N���X�͕��ނ̈Ӗ�������
class Enemy:
    def __init__(self, name):
        self.name = name
        
    def attack(self):
        print(self.name + "�͗E�҂��U������")

# ���X�g�ɃI�u�W�F�N�g��ݒ�
enemies = []
enemies.append(Enemy("�X���C��"))
enemies.append(Enemy("�����X�^�["))
enemies.append(Enemy("�h���S��"))

# ���[�v�ŃI�u�W�F�N�g����
for enemy in enemies:
    enemy.attack()