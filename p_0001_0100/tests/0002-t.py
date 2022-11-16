def test(sln, ls1, ls2, target):
    print('ls1 = %s, ls2 = %s, target = %s' % (ls1, ls2, target))

    l1 = ls_to_ll(ls1)
    l2 = ls_to_ll(ls2)
    out = sln.addTwoNumbers(l1, l2)

    out_ls = ll_to_ls(out)
    print("out_ls = %s" % out_ls)
    print('')    
    
    assert out_ls == target

def run(sln):

    test(sln, [2, 4, 3], [5, 6, 4], [7, 0, 8])
    test(sln, [0], [0], [0])
    test(sln, [9, 9, 9, 9, 9, 9, 9], [9, 9, 9, 9], [8, 9, 9, 9, 0, 0, 0, 1])

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def ls_to_ll(ls):
    head = None
    nd0 = None
    for v in ls:
        nd1 = ListNode(v)
        
        if head == None:
            head = nd1
            nd0 = nd1 
        else:
            nd0.next = nd1
            nd0 = nd1 

    return head

def ll_to_ls(head):
    ls = []
    nd = head
    while nd != None:
        ls.append(nd.val)
        nd = nd.next

    return ls

