def outer():
    test = 1 # outer scope
    def inner():
        # 딱히 쓸일은 없을듯?
        nonlocal test
        test = 2 # nearest enclosing scope
        print('inner:', test)
    inner()
    print('outer:', test)
test = 0 # global scope
outer()
print('global:', test)
