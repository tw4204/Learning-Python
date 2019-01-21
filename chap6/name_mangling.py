#factor_name = '_factor'
factor_name = '__factor'

class A:
    def __init__(self, factor):
        setattr(self,factor_name, factor)
    def op1(self):
        print('Op1 with factor {}...'.format(getattr(self,factor_name)))
class B(A):
    def op2(self, factor):
        setattr(self,factor_name, factor)
        print('Op2 with factor {}...'.format(getattr(self,factor_name)))

obj = B(100)
obj.op1() # Op1 with factor 100...
obj.op2(42) # Op2 with factor 42...
obj.op1() # Op1 with factor 100...

if factor_name == '_factor':
    print(obj.__dict__.keys())
    # dict_keys(['_factor'])
else:
    print(obj.__dict__.keys())
    # dict_keys(['_A__factor', '_B__factor'])

# setattr는 해당사항이 없는듯.
