class Generic_tree_Node:
    def __init__(self, data):
        self.data = data
        self.firstchild = None
        self.firstchild_flag = 1
        self.nextsibling = None
        self.nextsibling_flag = 1

class Generic_tree:
    def __init__(self, node_arr):
        self.root = None

        for i, family in enumerate(node_arr):
            self.insert(i, family)


    def insert(self, i, family):
        if self.root is None:
            self.root = Generic_tree_Node(family[0][0])


            temp_node = self.root
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

                    flag = any(next_queue)

    
    def thread_binary_tree(self, node, res= []):

        # 二分木化してしまっているので、レベルは右にいった高さで表現する必要あり
        # これを上手く扱う方法としてスレッド二分木を使用する

        # dummy nodeの追加
        self.dummy_node = Generic_tree_Node('Null')
        self.dummy_node.nextsibling = self.root
        # https://yottagin.com/?p=3423
        self.dummy_node.firstchild = self.dummy_node.firstchild

        # 走査の終了条件
        if node is None:
            return
        
        res.append(node.data)

        if node.nextsibling is not None:
            self.thread_binary_tree(node.nextsibling, res)
        else:
            return

        if node.firstchild is None:
            self.thread_binary_tree(node.nextsibling, res)
            self.thread_binary_tree(node.firstchild, res)    
        else:
            return

        return res


            
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

print(ins_generic.thread_binary_tree(ins_generic.root))