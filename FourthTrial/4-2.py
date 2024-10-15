"""
在PI(前一亿位)文件中,查找你们自己的生日,年份4位+两位月份+两位日期
"""

def read_large_file(file_path):
    with open(file_path, 'r') as file:
        for line in file:
            yield line

def process(file_path, birthday):
    # 调用 read_large_file 函数，逐行读取文件内容
    file = read_large_file(file_path)
    
    # 初始化一个空字符串，用于存储 PI 数字
    pi_digits = ""
    
    # 遍历文件的每一行
    for line in file:
        # 去掉行首尾的空白字符，并将其添加到 pi_digits 字符串中
        pi_digits += line.strip()
        
        # 检查生日字符串是否在 pi_digits 中
        if birthday in pi_digits:
            # 如果找到生日字符串，打印找到的信息并返回
            print(f"Found birthday {birthday} in PI digits.")
            return
    
    # 如果遍历完所有行后仍未找到生日字符串，打印未找到的信息
    print(f"Birthday {birthday} not found in the file.")

if __name__ == "__main__":
    file_path = '第四次上机/pi.txt'
    birthday = input("Please input your birthday (YYYYMMDD): ")
    
    if len(birthday) != 8:
        print("Invalid input. Please enter in the format YYYYMMDD.")
    else:
        process(file_path, birthday)
