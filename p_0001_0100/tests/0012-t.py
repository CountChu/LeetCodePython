def test(sln, num, target):
    print('num = %d, target = %s' % (num, target))
    out = sln.intToRoman(num)    
    assert out == target

def run(sln):
    test(sln, 3, 'III')
    test(sln, 4, 'IV')
    test(sln, 9, 'IX')
    test(sln, 58, 'LVIII')
    test(sln, 1994, 'MCMXCIV')