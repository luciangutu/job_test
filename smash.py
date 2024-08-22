# https://www.codewars.com/kata/53dc23c68a0c93699800041d/train/python

def smash(words):
    return ' '.join(words)


assert smash(['hello', 'world', 'this', 'is', 'great']) == 'hello world this is great', '%s != %s' % (
    smash(['hello', 'world', 'this', 'is', 'great']), 'hello world this is great')