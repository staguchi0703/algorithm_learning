# generic tree
# --> threaded binary tree


class Threaded_binary_tree_Node:
    def __init__(self, data):
        # inorder thread binary tree
        self.data = data
        self.firstchild_flag = 0    #thread
        self.firstchild = None
        self.nextsibling_flag = 0   #thread
        self.nextsibling = None


class Threaded_binary_tree:
    def __init__(self, node_arr):
        self.root = None

        # dummy nodeの追加
        self.dummy_node = Threaded_binary_tree_Node('Null')
        self.dummy_node.nextsibling = self.root
        self.dummy_node.nextsibling_flag = 1
        self.dummy_node.firstchild = self.dummy_node
        self.dummy_node.firstchild_flag = 1
        
        for i, family in enumerate(node_arr):
            self.insert(i, family)


    def insert(self, i, family):
        if self.root is None:
            self.root = Threaded_binary_tree_Node(family[0][0])
            self.root.firstchild = Threaded_binary_tree_Node(family[0][1])
            self.root.firstchild_flag = 1


            temp_node = self.root.firstchild
            siblings = [contents[1] for contents in family]

            for sibling in siblings:
                temp_node.nextsibling = Threaded_binary_tree_Node(sibling)
                temp_node.nextsibling_flag = 1
                temp_node = temp_node.nextsibling
            else:
                temp_node = self.dummy_node


        else:
            if i >=1:
                pairent = family[0][0]
                child = family[0][1]
                

                flag = True
                next_queue = [self.root] #初回のqueueを作成
                while flag:
                    temp_queue, next_queue = next_queue, []
                    for node in temp_queue:
                        if node.nextsibling is not None:
                            next_queue.append(node.nextsibling)
                            
                        if node.firstchild is not None:
                            next_queue.append(node.firstchild)
                        if node.data == pairent:
                            node.firstchild = Threaded_binary_tree_Node(child)
                            node.firstchild_flag = 1
                            temp_node = node.firstchild
                            siblings = [contents[1] for contents in family]

                            for sibling in siblings:
                                temp_node.nextsibling = Threaded_binary_tree_Node(sibling)
                                temp_node = temp_node.nextsibling

                    if len(next_queue) >= 1:
                        flag = None
                
                # temp_queue[-1].firstchild = self.dummy_node

    def inorder_successor(self, node):
        """ 
        とあるnodeのinorder traverse時の後nodeを探す
        """
        if node.nextsibling_flag == 0:
            return node.nextsibling

        else: # node.nextsibling_flag == 1: 
            position = node.nextsibling
            while position.firstchild_flag == 1:
                position = position.firstchild

            return position



    def traverse(self, node):

        # 二分木化してしまっているので、レベルは右にいった高さで表現する必要あり
        # これを上手く扱う方法としてスレッド二分木を使用する

        # 走査の終了条件
        flag = True
        while node:
            temp_node = self.inorder_successor(node) 

            if temp_node:
                print(temp_node.data, temp_node.nextsibling_flag, temp_node.firstchild_flag)

            node = temp_node

        return




            
#####
node_arr =[
            [[1, 2], [1, 3], [1, 4], [1, 5],[1, 6]],
            [[4, 9]],
            [[5, 10], [5, 11]],
            [[6, 12], [6, 13], [6, 14]],
            [[8, 15]],
            [[11, 16], [11, 17]]
]

ins_generic = Threaded_binary_tree(node_arr)

print(ins_generic.root.data)
ins_generic.traverse(ins_generic.root.firstchild)