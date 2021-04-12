def test(sln, list1, list2, target):
    link1 = sln.list_to_link(list1)
    link2 = sln.list_to_link(list2)
    
    out_link = sln.mergeTwoLists(link1, link2)
    out = out_link = sln.link_to_list(out_link)
    print('list1 = %s, list2 = %s, out = %s' % (list1, list2, out))
    assert out == target

def run(sln):
    test(sln, [1, 2, 4], [1, 3, 4], [1, 1, 2, 3, 4, 4])
    test(sln, [], [], [])
    test(sln, [], [0], [0])