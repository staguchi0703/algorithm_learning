class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BST:
    def __init__(self, arr):
        self.root = None

        for val in arr:
            self.insert(val)
    
    def insert(self, val):
        if self.root is None:
            self.root = Node(val)

        else:
            flag = True
            temp_queue = []
            next_queue= [self.root]
            level = 1

            while flag:
                temp_queue, next_queue = next_queue, []
                level += 1

                for node in temp_queue:
                    if node.left is not None:
                        next_queue.append(node.left)
                    else:
                        if node.data > val:
                            node.left = Node(val)
                            return 

                    if node.right is not None:
                        next_queue.append(node.right)
                    else:
                        if node.data < val:
                            node.right = Node(val)
                            return

                    flag = any(next_queue)
                    level += 1

    def find(self, node, val):
        if node is not None:
            if node.data == val:
                return True

            else:
                flag_left = self.find(node.left, val) 
                flag_right = self.find(node.right, val)
            
                if flag_left or flag_right:
                    return True

        return False

    def bst_min(self, node):
        if node.left is None:
            return node
        else:
            self.bst_min(node.left)

        return node.data

    def inoder_traverse(self, node):
        if node is not None:
            self.inoder_traverse(node.left)
            print(node.data)
            self.inoder_traverse(node.right)


import random

arr = [random.randint(1, 100) for _ in range(12)]
ins = BST(arr)
print(arr)
print(ins.find(ins.root, 4))
print(ins.bst_min(ins.root))
ins.inoder_traverse(ins.root)

            