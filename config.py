import os
import json
import importlib
import sys
from datetime import datetime

import gen 
import util

import pdb
br = pdb.set_trace

def collect_solution_bns(cfg, lesson_dn):
    solutionDn = cfg['dirs']['solutionDn']
    solutions_dn = util.get_dn_and_build(lesson_dn, solutionDn)
    bns = []
    for bn2 in os.listdir(solutions_dn):
        fn = os.path.join(solutions_dn, bn2)
        if not os.path.isfile(fn):
            continue
        bns.append(bn2)
    return bns

def get_problem_fn_create(cfg, lesson_dn, problem):
    problemDn = cfg['dirs']['problemDn']
    problems_dn = util.get_dn_and_build(lesson_dn, problemDn)

    problem_bn = '%s-%s.py' % (problem['id'], problem['inferId'])
    problem_fn = os.path.join(problems_dn, problem_bn)

    return problem_fn

def infer_solutions(cfg, bn, solution_bns, problem):
    solutionDn = cfg['dirs']['solutionDn']
    id = problem['id']
    inferId = problem['inferId']
    matched_bns = []
    prefix = '%s-%s-' % (id, inferId)
    for sln_bn in solution_bns:
        if sln_bn.find(prefix) == 0:
            matched_bns.append(sln_bn)
    matched_bns.sort()

    solutions = []
    for m_bn in matched_bns:
        sln_fn = os.path.join(bn, solutionDn, m_bn)
        assert os.path.exists(sln_fn)
        sln_module_name = util.get_module_name(sln_fn)
        sln_module = importlib.import_module(sln_module_name)
        solution_json = sln_module.solution_json
        sln_id = m_bn[len(prefix):-3]
        solution_json['id'] = sln_id 
        solution_json['program'] = '%s-%s-%s.py' % (id, inferId, sln_id)
        solutions.append(solution_json)

    return solutions

def handle_id(pid, problem, cfg, lesson_dn, solution_bns, merged_cfg):
    #print('Handle %s' % problem['id'])
    problem['lesson'] = lesson_dn

    if 'inferId' in problem: 
        problem_fn = get_problem_fn_create(cfg, lesson_dn, problem)
        if pid != None and problem['id'] == pid: 
            if not os.path.exists(problem_fn):
                print('The problem does not exist.')
                print(problem_fn)
                answer = input('Do you want to create it? [y/Y]')
                if answer in ['y', 'Y']:
                    f = open(problem_fn, 'w')
                    content = gen.problem()
                    f.write(content)
                    f.close()
                    print('Build ', problem_fn)
                sys.exit()

        problem['fn'] = problem_fn

    if not 'testScript' in problem:

        #
        # Infer testScript as follows:
        #
        #   problem.id = '0001'
        #   ---> testScript = '0001-t.py'
        #

        testDn = cfg['dirs']['testDn']
        testScript_bn = '%s-t.py' % problem['id']
        tests_dn = util.get_dn_and_build(lesson_dn, testDn)
        testScript_fn = os.path.join(tests_dn, testScript_bn)
        problem['testScript'] = testScript_bn  

    #
    # If inferId is specified, inter solutions as follows:
    #
    #   problem.id = '0001'
    #   inferId = 'two-sum'
    #   A solution is read from solution_json in 0001-two-sum-s1.py
    #
    #   ---> program = 0001-tw-sum-s2.py 
    #

    if 'inferId' in problem:
        assert 'solutions' not in problem
        solutions = infer_solutions(cfg, lesson_dn, solution_bns, problem)
        problem['solutions'] = solutions

    fn = problem['testScript']
    fn = os.path.join(lesson_dn, cfg['dirs']['testDn'], fn)
    problem['testScript'] = fn

    if 'solutions' not in problem:
        print('Error! Solutions of the problem are not found.')
        print('problem:')
        print(problem)
        #br()

    else:
        for sln in problem['solutions']:
            fn = sln['program']
            fn = os.path.join(lesson_dn, cfg['dirs']['solutionDn'], fn)
            sln['program'] = fn

            t = os.path.getmtime(fn)
            dt = datetime.fromtimestamp(t)

            #sln['programDate'] = dt.strftime('%Y/%-m/%-d')
            sln['programDate'] = dt.strftime('%Y/%m/%d')
            sln['programTime'] = dt.strftime('%H:%M')

    merged_cfg['problems'].append(problem)
    merged_cfg['idProblem'][problem['id']] = problem


def handle_ref(problem, lesson_dn, merged_cfg):
    #print('Handle %s' % problem['ref'])    
    reference = {
        'ref': problem['ref'],
        'lesson': lesson_dn,
        }

    merged_cfg['references'].append(reference)

def collect(pid):
    cfg_ls = []
    lesson_dn_ls = []
    for bn in os.listdir('.'):
        fn = os.path.join(bn, 'config.json')
        if os.path.exists(fn):         
            lesson_dn_ls.append(bn)   
            f = open(fn)
            cfg = json.load(f)
            f.close()
            cfg_ls.append(cfg)

    #
    # For each problem, check the syntax of it.
    #

    for cfg, lesson_dn in zip(cfg_ls, lesson_dn_ls):
        for problem in cfg['problems']:
            for key in problem:
                if key not in ['id-', 'id', 'like', 'testScript', 'ref', 'inferId', 'name', 'level']:
                    print('Error! The %s is invalid for the problem %s' % (key, problem))
                    sys.exit(0)    

    #
    # Check duplicated problem id.
    #

    id_ls = []
    for cfg, lesson_dn in zip(cfg_ls, lesson_dn_ls):
        for problem in cfg['problems']:
            if 'id' in problem:
                if problem['id'] in id_ls:
                    print('Error. The problem id %s is duplicated.' % problem['id'])
                    sys.exit(0)
                
                id_ls.append(problem['id'])
    
    #
    # Transform cfg_ls into merged_cfg (combined)
    #

    merged_cfg= {
        'problems': [],
        'references': [],
        'idProblem': {},
        }

    for cfg, lesson_dn in zip(cfg_ls, lesson_dn_ls):
        solution_bns = collect_solution_bns(cfg, lesson_dn)

        for problem in cfg['problems']:
            if 'id' in problem:
                handle_id(pid, problem, cfg, lesson_dn, solution_bns, merged_cfg)

            elif 'ref' in problem:
                handle_ref(problem, lesson_dn, merged_cfg)

    #
    # Build merged_cfg['references']
    #

    for refer in merged_cfg['references']:
        id = refer['ref']
        problem = merged_cfg['idProblem'][id]
        refer['problem'] = problem

    #
    # Sort merged_cfg['problems']
    #

    merged_cfg['problems'] = sorted(merged_cfg['problems'], key=lambda x: x['id'])

    return merged_cfg

