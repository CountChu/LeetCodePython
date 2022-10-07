from data_structure import *
import pdb

def test(sln, nums, key, answer):
    print('nums = %s, key = %d, answer = %s' % (nums, key, answer))
    root = binary_tree_v3.ls_to_tree(nums)
    root = sln.deleteNode(root, key)
    root_ls = binary_tree_v3.tree_to_ls(root)
    assert root_ls == answer, root_ls

def run(sln):
    if True:                            # Example 1
        '''
                    5              5
                 3     6        4     6
                2 4      7     2        7
        '''
        test(sln, [5, 3, 6, 2, 4, None, 7], 3, [5, 4, 6, 2, None, None, 7])

    if True:                            # Example 2
        test(sln, [5, 3, 6, 2, 4, None, 7], 0, [5, 3, 6, 2, 4, None, 7])

    if True:                            # Example 3
        test(sln, [], 0, [])

    if True:
        """
                    5              6
                 3     6       3      7
                2 4     7     2 4
        """
        test(sln, [5, 3, 6, 2, 4, None, 7], 5, [6, 3, 7, 2, 4])

    if True:
        test(sln, [0], 0, [])
        test(sln, [1,None,2], 1, [2])

    if True:
        """
                  50                    60
            30          70     ->  30        70
               40    60    80         40        80
        """
        test(
            sln, 
            [50, 30, 70, None, 40, 60, 80], 
            50, 
            [60, 30, 70, None, 40, None, 80]
        )

    if True:
        """
                   3
              2         5 <-
                     4     10
                          8  15
                         7
        """ 
        test(
            sln, 
            [3, 2, 5, None, None, 4, 10, None, None, 8, 15, 7], 
            5, 
            [3, 2, 7, None, None, 4, 10, None ,None, 8, 15
            ]
        )

    if True:
        test(
            sln,
            [
                2,
                0, 33,
                None, 1, 25, 40,
                None, None, None, None, 34, 45,
                None, 36, None, None,
                35, 39
            ],
            33,
            [
                2,
                0, 34,
                None, 1, 25, 40,
                None, None, None, None, 36, 45,
                35, 39
            ],
        )

    if True:
        """
                      5
                 3        6
               2   4         7     
        """
        test(
            sln,
            [5, 3, 6, 2, 4, None, 7],
            7,
            [5, 3, 6, 2, 4]
        )

    if True:
        """
                    2<-
                 1   
        """
        test(
            sln,
            [2, 1],
            2,
            [1]
        )

    if True:
        """
                  3
              2       4
            1
        """
        test(
            sln,
            [3, 2, 4, 1],
            2,
            [3, 1, 4]
        )

    if True:
        """
                       33                  33
                   25<-    40          12<-    40
              11                    11
            7   12<-              7
        """
        test(
            sln,
            [33, 25, 40, 11, None, None, None, 7, 12],
            25,
            [33, 12, 40, 11, None, None, None, 7]
        )


