# generic tree
# --> threaded binary tree


class Generic_tree_Node:
    def __init__(self, data):
        # inorder thread binary tree
        self.data = data
        self.firstchild = None
        self.nextsibling = None

# class Threaded_binary_tree_Node:
#     def __init__(self, data):
#         # inorder thread binary tree
#         self.data = data
#         self.firstchild_flag = 0    #thread
#         self.firstchild = None
#         self.nextsibling_flag = 0   #thread
#         self.nextsibling = None


class Generic_tree:
    def __init__(self, node_arr):
        self.root = None
        
        for i, family in enumerate(node_arr):
            self.insert(i, family)


    def insert(self, i, family):
        if self.root is None:
            self.root = Generic_tree_Node(family[0][0])
            self.root.firstchild = Generic_tree_Node(family[0][1])

            temp_node = self.root.firstchild
            siblings = [contents[1] for contents in family]

            for sibling in siblings:
                temp_node.nextsibling = Generic_tree_Node(sibling)
                temp_node = temp_node.nextsibling

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
                            node.firstchild = Generic_tree_Node(child)
                            temp_node = node.firstchild
                            siblings = [contents[1] for contents in family]

                            for sibling in siblings:
                                temp_node.nextsibling = Generic_tree_Node(sibling)
                                temp_node = temp_node.nextsibling

                    if len(next_queue) >= 1:
                        flag = None
                

    def inorder_traverse(self, node):

        # 二分木化してしまっているので、レベルは右にいった高さで表現する必要あり
        # これを上手く扱う方法としてスレッド二分木を使用する

        # 走査の終了条件
        if node is None:
            return

        self.inorder_traverse(node.nextsibling)
        print(node.data)
        self.inorder_traverse(node.firstchild)




            
#####
node_arr =[
            [[1, 2], [1, 3], [1, 4], [1, 5],[1, 6]],
            [[4, 9]],
            [[5, 10], [5, 11]],
            [[6, 12], [6, 13], [6, 14]],
            [[8, 15]],
            [[11, 16], [11, 17]]
]

ins_generic = Generic_tree(node_arr)

print(ins_generic.root.data)
ins_generic.inorder_traverse(ins_generic.root.firstchild)