import json
import os

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
