import pdb

def test(sln, arr, answer):
    print('arr = %s, answer = %s' % (arr, answer))
    sln.duplicateZeros(arr)
    assert arr == answer, arr

def run(sln):
    test(sln, [0,0,0,0,0,0,0], [0,0,0,0,0,0,0])
    test(sln, [1,0,2,3,0,4,5,0], [1,0,0,2,3,0,0,4])
    test(sln, [1,2,3], [1,2,3])
