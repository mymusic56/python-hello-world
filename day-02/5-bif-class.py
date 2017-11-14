"""
和类相关的内置函数（BIF）
isinstance hasattr setattr getattr delattr

isinstance issubclass

property

"""

class A:
	def setXy(self,x,y):
		self.x = x
		self.y = y

a = A()
print(A.__dict__)
print(a.__dict__)

a.setXy(1,2)
print(A.__dict__)
print(a.__dict__)

print('-----------------------------------')

print(isinstance(a,A))
print(hasattr(a,'x'))
print(hasattr(a,'c'))

setattr(a,'c','4')
print(hasattr(a,'c'), a.__dict__)
print(getattr(a,'c'))

delattr(a,'c')
print(hasattr(a,'c'), a.__dict__)

print('-------设置属性，然后删除属性--------')
setattr(a,'c','4')
print(hasattr(a,'c'), a.__dict__)
del a.c
print(hasattr(a,'c'), a.__dict__)
print('-----------------------------------')
class B(A):
    pass

print('B是否是A的子类:', issubclass(B,A))

print('B是否是objec子类:',issubclass(B,object))
print('B是否是自己的子类:',issubclass(B,B))
"""
property
"""


class D(object):
    def getx(self): return self._x

    def setx(self, value): self._x = value

    def delx(self): del self._x

    x = property(getx, setx, delx, "I'm the 'x' property.")

print('------------------------property--------------------------')
d = D()
print(hasattr(d,'x'))
d.x = 15
print(hasattr(d,'x'), d.x)

del d.x
print(hasattr(d,'x'))
