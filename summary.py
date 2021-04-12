import json
import argparse
import importlib
import statistics
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
    # Check config syntex.
    # 

    for problem in config['problems']:
        assert 'id' in problem
        assert 'name' in problem
        assert 'level' in problem

        level = problem['level']
        assert level in ['easy', 'medium', 'hard']

        keys = problem.keys()
        for key in keys:
            assert key in ['id', 'name', 'level', 'testScript', 'solutions'], problem
        for sln in problem['solutions']:
            keys = sln.keys()
            for key in keys:
                assert key in ['id', 'program', 'date', 'bug', 'timeTaken', 'runtime', 'memory'], sln

    #
    # Report them.
    #    

    print('Problems: %d' % len(config['problems']))

    #
    # Report solved solutions.
    #

    for problem in config['problems']:
        solved = False
        if len(problem['solutions']) >= 1:
            solved = True
            last_sln = problem['solutions'][-1]
            if 'bug' in last_sln:
                solved = False
        problem['solved'] = solved
        
    solved_count = 0    
    for problem in config['problems']:
        if problem['solved']:
            solved_count += 1
    print('Solved Problem: %d' % solved_count)

    #
    # Report time taken.
    #

    level_timeTaken_d = {
        'easy': [],
        'medium': [],
        'hard': []
        }

    for problem in config['problems']:
        if not problem['solved']:
            continue

        name = problem['name']
        level = problem['level']
        last_sln = problem['solutions'][-1]
        if 'timeTaken' in last_sln:
            timeTaken = last_sln['timeTaken']
            level_timeTaken_d[level].append(timeTaken)
            if args.detail:
                print('%s:' % name)
                print('    level = %6s, timeTaken = %d' % (level, timeTaken))    

    #
    # Report level_timeTaken_d
    #

    print('TIme taken:')
    for level, timeTaken_ls in level_timeTaken_d.items():
        max_tt = max(timeTaken_ls)
        mean = statistics.mean(timeTaken_ls)
        count = len(timeTaken_ls)
        print('    %-7s: count = %3d, mean = %3d mins, max = %3d mins' % (level, count, mean, max_tt))

    #pdb.set_trace()
                        

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

    '''    
    parser.add_argument(
            'problem',       
            help='An ID of the problem that is defined in config.json. E.g., 010')
    '''
    
    #
    # Specific arguments
    #

    parser.add_argument(
            '-d',
            dest='detail',
            action='store_true',
            help='Detail.')             

    return parser.parse_args()



if __name__ == '__main__':
    main()
    