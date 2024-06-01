
from data_structure import *
import pdb
br = pdb.set_trace

def test_solution(sln, strs, target):
    print("strs = %s, target = %s" % (strs, target))
    out = sln.groupAnagrams(strs)
    print("out = %s" % out)
    print('')

    for ls in out:
        ls.sort()
    out.sort()

    for ls in target:
        ls.sort()
    target.sort()

    #br()
    assert out == target

def run(sln):

    if True:
        test_solution(
            sln, 
            ["eat", "tea", "tan", "ate", "nat", "bat"], 
            [
                ["bat"],
                ["nat", "tan"],
                ["ate", "eat", "tea"]
            ])

    if True:
        test_solution( 
            sln, 
            [""],
            [[""]])

    if True:
        test_solution(
            sln,
            ["a"],
            [["a"]])
