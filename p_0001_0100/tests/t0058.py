def test(sln, s, answer):
    print('s = %s, answer = %d' % (s, answer))

    out = sln.lengthOfLastWord(s)
    assert out == answer, out

def run(sln):        
    test(sln, "Hello World", 5)
    test(sln, " ", 0)
    test(sln, "a ", 1)
    test(sln, "a  ", 1)
    test(sln, "a  aa ", 2)
    test(sln, "Today is a nice day", 3)