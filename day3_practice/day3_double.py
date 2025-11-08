def double_numbers(numbers): #create a function that takes an array of numbers and doubles each number in the array, the returns a new array with the doubled numbers
    doubled = []
    for n in numbers:
        doubled.append(n * 2)
    return doubled

print(double_numbers([1,2,3,4]))