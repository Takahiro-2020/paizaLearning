# coding: utf-8
# クラスを作成する

# クラス名指定
class Player:
    # メソッド名
    # クラス内のメソッドは必ずself引数定義
    def walk(self):
        print("勇者は荒野を歩いていた")
    
    def attack(self, enemy):
        print("勇者は" + enemy + "を攻撃した")

# クラスからオブジェクトをインスタンス化
player1 = Player()
player1.walk()
player1.attack("スライム")