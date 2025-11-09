def word_frequency(text): #write a function that determines the frequency of words used in a sentence
    freq = {}
    words = text.lower().split()

    for w in words:
        if w in freq:
            freq[w] += 1
        else: 
            freq[w] = 1
    return freq

print(word_frequency("hello hello world this is world world"))