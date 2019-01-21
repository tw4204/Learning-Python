from collections import defaultdict

# 초기화할때 정말 좋을 것 같다.
# count를 셀때, object안에 list를 보관할 때, ...
dd = defaultdict(list)
for i in range(10):
    dd['a'].append(i) 
print (dd['a'])
