# coding: utf-8
# �N���X�ŁA�����Ɩ߂�l�̂��郁�\�b�h�����

class Item:
    # �N���X�ϐ�
    tax = 1.08
    
    def __init__(self, price, quantity):
        # �C���X�^���X�ϐ��i�N���X�ϐ��Ƃ͕ʁI�I�j
        self.price = price
        self.quantity = quantity
    
    def total(self):
        # �N���X�ϐ��̓N���X��.�ϐ���
        # return����Ζ߂�l�IJava�Ɠ����B
        return int(self.price * self.quantity * Item.tax)

apple = Item(120, 15)
total = apple.total()
print("���v���z��" + str(total) + "�~�ł�")

orange = Item(85, 32)
print("���v���z��" + str(orange.total()) + "�~�ł�")

