class ExitLoopException(Exception):
    pass
try:
    n = 100
    for a in range(n):
        for b in range(n):
            for c in range(n):
                if 42 * a + 17 * b + c == 5096:
                    raise ExitLoopException(a, b, c)
except ExitLoopException as ele:
    print(ele) # (79, 99, 95)

# flag를 사용하지 않고 이렇게 할 수 있다.
