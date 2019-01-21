from math import sqrt
mx = 10
# filter
legs = [(a, b, sqrt(a**2 + b**2)) for a in range(1, mx) for b in range(a, mx)]
# refine
legs = [(a, b, int(c)) for a, b, c in legs if c.is_integer()]

print(legs) # prints: [(3, 4, 5), (6, 8, 10)]

#이 방법이 가장 깔끔한듯
