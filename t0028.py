def test(sln, haystack, needle, answer):
    print('haystack = %s, needle = %s, answer = %d' % (haystack, needle, answer))
    out = sln.strStr(haystack, needle)
    assert out == answer, out
    
def run(sln):
    test(sln, "hello", "ll", 2)
    test(sln, "aaaaa", "bba", -1)
    test(sln, "", "", 0)