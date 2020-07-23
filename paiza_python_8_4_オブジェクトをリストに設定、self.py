# coding: utf-8
# RPGの敵クラスを作る
# クラスは分類の意味もある
class Enemy:
    def __init__(self, name):
        self.name = name
        
    def attack(self):
        print(self.name + "は勇者を攻撃した")

# リストにオブジェクトを設定
enemies = []
enemies.append(Enemy("スライム"))
enemies.append(Enemy("モンスター"))
enemies.append(Enemy("ドラゴン"))

# ループでオブジェクトを回す
for enemy in enemies:
    enemy.attack()