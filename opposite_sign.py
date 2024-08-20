# https://www.codewars.com/kata/56dec885c54a926dcd001095/train/python

def opposite(number):
  return -abs(number) if number > 0 else abs(number)

# best solution:
# def opposite(number):
#     return -number

assert opposite(1) == -1, '%s != %s' % (
    opposite(1), -1)

assert opposite(3.1458) == -3.1458, '%s != %s' % (
    opposite(3.1458), -3.1458)

assert opposite(-3.1458) == 3.1458, '%s != %s' % (
    opposite(-3.1458), 3.1458)