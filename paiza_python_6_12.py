# coding: utf-8
# Your code here!

# 2�������X�g�ŉ摜��z�u

# �摜�p���X�g
players_img = [
    "https://paiza-webapp.s3.amazonaws.com/files/learning/rpg/Empty.png",
    "https://paiza-webapp.s3.amazonaws.com/files/learning/rpg/Dragon.png",
    "https://paiza-webapp.s3.amazonaws.com/files/learning/rpg/Crystal.png",
    "https://paiza-webapp.s3.amazonaws.com/files/learning/rpg/Hero.png",
    "https://paiza-webapp.s3.amazonaws.com/files/learning/rpg/Heroine.png"]

# �z�u�f�[�^�ǂݍ���
team = []
while True:
    line = input()
    if line == "_":
        break
    team.append(line.split(","))
print(team)

# �z�u�ɍ��킹�ĕ\��
print("<table>")
for line in team:
    # print(line)
    print("<tr>")
    for person in line:
        print("<td><img src='" + players_img[int(person)] + "'></td>")
    print("</tr>")
print("</table>")