# ‰Šú‚Ì’n}
landmap = [["X" for i in range(19)] for j in range(10)]
landmap[2][9] = "é"
landmap[0][0] = "’¬"
landmap[0][18] = "’¬"
landmap[9][0] = "’¬"
landmap[9][18] = "’¬"

# ’n}‚É“¹‚ğì‚é
for i, line in enumerate(landmap):
    for j, area in enumerate(line):
        # ‚±‚±‚©‚ç‘«‚è‚È‚¢‚Æ‚±‚ë‚ğ“ü—Í‚µ‚Ä‚­‚¾‚³‚¢
        if (i % 9 == 0 or j % 9 == 0) and area == "X":
            print("{", end="")
        else:
            print(area, end="")
    print()
