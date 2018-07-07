def add(items):
    if len(items)==1:
        return items[0]
    else:
        print(items[0],items[1:])
        return items[0]+add(items[1:])

if __name__ == '__main__':
    mylist =[1,3,4,5,6,2,3,4,5,6,7,1]
    add=add(mylist)
    print(add)
    