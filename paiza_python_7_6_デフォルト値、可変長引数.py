# �����̃f�t�H���g�l
# �f�t�H���g�l�̂���ϐ��͈�ԍŌ�I
def intorduce(greeting, name = "���l"):
    print("����" + name + "�ł��B" + greeting)

intorduce("�E��")
intorduce("����ɂ���")

# �ϒ��ϐ�
def intorduce(greeting, *names):
    for name in names:
        print("����" + name + "�ł��B" + greeting)

intorduce("����ɂ���", "�E��", "���l", "���m")


# �ϒ��ϐ��@�����̂悤�ɓn����
def intorduce(**people):
    for name, greeting in people.items():
        print("����" + name + "�ł��B" + greeting)
    print(people)

# ������n���킯����Ȃ����Ƃɒ���
# intorduce({hero:"�͂��߂܂���", vilager:"����ɂ���"})
intorduce(here="�͂��߂܂���", villager="����ɂ���",soldier="��낵�����肢�\���グ�܂�")
