from itertools import combinations

def uniqueCombination(num):
    return list(combinations(num, 2))

num = [1, 2, 3, 4]
print(uniqueCombination(num))