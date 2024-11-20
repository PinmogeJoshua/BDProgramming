import random

choices =["剪刀","石头","布"]
player = False
cpu_score = 0
player_score = 0

while True:
    player = input("剪刀，石头，布？").capitalize()
    assert player in choices, "请输入正确的选项"
    computer = random.choice(choices)
    pass
    break
