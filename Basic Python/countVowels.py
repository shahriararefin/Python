def countVowels(s):
    vowels = "aeiouAEIOU"
    count = 0
    for char in s:
        if char in vowels:
            count+=1
    return count
sentence = input()
print(countVowels(sentence))

