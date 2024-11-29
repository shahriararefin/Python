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


sentence = "sentence that i need to write is not the sentence i am going to write. bahahahahaha"


    # comment: 
# end while), ExclusiveEnd): expression"

print(countFrequency(sentence))