from data_structure import *
import pdb

def test(sln, s, answer):
    print('s = %s, answer = %s' % (s, answer))
    out = sln.decodeString(s)
    assert out == answer, out

def run(sln):
    test(sln, "3[ab2[c]d]", "abccdabccdabccd")

    test(sln, "3[a]2[bc]", "aaabcbc")
    test(sln, "3[a2[c]]", "accaccacc")    
    test(sln, "2[abc]3[cd]ef", "abcabccdcdcdef")    
    test(sln, "abc3[cd]xyz", "abccdcdcdxyz")    
    test(sln, "10[leet]", "leetleetleetleetleetleetleetleetleetleet")

    test(sln, "2[a2[bc]]ef", "abcbc"+"abcbc"+"ef")     

    test(sln, "2[2[y]pq4[2[jk]e1[f]]]ef", "yypqjkjkefjkjkefjkjkefjkjkef"+"yypqjkjkefjkjkefjkjkefjkjkef"+"ef")     

    test(sln, "2[2[y]pq4[2[jk]e1[f]]]", "yypqjkjkefjkjkefjkjkefjkjkefyypqjkjkefjkjkefjkjkefjkjkef")     
    test(sln, "3[z]2[2[y]pq4[2[jk]e1[f]]]", "zzzyypqjkjkefjkjkefjkjkefjkjkefyypqjkjkefjkjkefjkjkefjkjkef")     
    test(sln, "3[z]2[2[y]pq4[2[jk]e1[f]]]ef", "zzzyypqjkjkefjkjkefjkjkefjkjkefyypqjkjkefjkjkefjkjkefjkjkefef")