import json
import os
import datetime
import sys

import pdb
br = pdb.set_trace

def get_module_name(fn):
    mn, ext = os.path.splitext(fn) 
    mn = mn.replace('\\', '.')
    mn = mn.replace('/', '.') 
    return mn

def get_dn_and_build(home, sub_dn):
    dn = os.path.join(home, sub_dn)

    if not os.path.exists(dn):
        print('Build %s' % dn)
        os.mkdir(dn)

    return dn

def decorate_date(date):
    d = datetime.datetime.strptime(date, '%Y/%m/%d')
    date_f = d.strftime('%Y/%m/%d')
    return date_f

def gen_history(sln_ls):
    out = {}
    for sln in sln_ls:
        sid = sln['id']

        date = sln['date']

        try:
            date_f = decorate_date(date)
        except:
            print('Error. The date %s is wrong.' % date)
            print(sln)
            sys.exit(0)

        key = '%s-%s' % (date_f, sid)
        if key in out:
            print('Error! The key %s is duplicated.' % key)
            print(sln)
            sys.exit(0)

        out[key] = sln

        if 'again' in sln:
            for date in sln['again']:

                try:
                    date_f = decorate_date(date)
                except:
                    print('Error. The date %s is wrong.' % date)
                    print(sln)
                    sys.exit(0)

                key = '%s-%s' % (date_f, sid)
                if key in out:
                    print('Error! The key %s is duplicated.' % key)
                    print(sln)
                    sys.exit(0)

            out[key] = sln

    return out

def get_last_solution(problem):
    keys = list(problem['history'].keys())
    keys.sort()
    key = keys[-1]
    out = problem['history'][key]
    return key, out

def get_performance(sln):
    out = ''

    if 'design' in sln:
        if sln['design'] != 0:
            out += 'design: %d mins, ' % sln['design']            
    
    if 'coding' in sln:
        if sln['coding'] != 0:
            out += 'coding: %d mins, ' % sln['coding']
    
    if 'runtime' in sln:
        out += 'runtime: %s, ' % sln['runtime']
    
    if 'fasterThan' in sln:
        out += 'fasterThan: %s, ' % sln['fasterThan']

    if 'memory' in sln:
        out += 'memory: %s, ' % sln['memory']
    
    if 'bug' in sln:
        out += 'bug: %s, ' % sln['bug']

    return out


