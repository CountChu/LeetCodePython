import pdb

def test(sln, n, answer):
    print('n = %s, answer = %s' % (n, answer))
    out = sln.generateParenthesis(n)
    assert out == answer, out

def run(sln):
    test(sln, 3, ['()()()', '(())()', '()(())', '(()())', '((()))'])
    test(sln, 1, ["()"])
    test(sln, 2, ["()()", "(())"])
