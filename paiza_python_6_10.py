# coding: utf-8
# Your code here!

# 2ŸŒ³ƒŠƒXƒg‚Å’n}‚ğ•\¦‚·‚é

landmap = [["X" for i in range(20)] for j in range(10)]
landmap[0][0] = "é"
landmap[0][19] = "’¬"
landmap[9][19] = "’¬"
for i,line in enumerate(landmap):
    print(str(i) + ":", end="")
    for j, area in enumerate(line):
        if (i % 2 == 0 or j % 3 == 0) and area == "X":
            print("{", end="")
        else:
            print(area, end="")
    print()