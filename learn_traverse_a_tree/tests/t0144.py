import pdb

def test(sln, nums, answer):
    print('nums = %s, answer = %s' % (nums, answer))
    nums = sln.transform_ls(nums)
    root = sln.ls_to_tree(nums)
    #pdb.set_trace()

    #nums = sln.tree_to_ls(root)
    #pdb.set_trace()

    out = sln.preorderTraversal(root)

    assert out == answer, out


def run(sln):
    test(sln, [0, 1, 2, 3, 4, 5, 6, 7, 8], [0, 1, 3, 7, 8, 4, 2, 5, 6])
    test(sln, [1,None,2,3], [1,2,3])
    test(sln, [], [])
    test(sln, [1], [1])
    test(sln, [1,2], [1,2])
    test(sln, [1,None,2], [1,2])
