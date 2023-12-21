#
# FILENAME.
#       summary.py - Summary Python App.
#
# FUNCTIONAL DESCRIPTION.
#       The app summarizes the progress.
#
# NOTICE.
#       Author: visualge@gmail.com (CountChu)
#       Created on 2021/4/11
#       Updated on 2023/11/30
#

import json
import argparse
import statistics
import datetime
import sys

import config
import util

import pdb
br = pdb.set_trace

#
# Build argument parser and return it.
#

def build_args():
    desc = '''
The app summarizes the progress.

Usage 1:
    python summary.py lesson

Usage 2:
    python summary.py problem

Usage 2:
    python summary.py problem -p    

'''

    parser = argparse.ArgumentParser(
                formatter_class=argparse.RawTextHelpFormatter,
                description=desc)

    #
    # Anonymous arguments.
    #

    parser.add_argument(
            'object',      
            help='object is lesson or problem(p)')
    
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
            help='Date. E.g., "2022/9/3"')     

    parser.add_argument(
            '--like',
            dest='like',
            action='store_true',
            help='Display problem I like.')     

    parser.add_argument(
            '-l',
            dest='lesson',
            help='E.g., p_0001_0100')  

    parser.add_argument(
            '-p',
            dest='problem',
            help='Problem ID. E.g., 0002')  

    return parser.parse_args()

def display_problems(title, pbl_ls):
    print('%s: (%d)' % (title, len(pbl_ls)))

    w = 0
    for problem in pbl_ls:
        id = problem['id']
        w = max(0, len(id))

    for problem in pbl_ls:
        id = problem['id']
        level = problem['level']
        name = problem['name']
        fmt = '    %'+str(w)+'s, %7s: %s'
        print(fmt % (id, level, name))
    print('')

def display_references(title, refer_ls):
    print('%s: (%d)' % (title, len(refer_ls)))

    w = 0
    for refer in refer_ls:
        id = refer['ref']
        problem = refer['problem']
        lesson = problem['lesson']
        level = problem['level']
        name = problem['name']

        fmt = '    %s @ %s, %s: %s'
        print(fmt %(id, lesson, level, name))
    print('')

