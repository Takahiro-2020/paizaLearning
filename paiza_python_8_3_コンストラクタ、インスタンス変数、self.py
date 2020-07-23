# coding: utf-8
# 変数をクラスで管理する
# コンストラクタ、インスタンス変数

class Player:
    # コンストラクタ
    # 呼び出しを指定しなくても勝手に呼ばれる
    def __init__(self, job):
        # インスタンス変数
        self.job = job
    
    # selfはインスタンス変数を示す　jobね
    def walk(self):
        print(self.job + "は荒野を歩いていた")

player1 = Player("戦士")
player1.walk()

player2 = Player("魔法使い")
player2.walk()

# インスタンス化したオブジェクト
player1.walk()