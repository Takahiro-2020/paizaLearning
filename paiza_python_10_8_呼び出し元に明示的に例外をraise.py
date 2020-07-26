# coding: utf-8
# Your code here!

# 呼び出し元に明示的に例外をraise
def test_exception(number):
    print(2)
    # 関数側でも例外をキャッチする
    try:
        print(3)
        answer = 100 / number
        return answer
        print(4)
    except ZeroDivisionError as e:
        print(5)
        # 例外を明示的にしてraise
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