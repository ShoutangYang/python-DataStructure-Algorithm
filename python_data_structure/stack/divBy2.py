from stack import Stack

def didBy2(num):
    d = Stack()
    while num>0:
        rem= num%2
        d.push(rem)
        num = num//2
    binstring=''
    while not d.isEmpty():
        binstring = binstring+str(d.pop())
   
    return binstring

def  baseCover(num,base):
    n =Stack()

    while num>0:
        rem = num%base
        n.push(rem)
        num=num//base
    
    baseString = ''
    while not n.isEmpty():
        baseString = baseString+str(n.pop())
    return baseString

if __name__ == '__main__':
    
    print(baseCover(100,16))

    


