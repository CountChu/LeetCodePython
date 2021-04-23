#
# 4/11: 6 mins
#

def test(sln, s, numRows, target):
    print('s = %s, numRows = %d' % (s, numRows))    
    out = sln.convert(s, numRows)
    assert out == target, target
    print('')

def run(sln):
    test(sln, 'PAYPALISHIRING', 3, 'PAHNAPLSIIGYIR')
    test(sln, 'PAYPALISHIRING', 4, 'PINALSIGYAHRPI')
    test(sln, 'A', 1, 'A')
