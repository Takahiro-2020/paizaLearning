# coding: utf-8
# Your code here!

print(1)
try:
    number = 0
    # ここで止まる
    answer = 100 / number
    print(answer)
# 例外が発生した場合
# 例外ハンドラ
except ZeroDivisionError as e:
    print(e)

# 最後に必ずやりたい処理
finally:
    print(2)