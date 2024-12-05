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

tree2 = parse_tuple(treeTuple)

def inorderTraverse(node):
    if node is None:
        return []
    return (inorderTraverse(node.left) + [node.key] + inorderTraverse(node.right))

def preorderTraverse(node):
    if node is None:
        return []
    return([node.key] + preorderTraverse(node.left) + preorderTraverse(node.right))

def postorderTraverse(node):
    if node is None:
        return[]
    return(postorderTraverse(node.left) + postorderTraverse(node.right) + [node.key])
print(inorderTraverse(tree2))
print(preorderTraverse(tree2))
print(postorderTraverse(tree2))