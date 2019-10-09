def narcissistic( value ):
    mylist = str(value)
    r = 0
    c = 0
    for i in mylist:
        if i.isdigit():
            c = int(i)**len(mylist)
        r += c
    return True if r == value else False

print(narcissistic(7))
print(narcissistic(371))
