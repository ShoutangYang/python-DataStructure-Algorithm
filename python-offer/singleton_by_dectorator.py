"""

 singleton :
    - 只有一个实例
    - 新建实例的时候判断

"""
from functools import wraps


def singleton(cls):
    """[summary]
    装饰器：
        - 返回内部函数 getinstance
        - 判断该函数是否在字典中，不在则实例化，有则直接返回函数
        - 
    Returns:
        [type] -- [description]
    """
    _instance = {}
    @wraps(cls)
    def getinstance(*args,**kwargs):
        if cls not in _instance:
            _instance[cls] = cls(*args,**kwargs)
        return _instance[cls]
    
    return getinstance


@singleton
class myclass(object):
    
    def __init__(self, val):
        self.a = val
   

if __name__ == '__main__':
    a = myclass(10)
    b = myclass(2)

    print(a is b)

    print(type(a))
    print(type(b))

    print(a.a)
    print(b.a)

    