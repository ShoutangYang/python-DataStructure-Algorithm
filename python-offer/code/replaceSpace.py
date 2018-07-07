
"""
 题目：请实现一个函数，将一个字符串中的空格替换成“%20”。

 方法1：
    使用内置函数 replace

 方法2;
    使用正则表达式


"""
import re


def replaceSpace(s):
    s.replace(' ','%20')
    return s

def replaceSpaceRe(s):
    
    return re.sub(' ','%20',s)

if __name__ == '__main__':
    
    # print( replaceSpace('We Are Happy'))
    
    print(replaceSpaceRe('   we are '))