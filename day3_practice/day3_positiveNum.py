def get_positives(numbers):
    positives = []
    for n in numbers:
        if n > 0:
            positives.append(n)
    return positives
    
print(get_positives([-3, -1, 0, 1, 5]))