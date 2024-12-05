class user:
    def __init__(self, username, Fname, email):
        self.username = username
        self.Fname = Fname
        self.email = email
        self.left = None
        self.right = None
        
    def insert(tree, username, Fname, email):
        if tree is None:
            return user(username, Fname, email)
        elif (tree.username > username):
            tree.left = user.insert(tree.left, username, Fname,email)
        elif (tree.username < username):
            tree.right = user.insert(tree.right,username, Fname, email)
        return tree
tree = user('dinidu',"Dinindu Vishwajith", "dinindu1919@gmail.com" )
user.insert(tree, "akash", "Akash Silva", "aks@gmail.com")
user.insert (tree, "manee", "Maneesha Alviz", "mnsh@gmail.com")
print(tree.left.username)
print(tree.right.username)