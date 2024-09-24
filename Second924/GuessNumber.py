import random
count = 0

while True:
    num = random.randint(1,100)
    number = int(input("Please guess one number:"))
    if num == number:
        print("Right! You made it!")
        break
    elif num > number:
        print("A little bit smaller, please try it again")
        count += 1
    elif num < number:
        print("A little bit bigger, please try it again")
        count += 1
print(f"你总共猜了{count}次")
