def get_squares_gen(n):
    for x in range(n):
        yield x ** 2
squares = get_squares_gen(4) # this creates a generator object
print(squares) # <generator object get_squares_gen at 0x7f158...>
print(next(squares)) # prints: 0
print(next(squares)) # prints: 1
print(next(squares)) # prints: 4
print(next(squares)) # prints: 9
# the following raises StopIteration, the generator is exhausted,
# any further call to next will keep raising StopIteration

# print(next(squares))

# 쓸일이 있을까?

# set comprehension에 왜 ()을 안쓴지 알겠다.
cubes_gen = (k**3 for k in range(10))

print(list(cubes_gen))

print(list(cubes_gen))


s = sum([n**2 for n in range(10**8)]) # this is killed
# s = sum(n**2 for n in range(10**8)) # this succeeds
print(s)

# 쓸일이 있구나..
