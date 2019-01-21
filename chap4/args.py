def func(*args):
    for a in args:
        print (a)

# List도 되고 tuple도 된다.

#values = (1, 3, -7, 9)
values = [1, 3, -7, 9]
func(*values)
