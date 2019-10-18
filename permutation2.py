def permutations(string):
    if len(string) == 1:
        return set(string)
    first = string[0]
    rest = permutations(string[1:])

    result = set()
    for i in range(0, len(string)):
        for p in rest:
            result.add(p[0:i] + first + p[i:])
    return result


# print(sorted(permutations('a')))  # ['a']);
# print(sorted(permutations('ab')))  # ['ab', 'ba'])
print(sorted(permutations('aabb')))  # ['aabb', 'abab', 'abba', 'baab', 'baba', 'bbaa'])
