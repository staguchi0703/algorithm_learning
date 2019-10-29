# %%
class Node:
    """ user difine data structure Node """
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
# %%
class BST:
    """ user difine data structure BST """
    def __init__(self, arr):
        self.root = None

        for inserted_node_data in arr:
            self.insert(inserted_node_data)

    def insert(self, data):
        temp_node = self.root
        if self.root == None:
            self.root = Node(data)

        else:
            while temp_node:
                temp_node_val = temp_node.data
                if data < temp_node_val:
                    if temp_node.left is None:
                        temp_node.left = Node(data)
                        return 

                    temp_node = temp_node.left


                elif data > temp_node_val:
                    if temp_node.right is None:
                        temp_node.right = Node(data)
                        return
                    
                    temp_node = temp_node.right

                else:
                    temp_node.data = data
                    return

    ###########################
    #
    #  Tree traversal
    #
    ###############################
    def preoder_traversal(self, node, res):
        if node == None:
            return res
        
        print('stack', node.data)
        res.append(node.data)

        # 前順序で左部分木
        self.preoder_traversal(node.left, res)
        # 前順序で右部分木
        self.preoder_traversal(node.right, res)


ins = BST([24,12,3, 5,14,5,16,7,8, 11, 99])
ins_root = ins.root

def left_wing_viewer(ins_root):
    try:
        temp_data = ins_root.data
        print(temp_data)
    except AttributeError:
        return

    return left_wing_viewer(ins_root.left)



# TODO 探索の方法を確認して実装する

res = ins.preoder_traversal(ins.root, [])
print(res)
