# https://www.codewars.com/kata/57cebe1dc6fdc20c57000ac9/train/python

def find_short(s):
    n = s.split()
    m = sorted([ len(x) for x in n ])
    return list(m)[0]
# best: return min(len(x) for x in s.split())

assert find_short("bitcoin take over the world maybe who knows perhaps") == 3, '%s != %s' % (
    find_short("bitcoin take over the world maybe who knows perhaps"), 3)

assert find_short("BTC Steem LiteCoin") == 3, '%s != %s' % (
    find_short("BTC Steem LiteCoin"), 3)