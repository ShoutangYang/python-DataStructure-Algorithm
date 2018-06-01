
class Stack:
    """
    堆栈：
        LIFO: last in frist out
        - __init__ :构造函数
        - isEmpty
        - push（item）  加入到栈的顶部
        - pop 从顶部删除
        - peek 返回栈的顶部
        -isize 
        - 定义： list 的头部为栈底，list的末尾为栈顶
    
    """
    def __init__(self, *args, **kwargs):
        self.items=[]

    def isEmpty(self):
        return self.items==[]

    def push(self,item):
        """
        加入栈顶
        Arguments:
            item {[type]} -- [description]
        """
        self.items.append(item)

    def pop(self):
        """
        删除栈顶
        """
        return self.items.pop()

    def peek(self):
        """
        返回栈顶元素
        """
        return self.items[len(self.items)-1]

    def size(self):
        """
        栈的大小
        """
        return len(self.items)




    


