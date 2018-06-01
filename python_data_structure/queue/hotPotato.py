from queue import Queue


def hotPotato(nameList,num):
    
    simQueue = Queue()

    for name in  nameList:
        simQueue.enqueue(name)
    print(simQueue.items)
    while simQueue.size()>1:
        for i in range(num):
            simQueue.enqueue(simQueue.dequeue())
        
        simQueue.dequeue()
        print(simQueue.items)

    return simQueue.dequeue()


if __name__ == '__main__':
    
    print(hotPotato(['1','2','3','4','5','6'],3))
    
    # ['6', '5', '4', '3', '2', '1']
    # ['3', '2', '1', '6', '5']
    # ['1', '6', '5', '3']
    # ['6', '5', '3']
    # ['6', '5']
    # ['5']
    # 5