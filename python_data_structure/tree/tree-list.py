"""
二叉树节点
"""
def BinaryTree(root):
    return [root,[],[]]
"""
插入左节点
"""
def insertLeft(root,newBranch):
    t = root.pop(1)
    if len(r)>1:
        root.insert(1,[newBranch,t,[]])
    else:
        root.insert(1,[newBranch,[],[]])
    return root
"""
插入右节点

"""

def insertRight(root,newBranch):
    t=root.pop(2)
    if len(t)>1:
        root.insert(2,[newBranch,[],t])
    else:
        root.insert(2,[newBranch,[],[]])
    return root

def getRootValue(root):
    return root[0]
def setRootValue(root,newroot):
    root[0]=newroot
def getLeftChild(root):
    return root[1]
def getRightChild(root):
    return root[2]


if __name__ == '__main__':
    
    