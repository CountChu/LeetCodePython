import pdb

def test(sln, arr, answer):
    print('arr = %s, answer = %s' % (arr, answer))
    out = sln.replaceElements(arr)
    assert out == answer, out

def run(sln):
    test(sln, [17,18,5,4,6,1], [18,6,6,6,1,-1])
    test(sln, [400], [-1])
