def test(sln, haystack, needle, target):
    out = sln.strStr(haystack, needle)
    print('haystack = %s, needle = %s, out = %d' % (haystack, needle, out))
    assert out == target
    
def run(sln):
    test(sln, "hello", "ll", 2)
    test(sln, "aaaaa", "bba", -1)
    test(sln, "", "", 0)