# https://www.codewars.com/kata/56747fd5cb988479af000028/train/python


def get_middle(s):
    chars = [*s]
    middle_pos = int(len(chars)/2)
    if len(chars) % 2 == 0:
        middle = chars[middle_pos - 1] + chars[middle_pos]
    else:
        middle = chars[middle_pos]
    return middle


# solution by others
# def get_middle(s):
#     index, odd = divmod(len(s), 2)
#     return s[index] if odd else s[index - 1:index + 1]
#
#
# def get_middle(s):
#     i = (len(s) - 1) // 2
#     return s[i:-i] or s
#
# def get_middle(s):
#     return s[(len(s)-1)//2:len(s)//2+1]




print(get_middle("test"))
print(get_middle("testing"))
print(get_middle("middle"))
