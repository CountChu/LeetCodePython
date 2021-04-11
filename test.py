import json
import argparse
import importlib
import os
import pdb

def main():

    #
    # Parse arguments
    #

    args = build_args()
    
    #
    # Read config.
    #
    
    f = open('config.json')
    config = json.load(f)
    f.close()
    
    #
    # Find problem in the config.
    #
    
    problem = None
    for i, _problem in enumerate(config['problems']):
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
    test_module_name, ext = os.path.splitext(bn)    
    test_module = importlib.import_module(test_module_name)
        
        
    count = 0    
    for solution in problem['solutions']:
        if args.solution != None:
            if solution['id'] == args.solution:
                assert count == 0, 'The solution ID %s is duplicated.' % solution['id']
                count += 1
                solve_it(test_module, solution)
        else:
            solve_it(test_module, solution)
            
#
# Build argument parser and return it.
#

def build_args():
    desc = '''
The app is to test a problem of LeCoo by solutions.
'''

    parser = argparse.ArgumentParser(
                formatter_class=argparse.RawTextHelpFormatter,
                description=desc)

    #
    # Standard arguments
    #

    parser.add_argument(
            '--verbose',
            dest='verbose',
            action='store_true',
            help='Print verbose messages')

    parser.add_argument(
            '--log',
            dest='log',
            action='store_true',
            help='Enable to save log in a file.')
            
    parser.add_argument(
            '--level',
            dest='level',
            default='info',
            help='Level of logging. debug->info->warning->error->critical')             

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
            dest='solution',
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
    sln_module_name, ext = os.path.splitext(bn)    
    sln_module = importlib.import_module(sln_module_name)
    sln = sln_module.Solution()
    test_module.run(sln)

if __name__ == '__main__':
    main()
    