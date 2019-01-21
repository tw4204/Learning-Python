people = [('James', 17), ('Kirk', 9), ('Lars', 13), ('Robert', 8)]
for person, age in people:
    if age >= 18:
        driver = (person, age)
        break

# for문 또는 while문 밑의 else는 flag 역할을 해준다.
# 즉 loop문이 정상적으로 끝나면, else문으로 들어가지 않는다.
# flag 관련해서 유용하게 쓰일듯.
else:
    print('Driver not found.')
