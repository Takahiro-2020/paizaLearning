# coding: utf-8
# Your code here!

# traceback�X�^�b�N�g���[�X��
import traceback, sys
print(1)
try:
    number = 0
    answer = 100 / number
    print(answer)
except ZeroDivisionError as e:
    print("0�ł͊���Z�ł��܂���")
    # ��O���𕶎���Ƃ��Ď擾�ł���
    # print(traceback.format_exc())

    # ���s���G���[�ɃG���[�ڍׂ��o��
    # �W���G���[�o��write ���o�͐�͐F�X�ς�����
    sys.stderr.write(traceback.format_exc())
finally:
    print(2)