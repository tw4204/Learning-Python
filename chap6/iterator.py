class OddEven:
    def __init__(self, data):
        self._data = data
        self.indexes = (list(range(0, len(data), 2)) + list(range(1, len(data), 2)))
    def __iter__(self):
        return self
    def __next__(self):
        if self.indexes:
            return self._data[self.indexes.pop(0)]
        raise StopIteration
oddeven = OddEven('ThIsIsCoOl!')
print(''.join(c for c in oddeven)) # TIICO!hssol


# Class의 iter를 새로 정의해서 iteration을 돌릴 수 있다.
