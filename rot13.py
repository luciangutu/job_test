def rot13(message):
    inputstr = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    output = "NOPQRSTUVWXYZABCDEFGHIJKLMnopqrstuvwxyzabcdefghijklm"

    result = str()

    for i in range(len(message)):
        if message[i] not in inputstr:
            result += message[i]
        else:
            x = inputstr.index(message[i])
            result += output[x]
    return result


print(rot13("EBG13 rknzcyr."))  # == "ROT13 example.")
