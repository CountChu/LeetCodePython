#
# I spent 3 mins to write test() and the framework.
#

def test(sln, s, target):
    out = sln.lengthOfLongestSubstring(s)
    print('s = %s, out = %d' % (s, out))
    assert out == target
    print('')

def run(sln):
    test(sln, 'abcabcbb', 3)
    test(sln, 'bbbbb', 1)
    test(sln, 'pwwkew', 3)
    test(sln, '', 0)
    test(sln, ' ', 1)
    test(sln, 'au', 2)
    test(sln, 'dvdf', 3)
    test(sln, 'nfpdmpi', 5)

