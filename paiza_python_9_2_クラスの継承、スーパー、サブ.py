class Box:
    def __init__(self, item):
        self.item = item
    
    def open(self):
        print("宝箱を開いた。" + self.item + "を手に入れた。")

# クラス名の後ろに親クラスをかっこで指定して継承
class JewlyyBox(Box):
    def look(self):
        print("宝箱はキラキラと輝いている。")

box = Box("鋼鉄の剣")
box.open()

# 子クラスにないメソッドは親クラスから呼ばれる
# スーパークラスのコンストラクタ経由で
# オブジェクトをインスタンス化
jewlyyBox = JewlyyBox("魔法の指輪")
jewlyyBox.look()
jewlyyBox.open()