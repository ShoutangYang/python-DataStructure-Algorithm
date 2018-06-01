"""[summary]
链表
- 无序list
- 每项保存相对于其他项的位置

"""

class Node:
    """
    定义节点：
        - 构造函数
        - 获取数据
        - 获取下一个节点
        - 设置数据
        - 设置指向下一个数据
    
    """
    def __init__(self, initData):
        self.data = initData
        self.next = None
    
    def getData(self):
        return self.data
    
    def getNext(self):
        return self.next
    
    def setData(self,newData):
        self.data = newData

    def setNext(self,newNext):
        self.next = newNext



class UnorderedList:
    def __init__(self, *args, **kwargs):
        """
            接地节点
        
        """
        self.head = None

    def isEmpty(self):
        return self.head ==None
    
    def add(self,item):
        """
        - 链表每查入一个更新其链表头，
        - 初始化时的节点为链表尾

        增加的步骤：
            - 实例话一个 节点；
            - 将实例的节点的 setNext指向 之前的节点
            - 更新最新的表头节点


        
        Arguments:
            item {[type]} -- [description]
        """
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp
    
    def size(self):
        """
            链表主要的就是 链表头
        
        """
        current = self.head
        count = 0
        while current !=None:
            count =count +1
            current = current.getNext()
        
        return count

    def search(self,item):
        current = self.head
        found = False

        while current!=None  and not found:
            if current.getData()==item:
                found =True
            else:
                current = current.getNext()
        
        return found


    def remove(self,item):
        current = self.head
        previous = None

        found = False

        while not found:
            if current.getData() ==item:
                found = True
            else:
                previous=current
                current=current.getNext()
        
        if previous ==None:
            self.head = current.getNext()
        
        else:
            previous.setNext(current.getNext())
        
    def travel(self):
        cur = self.head
        tem =[]
        
        while cur!=None:
            print(cur.getData())
            tem.append(str(cur.getData()))
            cur=cur.getNext()
        
        return tem
        

        

if __name__ == '__main__':
    l = UnorderedList()
    l.add(1)
    l.add(2)
    l.add(3)
    print(l.size())
    print( l.travel())
   


        

    
