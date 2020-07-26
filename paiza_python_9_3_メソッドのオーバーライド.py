class Box:
    def __init__(self, item):
        self.item = item

    def open(self):
        print("宝箱を開いた。" + self.item + "を手に入れた。")

# 子クラス
class MagicBox(Box):
    def look(self):
        print("宝箱は、怪しく輝いている。")

    # 親クラスのopenメソッドをオーバーライド
    def open(self):
        print("宝箱を開いた。" + self.item + "が襲ってきた！")

box = Box("鋼鉄の剣")
box.open()

magicbox = MagicBox("モノマネモンスター")
magicbox.look()
magicbox.open()