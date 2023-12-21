#
# FILENAME.
#       test.py - Test Python App.
#
# FUNCTIONAL DESCRIPTION.
#       The app runs a python program by given a solution ID to solve a problem. 
#
# NOTICE.
#       Author: visualge@gmail.com (CountChu)
#       Created on 2021/4/11
#       Updated on 2023/11/30
#

import json
import argparse
import os
import importlib
import shutil
import sys

import config
import gen 
import util

import pdb
br = pdb.set_trace

#
# Build argument parser and return it.
#

def build_args():
    desc = '''
The app runs a python program by given a solution ID to solve a problem.

Usage 1:
    python test.py 0073 -s p

Usage 2:
    python test.py 0073
'''

    parser = argparse.ArgumentParser(
                formatter_class=argparse.RawTextHelpFormatter,
                description=desc)

    #
    # Anonymous arguments.
    #

    parser.add_argument(
            'problem',
            help='An ID of the problem that is defined in config.json. E.g., 010')

    #
    # Specific arguments
    #

    parser.add_argument(
            '-s',
            dest='sid',
            help='A solution ID that is defined in config.json. E.g., v1') 
            
    '''
    parser.add_argument(
            '--test',
            dest='test',
            action='store_true',
            help='For test.')             
    '''

    return parser.parse_args()

def solve_it(test_module, solution):
    
    bn = solution['program']
    if not os.path.exists(bn):
        print('The program does not exist.')
        print(bn)
        answer = input('Do you want to create it? [y/Y]')
        if answer in ['y', 'Y']:
            content = gen.solution_0()
            f = open(bn, 'w')
            f.wirtelines(content)
            print('Build ', bn)
        sys.exit(0)

    sln_module_name = util.get_module_name(bn)
    sln_module = importlib.import_module(sln_module_name)
    sln = sln_module.Solution()
    #test_module.run(sln, sln_module)
    test_module.run(sln)

def main():

    #
    # Parse arguments
    #

    args = build_args()
    
    #
    # Merge configs into a config
    #

    cfg = config.collect(args.problem)
    
    #
    # Find problem in the config.
    #
    
    problem = None
    for i, _problem in enumerate(cfg['problems']):
        if args.problem == _problem['id']:
            assert problem == None, 'The problem ID %s is duplicated.' % _problem['id']
            problem = _problem
    
    if problem == None:
        print('Error. The problem ID %s is not found.' % args.problem)
        sys.exit(0)

    print('Problem: %s' % problem['name'])  
    print('')

    #
    # Import testScript
    #

    bn = problem['testScript']
    if not os.path.exists(bn):
        print('The testScript does not exist.')
        print(bn)
        answer = input('Do you want to create it? [y/Y]')
        if answer in ['y', 'Y']:
            f = open(bn, 'w')
            content = gen.test()
            f.write(content)
            f.close()
            print('Build ', bn)
        sys.exit(0)

    test_module_name = util.get_module_name(bn) 
    test_module = importlib.import_module(test_module_name)


    if args.sid == None:
        for solution in problem['solutions']:
            print('Solution: %s' % solution['id'])
            solve_it(test_module, solution)
            print('')

    else:

        #
        # Get solution......
        #

        found_solution = None 
        for solution in problem['solutions']:
            if solution['id'] == args.sid:
                found_solution = solution

        if found_solution:
            solve_it(test_module, found_solution)
        else:
            print('The solution %s is not found.' % args.sid)
            if problem['inferId']:
                answer = input('Do you want to create the solution %s for the problem %s-%s? [y/Y]' % (
                            args.sid, 
                            problem['id'], 
                            problem['inferId']))
                
                if answer in ['y', 'Y']:
                    if 'fn' in problem:
                        solution_bn = '%s-%s-%s.py' % (problem['id'], problem['inferId'], args.sid)
                        solution_fn = os.path.join(problem['lesson'], 'solutions', solution_bn)
                        assert not os.path.exists(solution_fn)
                        gen.solution(problem['fn'], solution_fn)
                        print(solution_fn)

                sys.exit(0)

if __name__ == '__main__':
    main()
    