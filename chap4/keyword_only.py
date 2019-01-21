def kwo(a, b=2 , *, c):
    print (a,b,c)

# variable positional argument뒤에 변수(c)는 키워드를 지정해야한다.
kwo(1,2,c=3)

# kwo(1,2,3)  <- error
