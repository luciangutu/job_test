def int32_to_ip(int32):
    o1 = int(int32 / 16777216) % 256
    o2 = int(int32 / 65536) % 256
    o3 = int(int32 / 256) % 256
    o4 = int(int32) % 256
    return '{}.{}.{}.{}'.format(o1, o2, o3, o4)
    # or return '%(o1)s.%(o2)s.%(o3)s.%(o4)s' % locals()

print('2149583361 -> %s' % int32_to_ip(2149583361))
