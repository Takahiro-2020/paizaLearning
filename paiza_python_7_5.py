# coding: utf-8
# Your code here!

# RPG�̍U���V�[��

import random

def attack(enemy):
    print("�E�҂�" + enemy + "���U�������B")
    hit = random.randint(1, 10)
    if hit < 6:
        print(enemy + "�ɁA" + str(hit) + "�̂��߁[����^�����I")
    else:
        print("�N���e�B�J���q�b�g�I" + enemy + "�ɁA100�̃_���[�W��^�����I�I")

enemies = ["�X���C��", "�����X�^�[", "�h���S��"]
for enemy in enemies:
    attack(enemy)