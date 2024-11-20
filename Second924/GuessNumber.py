import random
# 初始化猜测次数
guess_count = 0
# 生成一个随机数
num = random.randint(1, 100)

while True:
    try:
        # 获取用户输入的数字
        number = int(input("Please guess one number: "))
        
        # 比较用户输入的数字和随机数
        if num == number:
            print("Right! You made it!")
            break
        elif num > number:
            print("A little bit smaller, please try it again")
        elif num < number:
            print("A little bit bigger, please try it again")
        
        # 增加猜测次数
        guess_count += 1
    except ValueError:
        print("输入无效，请输入一个数字")

print(f"你总共猜了 {guess_count} 次")
