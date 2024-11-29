def frequency(sentence):
    words = sentence.lower().split()
    
    wordFrequency = {
        
    }
    
    for word in words:
        if word in wordFrequency:
            wordFrequency[word]+=1
        else:
            wordFrequency[word] = 1
    return wordFrequency

sentence = input()
print(frequency(sentence))