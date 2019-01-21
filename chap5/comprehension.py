# dict comprehension 
word = 'Hello'
swaps = {c: c.swapcase() for c in word}
print(swaps)


# set comprehension
word = 'Hello'
unique_letter = {c for c in word}
print(unique_letter)
