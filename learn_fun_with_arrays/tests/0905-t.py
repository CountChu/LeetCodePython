import pdb

def test(sln, A, answer):
    print('A = %s, answer = %s' % (A, answer))
    out = sln.sortArrayByParity(A)
    assert out == answer, out

def run(sln):
    test(sln, [3,1,2,4], [2,4,3,1])
