print( 1.0*3 - 3.0 ) # 0
print( 0.5*3 - 1.5 ) # 0

# 1아래로 값이 떨어지면 정확한 계산이 되지 않는다.
print( 0.3*3 - 0.9 ) # -1.1102230246251565e-16 

# Decimal 이용
from decimal import Decimal as D
print( D('0.3') * D('3') - D('0.9') )

# 아니면 LIMITED_MIN을 잡고 이와 비교해도 될듯
LIMITED_MIN = 1e-10

print( (0.3*3 - 0.9) < LIMITED_MIN ) # True
