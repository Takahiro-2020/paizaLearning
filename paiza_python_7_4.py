# coding: utf-8
# Your code here!

# �X�R�[�v�𗝉�����
# python�͊֐��̒��ƊO�͑S���Ɨ����Ă���
# ���[�J���ϐ��@�֐�������
# �O���[�o���ϐ��@�֐��̒��ł��O�ł��g����
message = "paiza"
a = 10
b = 20

def sum(x, y):
    a = 3
    # �֐��̒�����̕ύX�͋�����Ȃ�
    # �Q�Ƃ̂�
    # message += "paiza"
    
    # global������ΕύX�ł���
    # ���܂藘�p�͐�������Ă��Ȃ�
    global message
    message += "paiza"
    print(message + " " + str(a))
    return x + y

num = sum(a, b)
print(num)
print(message + " " + str(a))