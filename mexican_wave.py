def wave(str):
    mylist = []
    for c in range(len(str)):
        if str[c] == ' ':
            continue
        else:
            mylist.append(str[:c].lower() + str[c:].capitalize())
    return mylist


print(wave('go gu'))

print(wave('mexican'))