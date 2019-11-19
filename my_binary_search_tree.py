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
"""
binary treeのときはレベル順で来た順に問答無用で追加したが、二分探索木ではルートからスタートして順番に左右振り分けするのがポイント。
行った先にノートが格納されていれば、そこを起点に更に深く進んでいく。
末端にたどり着けばそこで追加する。
上から順に振り分けるのが味噌。
こうすることで左分木の中にルートより大きなものはいなくなる。
逆も真だし、当然どこの部分木を見てもこの法則が維持される。

つまり、探すときは素直に大小関係が合う方向に進むだけだし、最大最小は左端右端となる
"""
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
print(ins.bst_min(ins.root)) # TODO 直す
ins.inoder_traverse(ins.root)

            
