from stack import Stack

def parChecker(symbolString):

    s =Stack()
    blance = True
    index = 0

    while index <len(symbolString) and blance:
        
        symbol = symbolString[index]
        if symbol in '({[' :
            s.push(symbol)
        else:
            if s.isEmpty():
                blance = False
            else:
                top =s.pop()
                if not matches(top,symbol):
                    blance =False

        index =index+1

    if blance and s.isEmpty():
        return True
    else:
        return False
    
                
def matches(open,close):
    opens ='({['
    closes =")}]"

    return opens.index(open) ==closes.index(close)

if __name__ == '__main__':
    print(parChecker('()[]{}'))

