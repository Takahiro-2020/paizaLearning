class Box:
    def __init__(self, item):
        self.item = item
    
    def open(self):
        print("�󔠂��J�����B" + self.item + "����ɓ��ꂽ�B")

# �N���X���̌��ɐe�N���X���������Ŏw�肵�Čp��
class JewlyyBox(Box):
    def look(self):
        print("�󔠂̓L���L���ƋP���Ă���B")

box = Box("�|�S�̌�")
box.open()

# �q�N���X�ɂȂ����\�b�h�͐e�N���X����Ă΂��
# �X�[�p�[�N���X�̃R���X�g���N�^�o�R��
# �I�u�W�F�N�g���C���X�^���X��
jewlyyBox = JewlyyBox("���@�̎w��")
jewlyyBox.look()
jewlyyBox.open()