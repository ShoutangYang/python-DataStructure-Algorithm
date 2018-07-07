class BinaryTree():
    def __init__(self, rootObj):
        self.key = rootObj
        self.leftChild = None
        self.rightChild= None
    
    def insertLeftChild(self,newNode):
        if self.leftChild ==None:
            self.leftChild=BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.leftChild =self.leftChild
            self.leftChild =t
    
    def insertRighChild(self,newNode):
        if self.rightChild==None:
            self.rightChild = BinaryTree(newNode)
        else:
            t= BinaryTree(newNode)
            t.rightChild = self.rightChild
            self.rightChild = t
    
    def getRootValue(self):
        return self.key
    def setRootValue(self,newroot):
        self.key = newroot
    def getLeftChild(self):
         return self.leftChild
    def getRightChild(self):
        return self.rightChild
    """
    前序遍历树：
    - 深度优先
    - 递归遍历

    """
    def preorder(self):
        print(self.key)
        if self.leftChild:
            self.leftChild.preorder()
        if self.rightChild:
            self.rightChild.preorder()
    def postorder(self):
        if self.leftChild:
            self.leftChild.postorder()
        if self.rightChild:
            self.rightChild.postorder()
        print(self.key)
"""
前序遍历
"""
def preorder(tree):
    if tree:
        print(tree.getRootValue())
        preorder(tree.getLeftChild())
        preorder(tree.getRightChild())
"""
后序遍历：
- 
"""
def postorder(tree):
    if tree !=None:
        postorder(tree.getLeftChild())
        postorder(tree.getRightChild())
        print(tree.getRootValue())

"""
中序遍历：
- 
"""
def inorder(tree):
    if tree !=None:
        postorder(tree.getLeftChild())
        print(tree.getRootValue())
        postorder(tree.getRightChild())
       


if __name__ == '__main__':
    r= BinaryTree('1')
    r.insertLeftChild('4')
    r.insertRighChild('5')
    r.insertLeftChild('2')
    r.insertRighChild('3')
    r.preorder()

    preorder(r)
    postorder(r)
    inorder(r)

    