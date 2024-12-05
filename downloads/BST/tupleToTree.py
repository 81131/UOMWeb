
class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

treeTuple = ((1,3,None), 2, ((None,3,5),5,(6,7,8)))

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

print(tree2.key)
def parseTree(tree):
    if tree is None:
        return None
    if tree.left is None and tree.right is None:
        return tree.key
    return (parseTree(tree.left), tree.key, parseTree(tree.right))


print(tree2.left.key,  tree2.right.key)
print(parseTree(tree2))