#
# 2021/4/3: 3 mins.
#

def test(sln, s, p, target):
    print('s = %s, p = %s' % (s, p))
    out = sln.isMatch(s, p)
    print('out = %s' % (out))
    assert out == target  
    print('')

def run(sln):

    if True:
        test(sln, 'aa', 'aaa', False)
        test(sln, 'aaa', 'aaaa', False)
        test(sln, 'aaa', 'baa', False)
        test(sln, 'abb', 'acb', False)
        test(sln, 'aa', 'ab', False)
        test(sln, 'aa', 'a', False)
        test(sln, 'aa', 'aa', True)
        
    if True:
        test(sln, 'aaa', 'a.a', True)
        test(sln, 'aaa', 'b.a', False)
        test(sln, 'ab', '...', False)

    if True:
        test(sln, 'aaa', 'a*a', True)   
        test(sln, 'abcd', 'd*', False)
        test(sln, 'aaa', 'ba*a', False)
        test(sln, 'aab', 'c*a*b', True)
        test(sln, 'aaa', 'aa*a', True)
        test(sln, 'abc', 'ba*a', False)
        test(sln, 'abc', 'aa*a', False)
        test(sln, 'aac', 'a*bc', False)
        test(sln, 'bac', 'a*bc', False)
        test(sln, 'bac', 'ba*b', False)
        test(sln, 'bac', 'aa*b', False)
        test(sln, 'abc', 'a*bc', True) 
        test(sln, 'aaa', 'a*aa', True)

    if True:
        test(sln, 'a', '.*..', False)
        test(sln, 'a', '.*.*..', False)
        test(sln, 'a', '.*.*.*..', False)
        
        test(sln, 'ab', '.*..', True)
        test(sln, 'aaa', 'a*.', True)
        test(sln, 'aaab', 'a*ab', True)
        test(sln, 'aaab', 'aa*b', True)
        test(sln, 'aaab', 'a*.', True)
        test(sln, 'ab', '.*c', False)
        test(sln, 'aa', 'a*', True)
        test(sln, 'ab', '.*', True)
        
        test(sln, 'aab', 'ca*b', False)
        test(sln, 'aab', 'c*d*a*b', True)
        test(sln, 'bbbba', '.*a*a', True)
        test(sln, 'a', '.*..a*', False)
        test(sln, 'bbab', 'b*a*', False)
        test(sln, 'a', 'c*.', True)
        test(sln, 'b', 'c*bb', False)
        test(sln, 'aabcbcbcaccbcaabc', '.*a*aa*.*b*.c*.*a*', True) 
        test(sln, 'abbabaaaaaaacaa', 'a*.*b.a.*c*b*a*c*', True) 

    if True:
        
        test(sln, '', 'c*', True)
        test(sln, '', '.*', True)
        test(sln, '', '.', False)
        test(sln, 'a', '', False)
        
        test(sln, '', '', True)
        test(sln, '', 'bab', False)
        test(sln, '', 'c*c*', True)
        