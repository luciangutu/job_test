import unittest

def disemvowel(string_):
    vowels = ["a", "e", "i", "o", "u"]
    char_list = list(string_)
    # better answer: return "".join(c for c in string if c.lower() not in "aeiou")
    return ''.join([x for x in char_list if x.lower() not in vowels])


assert disemvowel("This website is for losers LOL!") == "Ths wbst s fr lsrs LL!", '%s != %s' % (disemvowel("This website is for losers LOL!"), "Ths wbst s fr lsrs LL!")
