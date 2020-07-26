# coding: utf-8
# Your code here!

print(1)
try:
    print(2)
    raise Exception("意図的な例外")
    print(3)
except Exception as e:
    print("予期せぬエラーが発生しました")
    print(e)
finally:
    print(4)
