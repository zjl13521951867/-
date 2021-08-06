# 1：__getattr__(self,attr) 只有在没有找到属性的情况下，才调用__getattr__


class Fib(object):
    def __init__(self):
        self.a, self.b = 0, 1  # 初始化两个计数器a，b

    def __iter__(self):
        return self  # 实例本身就是迭代对象，故返回自己

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b  # 计算下一个值
        if self.a > 100000:  # 退出循环的条件
            raise StopIteration()
        return self.a  # 返回下一个值
# for n in Fib():
#   print(n)



class Student(object):
    def __init__(self,name,score):
        self._name = name 
        self._score = score 
        print('当前',hasattr(self,'233'))

    @property
    def name(self):
        return self._name 

    def __getattr__(self,attr):
        if(attr == 'address'):
            return self._address
        else:
            return '暂无此项'

s1 = Student('张三',20)
print(s1.name)    


class Chain(object):
    def __init__(self, path=''):
        self._path = path
    # 这里的path属性就是attr，
    def __getattr__(self, path):
        print('lujing',path)
        return Chain('%s/%s' % (self._path, path))
    def __str__(self):
        return self._path
    __repr__ = __str__
'''
  1：读取不到status，所以调用个__getattr__属性，返回Chain(self,'/status')
  2：步骤1返回的就是Chain的实例，继续调用 实例.user => 依旧读取不到该属性，此时的path='/status/user'
  3：重复上面的操作，读取到最后一个list属性还是没有，path='/status.user.timeline.list'
'''
Chain().status
print(Chain().status.user.timeline.list)