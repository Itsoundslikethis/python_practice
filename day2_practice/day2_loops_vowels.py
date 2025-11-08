def count_vowels(sentence): #function designed to count vowels in a sentence
    vowels = "aeiou"
    count = 0
    for char in sentence.lower():
        if char in vowels:
            count += 1
    return count

print(count_vowels("Hello World"))
print(count_vowels("How many vowels are in this sentence?"))