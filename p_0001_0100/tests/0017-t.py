import pdb

def test(sln, digits, answer):
    print('digits = %s, answer = %s' % (digits, answer))
    out = sln.letterCombinations(digits)
    print('out = %s' % out)
    assert out == answer, out

def run(sln):
    test(sln, "23", ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"])
    test(sln, "", [])
    test(sln, "2", ["a", "b", "c"])
