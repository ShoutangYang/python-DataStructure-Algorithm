def maopao(nums):
    for i in range( len(nums)):
        for j in range(len(nums)-i-1):
            if nums[j]>nums[j+1]:
                nums[j] ,nums[j+1]=nums[j+1],nums[j]
    return nums

"""
冒泡排序
"""
def maopao2(nums):
    for i in range(len(nums)-1,0,-1):
        print('i->',i)
        for j in range(i):
            if nums[j]>nums[j+1]:
                nums[j] ,nums[j+1]=nums[j+1],nums[j]
    return nums

"""
选择排序

"""
def selectMax(nums):
    for i in range(len(nums)):
        for j in range(len(nums)-i-1):
            if nums[j]>nums[j+1]:
                nums[j+1]=nums[j]
    
    return nums
"""
插入排序

"""
def insertSort(nums):
    for index in range(1,len(nums)):
        current=nums[i]
        position = index

        while position>0 and nums[position-1]>current:
            nums[position] = nums[position-1]
            position = position-1
        
        nums[position] current
        
            
    

if __name__ == '__main__':
    print(maopao([2,3,4,6,7,99,100,13,4,56]))
    print(maopao2([2,3,4,5,1,2,3,4,6]))

    print(selectMax([1,3,4,6,2,78,6,90,100]))