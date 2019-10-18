def permutations(string):
    if len(string) == 1:
        return string if isinstance(string, list) else [string]

    result = []
    for i in range(len(string)):
        first = string[i]
        rest = string[:i] + string[i + 1:]
        next_permutation = permutations(rest)
        for p in next_permutation:
            result.append(first + p)
    return list(dict.fromkeys(result))


print(sorted(permutations('a')))  # ['a']);
print(sorted(permutations('ab')))  # ['ab', 'ba'])
print(sorted(permutations('aabb')))  # ['aabb', 'abab', 'abba', 'baab', 'baba', 'bbaa'])
