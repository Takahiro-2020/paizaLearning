# coding: utf-8
# Your code here!

# RPGの攻撃シーン

import random

def attack(enemy):
    print("勇者は" + enemy + "を攻撃した。")
    hit = random.randint(1, 10)
    if hit < 6:
        print(enemy + "に、" + str(hit) + "のだめーじを与えた！")
    else:
        print("クリティカルヒット！" + enemy + "に、100のダメージを与えた！！")

enemies = ["スライム", "モンスター", "ドラゴン"]
for enemy in enemies:
    attack(enemy)