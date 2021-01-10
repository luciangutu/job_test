"""
script to calculate how many years it will take to reach a better salary
s1 - current (lower) salary
s2 - future/wanted/promissed salary
i1 - yearly salary increase for the current salary
i2 - yearly salary increase at the other company that you are thinking of going
"""

s1 = 500
s2 = 800
i1 = 5
i2 = 2


########################
# percent calculator
########################
def compute(s, i):
    return s*i/100

sal1 = s1
sal2 = s2
x_test = False

for x in range(50):
    sal1 += compute(sal1, i1)
    sal2 += compute(sal2, i2)
    if sal1 >= s2 and not x_test:
        x1 = x
        x_test = True
    if sal1 >= sal2:
        print("Your current salary is {}. It will take {} years in order to reach the same aimed salary {}. Good luck!". format(s1, x1, s2))
        print("After {} years, you will have the same salary. Your current employee will pay you {} and the one that you aim for will pay you {}.". format(x, sal1, sal2))
        break
