def test(sln, strs, target):
    out = sln.longestCommonPrefix(strs)
    print('strs = %s, out = %s' % (strs, out))
    #pdb.set_trace()
    assert out == target

def run(sln):
    test(sln, ["ab", "a"], "a")
    test(sln, ["", "b"], "")
    test(sln, ["flower", "flow", "flight"], "fl")
    test(sln, ["dog", "racecar", "car"], "")