def handle_problem(args, cfg):

    #
    # Check args.
    #

    if args.like and (args.lesson != None):
        print('Error --like and -l can not be set at the same time.')
        sys.exit(0)

    #
    # Get date_str. e.g., '2021/4/22' 
    #

    if args.date == None:
        date_str = datetime.date.today().strftime('%Y/%-m/%-d')
    else:
        date_str = args.date


    #
    # If --like, report problems I like.
    #

    if args.like:
        problems = []
        for problem in cfg['problems']:
            if 'like' in problem:
                if problem['like']:
                    problems.append(problem)

        display_problems('Liked problems', problems)
        sys.exit(0)

    #
    # If -l, report problems in the lesson.
    #

    if args.lesson:
        problems = []
        for problem in cfg['problems']:
            if problem['lesson'] == args.lesson:
                problems.append(problem)

        display_problems('Liked problems', problems)


        references = []
        for reference in cfg['references']:
            if reference['lesson'] == args.lesson:
                references.append(reference)
        display_references('Liked problems(refer)', references)

        sys.exit(0)

    #
    # Report them.
    #    

    problems = cfg['problems']
    print('Problems: %d' % len(problems))

    #
    # Report solved solutions.
    #

    for problem in problems:
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
    for problem in problems:
        if problem['solved']:
            solved_count += 1
        else:
            unsolved_pbl_ls.append(problem)

    print('Solved Problem: %d' % solved_count)
    print('')

    #
    # Build level_coding_d
    #

    level_coding_d = {
        'easy': [],
        'medium': [],
        'hard': []
        }

    for problem in problems:
        if not problem['solved']:
            continue

        name = problem['name']
        level = problem['level']
        last_sln = problem['solutions'][-1]
        if 'coding' in last_sln:
            coding = last_sln['coding']
            if coding == 0:
                continue

            level_coding_d[level].append(coding)

    #
    # Build problem['history']
    #
    '''
    for problem in problems:
        if problem['solved']:
            history = util.gen_history(problem['solutions'])
            problem['history'] = history
    '''
    #print('')

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
    for problem in problems:
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

            if 'again' in sln:
                for d in sln['again']:
                    if d == date_str:
                        if id not in progress_d:
                            progress_d[id] = {
                                'problem': problem,
                                'solutions': [] 
                                }
                        progress_d[id]['solutions'].append(sln)   

    #
    # Transform progress_d into progress_ls
    # progress_ls = [progress]
    # progress = {'solution', 'problem'}
    #

    progress_ls = []
    for id in progress_d:
        problem = progress_d[id]['problem']
        solutions = progress_d[id]['solutions']
        for sln in solutions:
            sln['programDateTime'] = sln['programDate'] + ' ' + sln['programTime']
            progress = {'solution': sln, 'problem': problem}
            progress_ls.append(progress)

    #
    # Sort progress_ls by programDateTime
    #

    progress_ls.sort(key = lambda x: x['solution']['programDateTime'])

    #
    # Report progress_ls.
    #

    #pdb.set_trace()
    print('Progress on %s:' % date_str)
    print('')
    for progress in progress_ls:
        sln = progress['solution']
        problem = progress['problem']

        if sln['programDate'] == date_str:
            time_str = sln['programTime']
        else:
            time_str = '%s %s' % (sln['programDate'], sln['programTime'])        

        print('%s | %4s | %6s | %s' % (time_str, problem['id'], problem['level'], problem['name']))

        line = ' ' * len(time_str) + ' | ' + sln['id'] + ' | '
        line += util.get_performance(sln)
        
        print(line)
        print('')

    print('')        

    #
    # Report unsolved_pbl_ls
    #

    display_problems('Unsolved problems', unsolved_pbl_ls)

    #
    # All problem status
    #

    if args.detail:
        print('All problems status:')
        for problem in problems:
            pid = problem['id']
            name = problem['name']
            level = problem['level']
            date = ''

            if problem['solved']:
                key, sln = util.get_last_solution(problem)
            else:
                key = ''
                
            print('%6s | %6s | %-14s | %s' % (pid, level, key, name))
    print('')    

    #
    # One problem status
    #

    if args.problem != None:
        if args.problem not in cfg['idProblem']:
            print('Error! The problem %s does not exist.' % args.problem)
            sys.exit(0)

        problem = cfg['idProblem'][args.problem]
        pid = problem['id']
        name = problem['name']
        level = problem['level']
        lesson = problem['lesson']
        print('The problem:   %s | %6s | %s @ %s' % (pid, level, name, lesson))

        print('The history:')
        #history = problem['history']
        history = util.gen_history(problem['solutions'])
        for key in sorted(history.keys()):
            sln = history[key]
            line = ' '*15 + key + " | "
            line += util.get_performance(sln)
            print(line)
    print('')

def handle_lesson(args, cfg):
    problems = cfg['problems']

    lessons = set()
    for problem in problems:
        lessons.add(problem['lesson'])

    lesson_ls = list(lessons)
    lesson_ls.sort()
    print('Lessons:')
    for lesson in lesson_ls:
        print('    '+lesson)

def main():

    #
    # Parse arguments
    #

    args = build_args()

    #
    # Merge configs into a config
    #

    cfg = config.collect(None)

    #
    # Check cfg syntex.
    # 

    for problem in cfg['problems']:
        assert 'id' in problem
        assert 'name' in problem
        assert 'level' in problem, problem

        level = problem['level']
        assert level in ['easy', 'medium', 'hard'], level

        keys = problem.keys()
        for key in keys:
            if key not in ['id', 'name', 'inferId', 'level', 'testScript', 'lesson', 'fn', 'solutions', 'like']:
                print('Error. The key %s is wrong in the problem' % key)
                print(problem)
                sys.exit(0)

        if 'solutions' not in problem:
            print('Error the solutions are not in the problem')
            print(problem)
            sys.exit(0)

        for sln in problem['solutions']:
            keys = sln.keys()
            for key in keys:
                if key not in ['id', 'program', 'programDate', 'programTime', 'date', 'bug', 'design', 'coding', 'runtime', 'memory', 'fasterThan', 'again']:
                    print('Error. The key %s is wrong in the solution' % key)
                    print(sln)
                    sys.exit(0)

                if 'runtime' in keys:
                    assert 'date' in keys, sln

                if 'bug' in keys:
                    assert 'date' in keys, sln

                if 'again' in keys:
                    assert type(sln['again']) == list, sln

    #
    # Dispatch object
    #

    if args.object in ['problem', 'p']:
        handle_problem(args, cfg)

    elif args.object == 'lesson':
        handle_lesson(args, cfg)

    else:
        assert False


if __name__ == '__main__':
    main()
    