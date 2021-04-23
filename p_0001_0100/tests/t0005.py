#
# 4/10: 4 mins
#

def test(sln, s, target):
    out = sln.longestPalindrome(s)
    print('s = %s, out = %s' % (s, out))    
    assert out == target, target
    print('')

def run(sln):
    test(sln, 'babad', 'bab')
    test(sln, 'cbbd', 'bb')    
    test(sln, 'a', 'a')    
    test(sln, 'ac', 'a')   
    test(sln, 'ccc', 'ccc')
    test(sln, 'aaaa', 'aaaa')
