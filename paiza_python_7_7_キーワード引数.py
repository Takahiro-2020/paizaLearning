# coding: utf-8
# Your code here!

# キーワード引数
# 関数の引数にラベル付けられる

def say_hello(greeting = "hello", target = "world"):
    print(greeting + " " + target)

say_hello()
say_hello("こんにちは、", "皆さん")
say_hello("good morning!")
# ラベルを使って渡す
say_hello(greeting = "こんにちは", target = "皆さん")
say_hello(target = "ネコ先生", greeting = "おはようございます")
say_hello(target = "ネコ先生")
say_hello(greeting = "おはようございます")
