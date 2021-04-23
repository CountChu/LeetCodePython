#
# 2021/4/3: 11 mins
#

def test(sln, s, target):
    out = sln.myAtoi(s)
    print('s = %s, out = %d' % (s, out))
    assert out == target

def run(sln):
    test(sln, '42', 42)
    test(sln, '  -42', -42)
    test(sln, '4193 with words', 4193)
    test(sln, 'words and 987', 0)
    test(sln, '-91283472332', -2147483648)
    test(sln, '00000-42a1234', 0)
    test(sln, '   +0 123', 0)
    