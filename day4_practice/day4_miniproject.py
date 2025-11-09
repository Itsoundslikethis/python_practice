with open("day4_sampletext.txt", "r") as f: #read the text file day4_sampletext.txt"
    data = f.read()

def remove_vowels(text):  #function designed to remove vowels from the sentence
    vowels = "aeiouAEIOU"
    result = ""
    for char in text:
        if char not in vowels:
            result += char
    return result

cleaned = remove_vowels(data) #establish variable cleaned as the returned result from remove_vowels function

with open("cleaned_text.txt", "w") as f: #write to a new text file cleaned_text.txt with the returned result w/ vowels removed
    f.write(cleaned)

print("File cleaned and saved!")