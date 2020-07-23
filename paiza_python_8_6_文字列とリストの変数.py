# coding: utf-8
# 文字列とリストのメソッドを使ってみよう

text = "pYthon"
print(text)
# 先頭だけ大文字
print(text.capitalize())
# 全部大文字
print(text.upper())

# 文字列分割
players = "勇者,戦士,魔法使い,忍者"
list = players.split(",")
print(list)

# リストで使えるメソッド
# 削除
list.remove("忍者")
print(list)
# 追加
list.append("霧島")
print(list)