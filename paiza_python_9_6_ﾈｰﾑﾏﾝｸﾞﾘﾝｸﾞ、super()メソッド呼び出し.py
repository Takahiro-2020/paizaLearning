class Player:
    def __init__(self, name):
        self.name = name

    def attack(self, enemy):
        print(self.name + "は、" + enemy + "を攻撃した！")

class Wizard(Player):
    # ★sスーパークラスのメソッド呼び出し
    # super().メソッド名
    def __init__(self):
        super().__init__("魔法使い")

    def attack(self, enemy):
        # ★クラスの別のメソッド呼べる
        # ★self.メソッド名！！
        self.__spell()
        print(self.name + "は、" + enemy + "に炎を放った！")
    
    # 固有のメソッドだからプライベートに
    def __spell(self):
        print("ズバーン！")

print("=== パーティーでスライムと戦う ===")
hero = Player("勇者")
# hero.attack("スライム")
warrior = Player("戦士")
#wizard = Wizard("魔法使い") ★継承したコンストラクタ
wizard = Wizard()

party = [hero, warrior, wizard]
for member in party:
    member.attack("スライム")

# ネームマングリング（メソッド名、クラス名を変更できる）
# 特殊な呼び出しでプライベートメソッド呼べる
wizard._Wizard__spell()