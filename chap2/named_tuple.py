from collections import namedtuple
# immutable한 object형 같다.

Vision = namedtuple('vision' , ['l','r','avg'])
v = Vision(1.0,2.0,1.5)
print(type(v))

