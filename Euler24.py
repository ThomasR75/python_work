# Euler 24
# what is the millionth lexicographic permutation of 0 to 9

from itertools import permutations
perm = list(permutations(range(0, 10)))
l = perm[999999]
print(l)

