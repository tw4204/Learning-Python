from itertools import compress
data = range(10)
even_selector = [1, 0] * 10
odd_selector = [0, 1] * 10

even_numbers = list(compress(data, even_selector))
odd_numbers = list(compress(data, odd_selector))

print(even_numbers)     #[0, 2, 4, 6, 8]
print(odd_numbers)      #[1, 3, 5, 7, 9]

# 리스트에 들어있는 data를 masking할때 좋을 것 같다.
