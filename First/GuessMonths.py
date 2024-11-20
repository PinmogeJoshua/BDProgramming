while True:
    try:
        month = int(input("请输入月份（1-12）："))
        if 1 <= month <= 12:
            break
        else:
            print("请输入1到12之间的数字。")
    except ValueError:
        print("请输入有效的数字。")

daysPerMonth = [31,28,31,30,31,30,31,31,30,31,30,31]
print(daysPerMonth[month-1])
