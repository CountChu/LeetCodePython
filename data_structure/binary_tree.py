import pdb

#
# 2021/5/1: 15 mins, 42 mins
#

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def transform_ls(nums):
    d = False

    null_ls = []
    count = 0
    for i in range(len(nums)):
        if nums[i] == None:
            null_ls.append(i)
            null_ls.append(i*2 + 1)
            null_ls.append(i*2 + 2)
            count += 3
        else:
            count += 1

    if d:
        print('null_ls = %s, count = %d' % (null_ls, count))
    
    out = [None] * count
    j = 0
    for i in range(len(nums)):
        if nums[i] == None:
            continue

        while True:
            if j in null_ls:
                j += 1
            else:
                break

        if d:
            print(i, j, out)

        out[j] = nums[i]
        j += 1

    last_idx = 0
    for i in range(len(out)):
        if out[i] != None:
            last_idx = i
    
    out = out[:last_idx + 1]

    if d:
        print('out = %s' % out)

    return out

def ls_to_tree(nums):
    if nums == []:
        return None

    root = TreeNode(nums[0])        
    for i in range(1, len(nums)):
        build_node(root, i, nums[i])
    return root

def tree_to_ls(root):
    d = False

    if root == None:
        return []

    out = []
    queue = [root]
    while True:
        if queue == []:
            break

        node = queue.pop(0)
        if d:
            print(node.val)
        out.append(node.val)
        
        if node.left != None:
            queue.append(node.left)
        
        if node.right != None:
            queue.append(node.right)

    return out


def build_node(root, idx, val):
    path = get_path(idx)
    #pdb.set_trace()
    node = root
    for i in range(len(path)):
        if path[i] == 'l':
            if node.left == None:
                node.left = TreeNode()
            node = node.left
        elif path[i] == 'r':
            if node.right == None:
                node.right = TreeNode()
            node = node.right           
        else:
            assert False, path[i]

        if i == len(path) - 1:
            node.val = val

    return node

#
# 1 ---> (3, 4)
# if idx is odd, left, idx = (idx - 1) / 2
# if idx is event, right, idx = idx / 2
#

def get_path(idx):

    path = []
    while True:
        if idx == 0:
            break
        if idx % 2 == 0:
            idx = (idx - 1) // 2
            path.insert(0, 'r')
        else:
            idx = idx // 2
            path.insert(0, 'l')

    #pdb.set_trace()
    return path

