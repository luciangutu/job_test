# https://www.codewars.com/kata/54ba84be607a92aa900000f1/train/python
# using Two Pointer pattern
def is_isogram(string):
    temp_tuple = ()

    for c in string:
        if c.lower() in temp_tuple:
            return False
        temp_tuple = temp_tuple + tuple(c.lower())
    # shorter answer:
    # return len(string) == len(set(string.lower()))
    # explanation:
    # len(string) == len(set(string.lower()))
    # compares the length of the original string with the length of the set.If these lengths are equal,
    # it means there were no duplicate characters (i.e., the string is an isogram).If not, there were duplicates.
    return True

assert is_isogram("Dermatoglyphics") == True, '%s != %s' % (
    is_isogram("Dermatoglyphics"), True)

assert is_isogram("aba") == False, '%s != %s' % (
    is_isogram("aba"), False)

assert is_isogram("moOse") == False, '%s != %s' % (
    is_isogram("moOse"), False)