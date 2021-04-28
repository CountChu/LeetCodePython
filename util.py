import json
import os

def collect_config():
    config_ls = []
    bn_ls = []
    for bn in os.listdir('.'):
        fn = os.path.join(bn, 'config.json')
        if os.path.exists(fn):         
            bn_ls.append(bn)   
            f = open(fn)
            config = json.load(f)
            f.close()
            config_ls.append(config)

    #
    # Transform config_ls into merged_config (combined)
    #

    merged_config = {
        'problems': []
        }
    for config, bn in zip(config_ls, bn_ls):
        for problem in config['problems']:
            if not 'testScript' in problem:
                continue

            fn = problem['testScript']
            fn = os.path.join(bn, config['dirs']['testDn'], fn)
            problem['testScript'] = fn
            for sln in problem['solutions']:
                fn = sln['program']
                fn = os.path.join(bn, config['dirs']['programDn'], fn)
                sln['program'] = fn
            merged_config['problems'].append(problem)

    merged_config['problems'] = sorted(merged_config['problems'], key=lambda x: x['id'])

    return merged_config

