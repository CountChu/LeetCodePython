def test(sln, s, target):
    out = sln.lengthOfLastWord(s)
    print('s = %s, out = %d' % (s, out))
    assert out == target

def run(sln):        
    test(sln, "Hello World", 5)
    test(sln, " ", 0)
    test(sln, "a ", 1)
    test(sln, "a  ", 1)
    test(sln, "a  aa ", 2)