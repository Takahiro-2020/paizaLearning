# coding: utf-8
# �����̓��ӂȌ����
# Let's �`�������W�I�I

# ��s�ړǎ�@���҂̐��A�x���҂̐��A�����̉�
number = input().split(" ")
# print(len(number))
# print("���Ґ� �x���Ґ� ������" + str(number))
kouhosyaNum = int(number[0])
sijisyaNum = int(number[1])
enzetuNum = int(number[2])

# ���҂̐������x���҃��X�g�����������쐬
sijiDic = {}
for i in range(kouhosyaNum):
    # ��i + 1�̕�����������
    sijiDic[i + 1] = 0
# print(sijiDic)

# �����̉񐔂����J��Ԃ�
for j in range(enzetuNum):
    # ��s�ڈȍ~�ǎ�@����������҂̔ԍ��擾
    turnNum = int(input())
    # print(turnNum)
    
    # ���Ҕԍ��̎x���҃��X�g�ɒN���x�����Ă��Ȃ��x���҂Ƒ����҂̎x���҂�ǉ�����
    # ���҂̎x���҂𑝂₷
    tmpShijisyaNum = sijiDic[turnNum]
    tmpShijisyaNum += 1
    # print("���҂̎x���҃e���v" + str(tmpShijisyaNum))
    sijiDic[turnNum] = tmpShijisyaNum
    # print("��������̌��҂̎x����" + str(turnNum) + " " + str(sijiDic[turnNum]))
    # �x���҂̐������炷
    if sijisyaNum > 0:
        sijisyaNum -= 1
        # print("��������̎x���Ґ�" + str(sijisyaNum))

    # ���@�����҂̎x���҂����炷
    for key, otherShizisyaNum in sijiDic.items():
        # print("���Ҕԍ�" + str(key))
        if key != turnNum:
            # print("�����Ҏx���Ґ�" + str(key) + " " +str(otherShizisyaNum))
            if otherShizisyaNum > 0:

                # ���̎x���҂̐������炷
                # otherShizisyaNum -= 1
                sijiDic[key] -= 1
                # print("�x���҂��������I")
                # print("��������̑����Ҏx���Ґ�" + str(key) + " " +str(sijiDic[key]))
                
                # �����������҂Ɏx���҂���l�ړ�
                sijiDic[turnNum] += 1
                # print("�����҂̎x���Ґ�" + str(sijiDic[turnNum]))
                
    # print(str(j) + "��ډ��������I")
    # print()

# print(sijiDic)

# �ő�̎x���Ґ��������҂���������T��
# max�̎x���Ґ����擾
maxShijisyaNum = max(sijiDic.values())
for key, shijisyaNum in sijiDic.items():
    if maxShijisyaNum == shijisyaNum:
        # max�̎x���҂������Ҕԍ����o��
        print(key)
