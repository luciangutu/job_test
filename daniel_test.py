"""
Job interview test

Having a random list: strings = ['gigi', 'duru', 'ionel', 'florescu', 'popovici', 'restaurant', 'ovidiu'] Get the number of 3 char groups from it: { "tau": 1, "ran": 1, "res": 2, "pop": 1, "gig": 1, "ion": 1, "flo": 1, "diu": 1, "dur": 1, "ovi": 2 }
"""
import json
strings = ['gigi', 'duru', 'ionel', 'florescu', 'popovici', 'restaurant', 'ovidiu']
result = []
for string in strings:
    str_len = len(string)
    if str_len > 2:
        # counts = str_len / 3
        for count in range(0,str_len,3):
            str_res = string[count:count+3]
            if len(str_res) > 2:
                result.append(str_res)
d = {x:result.count(x) for x in result}
print(json.dumps(d, indent=2))
