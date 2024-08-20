# https://www.codewars.com/kata/515e271a311df0350d00000f/train/python



def square_sum(numbers):
    return sum([n**2 for n in numbers])

assert square_sum([1, 2, 2]) == 9, '%s != %s' % (
    square_sum([1, 2, 2]), 9)