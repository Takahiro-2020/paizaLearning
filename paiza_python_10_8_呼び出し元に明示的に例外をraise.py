# coding: utf-8
# Your code here!

# �Ăяo�����ɖ����I�ɗ�O��raise
def test_exception(number):
    print(2)
    # �֐����ł���O���L���b�`����
    try:
        print(3)
        answer = 100 / number
        return answer
        print(4)
    except ZeroDivisionError as e:
        print(5)
        # ��O�𖾎��I�ɂ���raise
        raise e
    print(6)

print(1)
try:
    answer = test_exception(0)
    print(7)
except ZeroDivisionError as e:
    print(6)
    print(e)
print(9)