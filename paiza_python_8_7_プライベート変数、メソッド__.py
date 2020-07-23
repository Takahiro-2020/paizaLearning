# coding: utf-8
# アクセス制限を理解する
# プライベート変数、プライベートメソッド__
# ★特別な呼び方をするとPythonでは外から呼べる

class Player:
    def __init__(self, job, weapon):
        self.job = job
        # プライベート変数、プライベートプロパティ
        self.__weapon = weapon

    def walk(self):
        print(self.job + "は荒野を歩いていた")
        self.__attack("スライム")

    # プライベートメソッド化
    def __attack(self, enemy):
        print(self.__weapon + "で" + enemy + "を攻撃")


player1 = Player("戦士", "剣")
player1.walk()
# player1.attack("スライム")
# print(player1.__weapon)
