# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！

# 一行目読取　候補者の数、支持者の数、演説の回数
number = input().split(" ")
# print(len(number))
# print("候補者数 支持者数 演説回数" + str(number))
kouhosyaNum = int(number[0])
sijisyaNum = int(number[1])
enzetuNum = int(number[2])

# 候補者の数だけ支持者リストを持つ辞書を作成
sijiDic = {}
for i in range(kouhosyaNum):
    # ★i + 1の方がいいかも
    sijiDic[i + 1] = 0
# print(sijiDic)

# 演説の回数だけ繰り返す
for j in range(enzetuNum):
    # 二行目以降読取　演説する候補者の番号取得
    turnNum = int(input())
    # print(turnNum)
    
    # 候補者番号の支持者リストに誰も支持していない支持者と他候補者の支持者を追加する
    # 候補者の支持者を増やす
    tmpShijisyaNum = sijiDic[turnNum]
    tmpShijisyaNum += 1
    # print("候補者の支持者テンプ" + str(tmpShijisyaNum))
    sijiDic[turnNum] = tmpShijisyaNum
    # print("増えた後の候補者の支持者" + str(turnNum) + " " + str(sijiDic[turnNum]))
    # 支持者の数を減らす
    if sijisyaNum > 0:
        sijisyaNum -= 1
        # print("減った後の支持者数" + str(sijisyaNum))

    # ★　他候補者の支持者を減らす
    for key, otherShizisyaNum in sijiDic.items():
        # print("候補者番号" + str(key))
        if key != turnNum:
            # print("他候補者支持者数" + str(key) + " " +str(otherShizisyaNum))
            if otherShizisyaNum > 0:

                # 他の支持者の数を減らす
                # otherShizisyaNum -= 1
                sijiDic[key] -= 1
                # print("支持者が減った！")
                # print("減った後の他候補者支持者数" + str(key) + " " +str(sijiDic[key]))
                
                # 演説した候補者に支持者を一人移動
                sijiDic[turnNum] += 1
                # print("演説者の支持者数" + str(sijiDic[turnNum]))
                
    # print(str(j) + "回目演説完了！")
    # print()

# print(sijiDic)

# 最大の支持者数を持つ候補者を辞書から探す
# maxの支持者数を取得
maxShijisyaNum = max(sijiDic.values())
for key, shijisyaNum in sijiDic.items():
    if maxShijisyaNum == shijisyaNum:
        # maxの支持者を持つ候補者番号を出力
        print(key)
