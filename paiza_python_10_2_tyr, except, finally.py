# coding: utf-8
# Your code here!

print(1)
try:
    number = 0
    # �����Ŏ~�܂�
    answer = 100 / number
    print(answer)
# ��O�����������ꍇ
# ��O�n���h��
except ZeroDivisionError as e:
    print(e)

# �Ō�ɕK����肽������
finally:
    print(2)