class rootSystem:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

node0 = rootSystem(2)
node1 = rootSystem(3)
node2 = rootSystem(1)
node3 = rootSystem(5)
node4 = rootSystem(3)
node5 = rootSystem(4)
node6 = rootSystem(7)
node7 = rootSystem(6)
node8 = rootSystem(8)

node0.left = node1
node1.left = node2
node0.right = node3
node3.left = node4
node4.right = node5
node3.right = node6
node6.left = node7
node7.right = node8