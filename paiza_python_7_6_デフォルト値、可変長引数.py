# 引数のデフォルト値
# デフォルト値のある変数は一番最後！
def intorduce(greeting, name = "村人"):
    print("私は" + name + "です。" + greeting)

intorduce("勇者")
intorduce("こんにちは")

# 可変長変数
def intorduce(greeting, *names):
    for name in names:
        print("私は" + name + "です。" + greeting)

intorduce("こんにちは", "勇者", "村人", "兵士")


# 可変長変数　辞書のように渡せる
def intorduce(**people):
    for name, greeting in people.items():
        print("私は" + name + "です。" + greeting)
    print(people)

# 辞書を渡すわけじゃないことに注意
# intorduce({hero:"はじめまして", vilager:"こんにちは"})
intorduce(here="はじめまして", villager="こんにちは",soldier="よろしくお願い申し上げます")
