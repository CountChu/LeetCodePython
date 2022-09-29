from data_structure import *
import pdb

def test(sln, grid, answer):
    print('grid = %s, answer = %d' % (grid, answer))
    out = sln.numIslands(grid)
    assert out == answer, out

def run(sln, module):
	if True:
	    test(
	    	sln,
	    	[ 
	    		["1","1","1","1","0"],
	  			["1","1","0","1","0"],
	  			["1","1","0","0","0"],
	  			["0","0","0","0","0"],
	  		],
	  		1
	  	)

	if True:
	    test(
	    	sln,
	    	[ 
				["1","1","0","0","0"],
	  			["1","1","0","0","0"],
	  			["0","0","1","0","0"],
	  			["0","0","0","1","1"],
	  		],
	  		3
	  	)