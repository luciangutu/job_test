# https://www.codewars.com/kata/54da5a58ea159efa38000836/train/python


def find_it(seq):
    count_dict = {}
    for e in seq:
        # better: count_dict[e] = count_dict.get(e, 0) + 1
        if e in count_dict:
            count_dict[e] += 1
        else:
            count_dict[e] = 1

    for k, v in count_dict.items():
        if v % 2 != 0:
            return k
    return None

# better answer in terms of readability:
# def find_it(seq):
#     for i in seq:
#         if seq.count(i)%2!=0:
#             return i



assert find_it([20,1,-1,2,-2,3,3,5,5,1,2,4,20,4,-1,-2,5]) == 5, '%s != %s' % (
    find_it([20,1,-1,2,-2,3,3,5,5,1,2,4,20,4,-1,-2,5]), 5)
