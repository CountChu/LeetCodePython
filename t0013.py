def test(sln, s, target):
    out = sln.romanToInt(s)    
    assert out == target

def run(sln):
    test(sln, 'III', 3)
    test(sln, 'IV', 4)
    test(sln, 'IX', 9)
    test(sln, 'LVIII', 58)
    test(sln, 'MCMXCIV', 1994)
