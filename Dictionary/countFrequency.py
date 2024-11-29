def countFrequency(sentence):
    wordFrequency = {}
    sentence = sentence.lower()
    words = sentence.split()
    
    for word in words:
        if word in wordFrequency:
            wordFrequency[word]+= 1
        else:
            wordFrequency[word] = 1
    return wordFrequency
# end def


sentence = "lambda  rangesad asciiwhile, cherry ascii(object : set a = ('b', 'g', 'a', 'd', 'f', 'c', 'h', 'e')"


    # comment: 
# end while), ExclusiveEnd): expression"

print(countFrequency(sentence))