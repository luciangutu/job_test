def multiply(a, b, *argv):
    all = (a, b) + argv
    return all

print(multiply("a", 2, "c", 4, "d"))
