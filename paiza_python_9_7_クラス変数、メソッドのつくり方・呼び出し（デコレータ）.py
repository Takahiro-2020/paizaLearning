class Player:
    # ★　共通のクラス変数　staticになるみたい
    __charactor_count = 0
    
    # ★　クラスメソッド　clsはクラス自身
#     def summary(cls):
#         print(str(Player.__charactor_count) + "人で、スライムを攻撃した。")

    # ★　クラスメソッドは@classmethodで簡単に作れる
    # ★　これをデコレータという
    @classmethod
    def summary(cls):
        print(str(Player.__charactor_count) + "人で、スライムを攻撃した。")

    
    def __init__(self, name):
        self.name = name
        Player.__charactor_count += 1
        print(str(Player.__charactor_count) + "番目のプレーヤー" + self.name + "が登場した。")

    def attack(self, enemy):
        print(self.name + "は、" + enemy + "を攻撃した！")
    
    # ★　classmethod関数はクラスメソッドを外部提供する
    # ★　pythonではメソッドもオブジェクト
    # summary = classmethod(summary)

class Wizard(Player):
    def __init__(self):
        super().__init__("魔法使い")

    def attack(self, enemy):
        self.__spell()
        print(self.name + "は、" + enemy + "に炎を放った！")

    def __spell(self):
        print("ズバーン！")

print("=== パーティーでスライムと戦う ===")
hero = Player("勇者")
warrior = Player("戦士")
wizard = Wizard()

party = [hero, warrior, wizard]
for member in party:
    member.attack("スライム")

# print(str(Player.charactor_count) + "人で、スライムを攻撃した。")
# クラスメソッドの呼び出し
Player.summary()