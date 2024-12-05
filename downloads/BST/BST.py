
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


def removeNone(nums):
    return(x for x in nums if x is not None)

def isBST(tree):
    if tree is None:
        return True, None, None
    isBSTL, minL, maxL = isBST(tree.left)
    isBSTR, minR, maxR = isBST(tree.right)
    isBSTNode = (isBSTL and isBSTR and (maxL is None or tree.key > maxL) and (minR is None or tree.key < minR))
    minKey = min(removeNone([minL, tree.key, minR]))
    maxKey = max(removeNone([maxL, tree.key, maxR]))
    return isBSTNode,  minKey, maxKey

print(isBST(tree2))