# https://www.codewars.com/kata/555086d53eac039a2a000083/python

def lovefunc(flower1, flower2):
    if (flower1 % 2 == 0 and flower2 % 2 != 0) or (flower1 % 2 != 0 and flower2 % 2 == 0):
        return True
    else:
        return False


# other solutions
# def lovefunc( flower1, flower2 ):
#     return (flower1+flower2)%2

# def lovefunc(flower1, flower2):
#     return flower1 % 2 != flower2 % 2

def basic_test_cases():
    assert lovefunc(1, 4)
    assert not lovefunc(2, 2)
    assert lovefunc(0, 1)
    assert not lovefunc(0, 0)


basic_test_cases()