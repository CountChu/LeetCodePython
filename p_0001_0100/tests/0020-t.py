def test(sln, s, target):
    out = sln.isValid(s)
    print('s = %s, out = %s' % (s, out))
    assert out == target

def run(sln):
    test(sln, "]", False)    
    test(sln, "[", False)
    test(sln, "()", True)
    test(sln, "()[]{}", True)
    test(sln, "(]", False)
    test(sln, "([)]", False)
    test(sln, "{[]}", True)