# coding: utf-8
# Your code here!

# �����̗�O�ɑΉ�
print(1)
try:
    number = 0
    answer = 100 / number
    print(answer2)
# �T�u�N���X�G���[�@��̓I�ȃG���[����L�q����
except ZeroDivisionError as e:
    print("0�ł͊���Z�ł��܂���")
    print(e)
except NameError as e:
    print("����`�̕ϐ����Ăяo���Ă��܂�")
    print(e)
# ��Exception�ł�����G���[���L���b�`
# Exception�͈�ԉ��ɔz�u����
except Exception as e:
    print("�\�����ʃG���[���������܂���")
    print(e)
finally:
    print(2)
