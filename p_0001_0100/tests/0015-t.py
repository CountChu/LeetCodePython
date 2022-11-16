#
# Write framework: 6 mins.
#

def test(sln, nums, target):
    print('nums = %s, target = %s' % (nums, target))
    out = sln.threeSum(nums)
    out.sort()
    target.sort()
    assert out == target, out

def run(sln):

    test(sln, [1, 2, -2, -1], [])
    test(sln, [-2,0,1,1,2], [[-2,0,2],[-2,1,1]])

    test(sln, [-1, 0, 1, 0], [[-1,0,1]])
    test(sln, [-1, 0, 1, 2, -1, -4], [[-1, -1, 2], [-1, 0, 1]])
    test(sln, [], [])
    test(sln, [0], [])
    test(sln, [0, 0, 0], [[0, 0, 0]])
    
    test(sln, [-1, 0, 1, 2, -1, -4], [[-1, 0, 1], [-1, -1, 2]])

    if True:
        test(
        	sln,
        	[-1, 0, 1, 2, -1, -4, -2, -3, 3, 0, 4],
        	[[-4, 0, 4], [-4, 1, 3], [-3, -1, 4], [-3, 0, 3], [-3, 1, 2], [-2, -1, 3],
             [-2, 0, 2], [-1, -1, 2], [-1 ,0, 1]])