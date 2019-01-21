from collections import ChainMap

default_connection = {'host': 'localhost', 'port': 4567}

connection = {'port': 5678}
conn = ChainMap(connection, default_connection) # 새로운게 앞에 와야 한다.

# 다음과 같이 mapping history를 볼 수 있다.
print( conn.maps ) # [{'port': 5678}, {'host': 'localhost', 'port': 4567}]

# 한겹씩 바르는 느낌이다.

# update call이 많을 때, dict 보다 이걸 쓰면 더 좋다고 한다. ( 공간 복잡도는?)
# 업데이트 내역을 유지해야 하는 상황에서는 쓰기 좋을듯.
