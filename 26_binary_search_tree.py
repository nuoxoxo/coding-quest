lines = open(0).read().splitlines()

class bst_node:
    def __init__ (self, val):
        self.val = val
        self.L = None
        self.R = None

def sorted_to_bst(A):
    mid = len(A) // 2
    node = bst_node(A[mid])
    node.L = sorted_to_bst(A[:mid])
    node.R = sorted_to_bst(A[mid+1:])
    return node

def sorted_to_bst_alt(A):
    # cf. leetcode
    def make_tree(arr, left, right):
        if left > right:
            return None
        mid = (right - left) // 2 + left
        node = bst_node(arr[mid])
        node.L = make_tree(arr, left, mid - 1)
        node.R = make_tree(arr, mid + 1, right)
        return node
    return make_tree(A, 0, len(A) - 1)

def nonsorted_array_to_bst(A):
    root = None
    def bst_insert(node, val):
        if not node:
            return bst_node(val)
        if val < node.val:
            node.L = bst_insert(node.L, val)
        else:
            node.R = bst_insert(node.R, val)
        return node
    for val in A:
        root = bst_insert( root, val )
    return root

A = []
for line in lines:
    A.append(int(line, 16))

# root = sorted_to_bst( A )
# root = sorted_to_bst_alt( A )
# both not right here
# ... in the order it is given to you (ie: don't pre-sort the data). !!!

root = nonsorted_array_to_bst( A )

def height(node):
    if not node:
        return 0
    L_height = height(node.L)
    R_height = height(node.R)
    return max(L_height, R_height) + 1

def level_width(node, level):
    if not node:
        return 0
    if level == 1:
        return 1
    return level_width(node.L, level - 1) + level_width(node.R, level - 1)

def width(node):
    res = 0
    H = height(node)
    for i in range(1, H + 1):
        W = level_width(node, i)
        res = max(res, W)
    return res

def printer_postorder(node):
    if node:
        printer_postorder(node.L)
        printer_postorder(node.R)
        print( hex(node.val)[2:], end=' ')

def printer_preorder(node):
    if node:
        print( hex(node.val)[2:], end=' ')
        printer_preorder(node.L)
        printer_preorder(node.R)

def printer_inorder(node):
    if node:
        printer_inorder(node.L)
        print( hex(node.val)[2:], end=' ')
        printer_inorder(node.R)

printer_inorder( root )
print('root/dec,hex/',root.val,hex(root.val),'end/inorder/')
#printer_preorder( root )
#print('end/preorder/')
#printer_postorder( root )
#print('end/postorder/')

W = width(root)
H = height(root)
res = W * H
print('w/h/res/',W,H,res)
assert res in [ 16, 30784 ]
