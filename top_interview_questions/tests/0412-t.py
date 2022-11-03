
from data_structure import *
import pdb
br = pdb.set_trace

def test_solution(sln, n, target):
    print("n = %d, target = %s" % (n, target))
    out = sln.fizzBuzz(n)
    print("out = %s" % out)
    print('')

    assert out == target

def run(sln):
    test_solution(sln, 3, ["1", "2", "Fizz"])
    test_solution(sln, 5, ["1", "2", "Fizz", "4", "Buzz"])
    test_solution(sln, 15, ["1", "2", "Fizz", "4", "Buzz", "Fizz", "7", "8", "Fizz", "Buzz", "11", "Fizz", "13", "14", "FizzBuzz"])

