#design a function with a for loop that determines if a number is even or odd
def even_or_odd(numbers):
    for n in numbers:
        if n % 2 == 0:
            print(str(n) + " is even")
        else:
            print(str(n) + " is odd")

even_or_odd([1,2,3,4,5,6,7,8,9])