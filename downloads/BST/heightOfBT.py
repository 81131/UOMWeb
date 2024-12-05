class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

treeTuple = ((1,3,None), 2, ((None,3,4),5,(6,7,8)))

def parse_tuple(data):
    if isinstance(data, tuple) and len(data) == 3:
        node = TreeNode(data[1])
        node.left = parse_tuple(data[0])
        node.right = parse_tuple(data[2])
    elif data is None:
        node = None
    else:
        node = TreeNode(data)
    return node

def calcHeight(node):
    if node is None:
        return 0
    return 1 + max(calcHeight(node.left), calcHeight(node.right))

def calcSize(node):
    if node is None:
        return 0
    return 1 + (calcSize(node.left) + calcSize(node.right))

tree2 = parse_tuple(treeTuple)
print (calcHeight(tree2))
print (calcSize(tree2))
