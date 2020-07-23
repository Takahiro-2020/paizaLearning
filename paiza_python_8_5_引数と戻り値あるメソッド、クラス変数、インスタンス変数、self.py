# coding: utf-8
# クラスで、引数と戻り値のあるメソッドを作る

class Item:
    # クラス変数
    tax = 1.08
    
    def __init__(self, price, quantity):
        # インスタンス変数（クラス変数とは別！！）
        self.price = price
        self.quantity = quantity
    
    def total(self):
        # クラス変数はクラス名.変数名
        # returnすれば戻り値！Javaと同じ。
        return int(self.price * self.quantity * Item.tax)

apple = Item(120, 15)
total = apple.total()
print("合計金額は" + str(total) + "円です")

orange = Item(85, 32)
print("合計金額は" + str(orange.total()) + "円です")

