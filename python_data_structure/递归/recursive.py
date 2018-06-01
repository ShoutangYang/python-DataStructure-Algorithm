"""
递归的定律：

- 停止递归算法的条件
- 每一次递归能接近基本情况
- 以递归方式调用自身

"""


"""
"""
def listSum(list):
    """
    停止的条件，数据长度
    """
    if len(list)==1:
        return list[0]
    else:
        """
        - 数据在减少
        - 调用自身
        """
        return list[0]+listSum(list[1:])

if __name__ == '__main__':
    list = [1,2,3,4,5,7,8,8]
    print(listSum(list))
    