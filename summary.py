import json
import argparse
import statistics
import datetime
import pdb

import util

def main():

    #
    # Parse arguments
    #

    args = build_args()

    #
    # Merge configs into a config
    #

    config = util.collect_config()

    #
    # Get date_str. e.g., '2021/4/22' 
    #

    if args.date == None:
        date_str = datetime.date.today().strftime('%Y/%-m/%-d')
    else:
        date_str = args.date
    #pdb.set_trace()

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
                assert key in ['id', 'program', 'date', 'bug', 'design', 'coding', 'runtime', 'memory'], sln

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
            if 'coding' not in last_sln:
                solved = False
        problem['solved'] = solved
        
    unsolved_pbl_ls = []
    solved_count = 0    
    for problem in config['problems']:
        if problem['solved']:
            solved_count += 1
        else:
            unsolved_pbl_ls.append(problem)

    print('Solved Problem: %d' % solved_count)

    #
    # Build level_coding_d
    #

    level_coding_d = {
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
        if 'coding' in last_sln:
            coding = last_sln['coding']
            level_coding_d[level].append(coding)
            if args.detail:
                print('%s:' % name)
                print('    level = %6s, coding = %d' % (level, coding))    
    print('')

    #
    # Report level_coding_d
    #

    print('Time taken:')
    for level, coding_ls in level_coding_d.items():
        #print(timeTaken_ls)
        max_tt = max(coding_ls)
        mean = statistics.mean(coding_ls)
        count = len(coding_ls)
        print('    %-7s: count = %3d, mean = %3d mins, max = %3d mins' % (level, count, mean, max_tt))
    print('')

    #
    # Build progress_d.
    #

    progress_d = {}  # progress_d[id] = {'problem', 'solutions'}
    for problem in config['problems']:
        id = problem['id']
        for sln in problem['solutions']:
            if 'date' in sln:
                if sln['date'] == date_str:
                    if id not in progress_d:
                        progress_d[id] = {
                            'problem': problem,
                            'solutions': [] 
                            }
                    progress_d[id]['solutions'].append(sln)

    #
    # Report progress.
    #

    #pdb.set_trace()
    print('Progress on %s:' % date_str)
    for id in progress_d:
        problem = progress_d[id]['problem']
        id = problem['id']
        level = problem['level']
        name = problem['name']        
        print('    %4s, %7s: %s' % (id, level, name))
        solutions = progress_d[id]['solutions']
        for sln in solutions:
            line = '                   %s: ' % sln['id']
            if 'design' in sln:
                line += 'design: %d mins, ' % sln['design']            
            if 'coding' in sln:
                line += 'coding: %d mins, ' % sln['coding']
            if 'runtime' in sln:
                line += 'runtime: %s, ' % sln['runtime']
            if 'memory' in sln:
                line += 'memory: %s, ' % sln['memory']
            if 'bug' in sln:
                line += 'bug: %s, ' % sln['bug']
            print(line)
        print('')
    print('')        


    #
    # Report unsolved_pbl_ls
    #

    print('Unsolved problems: (%d)' % len(unsolved_pbl_ls))
    for problem in unsolved_pbl_ls:
        id = problem['id']
        level = problem['level']
        name = problem['name']
        print('    %4s, %7s: %s' % (id, level, name))
    print('')

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

    parser.add_argument(
            '--date',
            dest='date',
            help='Date')     

    return parser.parse_args()



if __name__ == '__main__':
    main()
    