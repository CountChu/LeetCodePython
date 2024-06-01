def test(sln, s, target):
    print('s = %s, target = %d' % (s, target))    
    out = sln.romanToInt(s)    
    assert out == target, out
    print('')

def run(sln):
    test(sln, 'II', 2)
    test(sln, 'XII', 12)    
    test(sln, 'XXVII', 27) 
    test(sln, 'IV', 4)
    test(sln, 'IX', 9)

    test(sln, 'MCMXCIV', 1994)    
    test(sln, 'III', 3)
    test(sln, 'LVIII', 58)
