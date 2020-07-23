# coding: utf-8
# Your code here!

# スコープを理解する
# pythonは関数の中と外は全く独立している
# ローカル変数　関数内だけ
# グローバル変数　関数の中でも外でも使える
message = "paiza"
a = 10
b = 20

def sum(x, y):
    a = 3
    # 関数の中からの変更は許可されない
    # 参照のみ
    # message += "paiza"
    
    # globalをつければ変更できる
    # あまり利用は推奨されていない
    global message
    message += "paiza"
    print(message + " " + str(a))
    return x + y

num = sum(a, b)
print(num)
print(message + " " + str(a))