def removeDuplicate(num):
    seen = set()
    result = []
    for item in num:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result   
    
num = [1, 2, 3, 4, 5, 5, 4, 6, 5, 4, 3, 5, 2, 3, 4, 2, 3, 4, 1, 2, 1, 2,3, 4, 3, 4, 3, 3, 4, 1, 5,4,3, 3, 4, 1, 2, 3, 4 , 1, 4, 1, 4, 1, 2, 3, 5, 3]

print(removeDuplicate(num))