# https://www.codewars.com/kata/5390bac347d09b7da40006f6/train/python
def to_jaden_case(string):
    words = string.split()
    result = []
    for word in words:
        result.append(word.capitalize())
    return ' '.join(result)

# solution by others
# def to_jaden_case(string):
#    return ' '.join(word.capitalize() for word in string.split())

print(to_jaden_case("how can Mirrors Be Real If Our Eyes Aren't Real"))
