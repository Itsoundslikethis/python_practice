def get_double_positive(numbers):
    doubled_positve = []
    for n in numbers:
        if n > 0:
            doubled_positve.append(n * 2)
    return doubled_positve

print(get_double_positive([-1,-2,-3,0,2,3,4]))

