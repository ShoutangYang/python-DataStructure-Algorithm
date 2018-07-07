class Solution(object):
    """[summary]
    
    Arguments:
        object {[type]} -- [description]
    """
    def Find(self, target, array):
           
        rows = len(array)
        cols = len(array[0])
        if rows>0 and cols>0:
            row=0
            col = cols-1
            while row<rows and col>=0:
                if target==array[row][col]:
                    return True
                if target>array[row][col]:
                    row = row+1
                if target<array[row][col]:
                    col =col-1
        return False   

if __name__ == '__main__':
    data = [[1,2,8,9],[2,4,9,12],[4,7,10,13],[6,8,11,15]]
    solution = Solution()
    print(solution.Find(7,data))

