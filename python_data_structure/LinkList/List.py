
class Node():
    def __init__(self, data):
        self.data = data
        self.next = None
    def setData(self,newdata):
        self.data=newdata
    def getData(self):
        return self.data
    def getNext(self):
        return self.next
    def setNext(self,newnext):
        self.next =newnext
    
class List():
    def __init__(self, *args, **kwargs):
        self.head = None
    def add(self,item):
        """[summary]
        - 创建一个节点
        - 新节点的指向下一个引用指向旧链表的第一个节点
        - 链表头的新节点的引用指向新创建的节点
        Arguments:
            item {[type]} -- [description]
        """
        tem = Node(item)
        tem.setNext(self.head)
        self.head=tem
    def isEmpty(self):
        return self.head==None
    def search(self,item):
        current = self.head
        found = False
        while current!=None and not found:
            if current.getData()==item:
                found = True
            else:
                current=current.getNext()
        
        return found
        
    def size(self):
        count = 0
        current=self.head
        while current!=None:
            count=count+1
            current=current.getNext()
        return count

    def remove(self,item):
        found = False
        current = self.head
        pervious = None
        while current!=None and not found:
            if current.getData() ==item:
                found = True
            else:
                pervious= current
                current=current.getNext()
        if pervious==None:
            self.head = current.getNext()
        else:
            pervious.setNext(current.getNext())
        return current.getData()

            
if __name__ == '__main__':
    
    mylist = List()
    mylist.add(1)
    mylist.add(34)
    mylist.add(90)
    mylist.add(78)
    
    print(mylist.isEmpty())
    print(mylist.search(34))
    print(mylist.size())
    print(mylist.remove(78))
    print(mylist.size())
