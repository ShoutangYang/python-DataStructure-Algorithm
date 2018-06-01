from stack import Stack
"""
括号简单匹配的问题
- 区分括号是否匹配
- 使用stack实现
- 从左到右，（ 为入栈 ， ) 为出栈
- 情况1： （ 数量多余 ） 情况
- 情况2： （ 数量小于 ） 情况
"""
def parChencker(symbolString):
    s= Stack()
    balance = True
    index =0

    while index <len(symbolString) and balance:
        symbol = symbolString[index]

        if symbol =="(":
            s.push(symbol)
        else:
            if s.isEmpty():
                balance =False
            else:
                s.pop()
               

        index = index+1
    
    if balance and s.isEmpty():
        return True
    else:
        return False


if __name__ == '__main__':
    print(parChencker("(((((((())))))))))"))

    print(parChencker("))))"))

    print(parChencker("()((())())"))
    