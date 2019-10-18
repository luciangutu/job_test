def make_readable(seconds):
    a = b = 0
    c = seconds
    while c > 59:
        b += 1
        c = c - 60
    while b > 59:
        a += 1
        b = b - 60
    x = [str(a).zfill(2), str(b).zfill(2), str(c).zfill(2)]
    return ':'.join(x)


print(make_readable(0))  # "00:00:00")
print(make_readable(5))  # "00:00:05")
print(make_readable(60))  # "00:01:00")
print(make_readable(86399))  # "23:59:59")
print(make_readable(359999))  # "99:59:59")
