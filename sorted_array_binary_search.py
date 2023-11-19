array = ["a", "b", "c", "d", "e", "f", "g"]

def find_me_brute_enum(_array, f):
    for k,v in enumerate(_array):
        if v == f:
            return f, k
    return None

def find_me_brute(_array, f):
    for i in range(len(_array)):
        if _array[i] == f:
            return f, i
    return None


def find_me_smart(_array, f, start_index=0):
    # we are splitting the sorted array and check if the letter is before, after or equal with the middle index, in the alphabet
    # if is not equal, the run the function recursive
    half_index = len(_array) // 2
    current_index = start_index + half_index

    if f == _array[half_index]:
        return f, current_index
    elif f < _array[half_index]:
        return find_me_smart(_array[:half_index], f, start_index)
    elif f > _array[half_index]:
        return find_me_smart(_array[half_index + 1:], f, current_index + 1)
    return None


search_char = "b"

print(find_me_brute_enum(array, search_char)) if find_me_brute_enum(array, search_char) is not None else print(f"{search_char} not found in the array.")
print(find_me_brute(array, search_char)) if find_me_brute(array, search_char) is not None else print(f"{search_char} not found in the array.")
print(find_me_smart(array, search_char)) if find_me_smart(array, search_char) is not None else print(f"{search_char} not found in the array.")