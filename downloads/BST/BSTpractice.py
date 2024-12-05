class user:
    def __init__(self, username, fullName, Email):
        self.username = username
        self.fullname = fullName
        self.email = Email
        
    def __repr__(self, username, fullName, Email):
        return "Username: {}\n,Full Name: {}\n,Email: {}\n, ".format(username, fullName, Email)

def removeNone(tree):
    return (x for x in tree if x is not None)
def isBST(tree):
    if tree is None:
        return True, None, None
    isBSTL, minL, maxL = isBST(tree.left)
    isBSTR, minR, maxR = isBST(tree.right)
    
    isBSTNode = (isBSTL and isBSTR and (maxL is None or maxL > tree.username > maxL) and (minR is None or minR < tree.username))
    
    minKey = min(removeNone([minL,tree.username, minR]))
    maxKey = max(removeNone([maxL,tree.username, maxR]))
    
    return isBSTNode, minKey, maxKey
        
def insert(tree, username, fullname, Email):
    if tree is None:
        return user(username, fullname, Email)
    elif username > tree.username:
        tree.left = insert(tree.left, username, fullname, Email)
    elif username < tree.username:
        tree.right = insert(tree.right, username, fullname, Email)
    return tree

def makeBalancedBST(data, lo = 0, hi = None):
    if hi is None:
        hi = len(data) - 1
    if lo > hi:
        return None
    mid = lo + hi //2
    username, fullname, Email = data[mid]
    
    root = user(username, fullname, Email)
    root.left = makeBalancedBST(data, lo, mid-1, hi)
    root.right = makeBalancedBST(data, mid+1, hi, root)
    
    return root
        