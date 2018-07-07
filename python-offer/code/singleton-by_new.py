'''
单例模式：
    - 此类有且只有一个实例，
    - 实例是自己创造
    - 系统中使用到的都是这个实例

方法1: 使用 __new__
    联想：__new__ 和 __init__ 的区别：
    1._new__ :创建实例
    2.__init__ ：初始化实例

知识点1：
    cls 和 self 的区别:
     cls 作为第一个参数表示类本身，在类方法中调用，跟实例无关。
     self:表示实例本身，
知识点2：
    *args 和 **kwargs
     - *args 可以传递任意数量的参数
     **kwargs 可以和使用灭有事先定义的参数名
知识点3：
     super : 
        调用父类的方法


'''

"""[singleton]
- 使用__new__来控制实例的创建过程
- _instance 为类的私有变量
- _instance 为空，则创建实例，否则直接返回 cls._instance


"""
class Singleton(object):
    """[summary]
    
    Arguments:
        object {[type]} -- [description]
    """
    """
    定义一个类 私有变量
    """
    _instance =None

    def __new__(cls,*args,**kwargs):
        """
        
        """
        if  not cls._instance:
            cls._instance = super(Singleton,cls).__new__(cls,**kwargs)
            
        return cls._instance
        
       
class myClass(Singleton):
    value = 22

    def __init__(self, val):
        self.value  = val
    
    def obj_fun(self):
        print(("{0} {1}").format(self.value,'obj_fun'))
    
    @staticmethod
    def static_fun(self):
        print('static function')
    @classmethod
    def class_fun(self):
        print('{0} {1}'.format(self.value, 'class method'))


if __name__ == '__main__':
    a = myClass(1)
    b = myClass(2)

    print(a is b)
    print("ID:{0} ID:{1} ".format(id(a),id(b)))
    print(type(a))
    print(type(b))
    print(type(Singleton))
    print(type(type))
    a.obj_fun()
    b.class_fun()
    print(a.value)
    print(b.value)


