
def longest_word(data):
    string_split = data.split()
    longest_string = ""
    for word in string_split:
        if len(word) > len(longest_string):
            longest_string = word
            longest_string
    return longest_string

with open("day5_sampletext.txt", "r") as f:
        data = f.read()
    
result = longest_word(data)

print('The longest word is: ' + result + " (length: " + str(len(result)) + ")")

