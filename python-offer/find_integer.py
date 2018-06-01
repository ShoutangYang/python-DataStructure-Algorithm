"""
题目：
    二维数组中，每行从左到右递增，给出一个数，判断是否存在数组中

思路：
    从左下角或是右上角，开始比较
"""

def find_integer(matrix,num):
    """[summary]
    
    Arguments:
        matrix {[type]} -- [description]
        num {[type]} -- [description]
    """
    if not matrix:
        return False
    
    rows,cols = len(matrix),len(matrix[0])

    row,col = rows-1,0

    while row >=0 and col<=cols-1:
        if matrix[row][col] ==num:
            return True
        elif matrix[row][col]>num:
            row -=1
        else:
            col+=1
    return False


if __name__ == '__main__':
    
    martix = [[1,2,3,4,5,6],]
    