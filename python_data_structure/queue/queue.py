"""
队列：
    - 有序结合
    - FIFO
    - 队列类似 缓存
    - 入队列，把数据放在 list 的列头
    - 出队列 ，把list 末尾数据取出
    - 定义 ： list  头为队 尾； list 的最后为队首


"""
class Queue:
    def __init__(self):
        self.items =[]

    def enqueue(self,item):
        self.items.insert(0,item)
    def dequeue(self):
        return self.items.pop()
    
    def size(self):
        return len(self.items)
    def isEmpty(self):
        return self.items ==[]
    

