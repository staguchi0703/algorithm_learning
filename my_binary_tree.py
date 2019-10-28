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
            return

        else:
            while True:
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
    

ins = BST([24,12,35,14,5,16,7])
ins_root = ins.root

def viewer(ins_root):
    try:
        temp_data = ins_root.data
        print(temp_data)
    except AttributeError:
        
        return

    return viewer(ins_root.left)

# TODO 探索の方法を確認して実装する

viewer(ins_root)
