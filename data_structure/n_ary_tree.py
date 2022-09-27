class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

def _build_nd_ls(ls):
    ns_ls = []
    for v in ls:
        nd = Node(v)
        ns_ls.append(nd)
    return ns_ls

def ls_to_n_ary_tree(ls):
    v_ls = []
    q = []
    nd = None
    head = None
    for v in ls:
        if v == None:
            nd_ls = _build_nd_ls(v_ls)
            q += nd_ls
            if nd == None:
                nd = q.pop(0)
                head = nd
            else:
                nd.children = nd_ls
                nd = q.pop(0)

            v_ls = []
        
        else:
            v_ls.append(v)

    nd_ls = _build_nd_ls(v_ls)      
    nd.children = nd_ls   
    
    return head