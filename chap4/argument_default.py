# mutable type을 argument의 default값으로 쓰면 안된다.
def func(a=[], b={}):
    print(a)
    print(b)
    print('#' * 12)
    a.append(len(a)) # this will affect a's default value
    b[len(a)] = len(a) # and this will affect b's one


# 함수의 __defaults__에 값이 저장된다.
func()
print (func.__defaults__)
func()
print (func.__defaults__)
func()
print (func.__defaults__)
