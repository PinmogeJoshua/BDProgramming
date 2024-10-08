# 从用户输入获取一个表达式
expression = input("Please input an expression: ")

def middletopost(expression):
    number = []  # 用于存储输出的后缀表达式
    stack = []   # 用于存储操作符的栈
    i = 0
    while i < len(expression):
        if expression[i].isnumeric() or expression[i] == '.':  # 如果是数字或小数点
            num = []
            while i < len(expression) and (expression[i].isnumeric() or expression[i] == '.'):
                num.append(expression[i])
                i += 1
            number.append(''.join(num))  # 将整个数字添加到输出列表
            continue  # 跳过递增i，因为已经在内部处理
        else:
            item = expression[i]
            if len(stack) == 0:  # 如果栈为空，直接将操作符压入栈
                stack.append(item)
            elif item in '*/^(':  # 如果是乘、除、乘方或左括号，直接压入栈
                stack.append(item)
            elif item == ')':  # 如果是右括号，弹出栈顶元素直到遇到左括号
                t = stack.pop()
                while t != '(':
                    number.append(t)
                    t = stack.pop()
            elif item in '+-' and stack[-1] in '*/^':  # 如果是加减操作符且栈顶是乘除或乘方操作符
                if stack.count('(') == 0:  # 如果栈中没有左括号
                    while stack:  # 弹出所有操作符
                        number.append(stack.pop())
                else:  # 如果栈中有左括号
                    t = stack.pop()
                    while t != '(':  # 弹出直到遇到左括号
                        number.append(t)
                        t = stack.pop()
                    stack.append('(')  # 将左括号重新压入栈
                stack.append(item)  # 将当前操作符压入栈
            else:  # 其他情况，直接将操作符压入栈
                stack.append(item)
        i += 1
    while stack:  # 将栈中剩余的操作符全部弹出
        number.append(stack.pop())
    
    return " ".join(number)  # 将列表转换为字符串并返回

# 打印转换后的后缀表达式
print(middletopost(expression))
