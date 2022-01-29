# https://www.hackerrank.com/challenges/compress-the-string?isFullScreen=true
# I've stumble upon the solution (https://stackoverflow.com/a/63385302/12075722) while searching for itertools groupby examples
# Obviously I haven't submitted this solution to hackerrank
import itertools

s = '1222311'

def compress(string):
    for key, group in itertools.groupby(string):
        yield len(tuple(group)), int(key)

print(*compress(s))