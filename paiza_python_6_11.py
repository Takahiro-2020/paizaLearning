# coding: utf-8
# Your code here!

# �W�����͂���2�������X�g

enemy_img = []
while True:
    line = input()
    if line == "_":
        break
    # split�����������z��̗v�f�ɓ���ē񎟌����X�g��
    enemy_img.append(line.split(","))

# print(enemy_img)

for line in enemy_img:
    for dot in line:
        # ���W�����͂̃f�[�^�͕�����ɂȂ��Ă���
        # �ǂݍ��񂾃f�[�^��int�ɕϊ����Ċm�F
        if int(dot) == 1:
            print("#", end="")
        else:
            print(" ", end="")
    print()
