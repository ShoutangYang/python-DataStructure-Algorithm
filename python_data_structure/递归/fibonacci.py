"""
    
"""
def fb(num):
    if num<=1:
        return 1
    else:
        return  fb(num-1)+fb(num-2)
 
def for_fb(num):
    arr=[0,1,1]
    for i in range(num):
        arr.append(arr[i+1]+arr[i+2])
    
    return arr



if __name__ == '__main__':
  
      print(for_fb(100))
      