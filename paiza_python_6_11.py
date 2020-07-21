# coding: utf-8
# Your code here!

# 標準入力から2次元リスト

enemy_img = []
while True:
    line = input()
    if line == "_":
        break
    # splitした文字列を配列の要素に入れて二次元リストに
    enemy_img.append(line.split(","))

# print(enemy_img)

for line in enemy_img:
    for dot in line:
        # ★標準入力のデータは文字列になっている
        # 読み込んだデータをintに変換して確認
        if int(dot) == 1:
            print("#", end="")
        else:
            print(" ", end="")
    print()
