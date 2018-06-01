

def toString(num,base):
    converString='0123456789abcdef'

    if num<base:
        print(num)
        return converString[num]
    else:
        return toString(num//base,base)+converString[num%base]
if __name__ == '__main__':
   print( toString(654,16))
   
