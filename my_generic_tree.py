
class Generic_tree_Node:
    def __init__(self, data):
        # inorder thread binary tree
        self.data = data
        self.nextsibling = None
        self.firstchild = None


class Generic_tree:
    def __init__(self, node_arr):
        self.root = None
        
        for i, family in enumerate(node_arr):
            print('try to insert', family, 'in step ', i)
            self.insert(i, family)


    def insert(self, i, family):
        if self.root is None:
            print('make root node')
            self.root = Generic_tree_Node(family[0][0])
            print('make first child　which is {} for root'.format(family[0][1]))
            self.root.firstchild = Generic_tree_Node(family[0][1])

            temp_node = self.root.firstchild
            siblings = [contents[1] for contents in family[1:]] #family のfirstchildはsiblingから除く

            print('insert siblings to root.firstchild')
            for sibling in siblings:
                temp_node.nextsibling = Generic_tree_Node(sibling)
                temp_node = temp_node.nextsibling
            print('------------------------------')

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
                            # print('insert siblings to ', node.data, 'for making queue')
                            next_queue.append(node.nextsibling)
                            
                        if node.firstchild is not None:
                            # print('insert firstchild to ', node.data, 'for making queue')
                            next_queue.append(node.firstchild)

                        if node.data == pairent:
                            print('when you find {} which is pairent, insert '.format(node.data), child, ' as firstchild.')
                            node.firstchild = Generic_tree_Node(child)
                            temp_node = node.firstchild

                            print('insert siblings to ', node.data, '.')
                            siblings = [contents[1] for contents in family[1:]] #family のfirstchildはsiblingから除く
                            for sibling in siblings:
                                temp_node.nextsibling = Generic_tree_Node(sibling)
                                temp_node = temp_node.nextsibling
                            print('------------------------------')

                    if len(next_queue) == 0:
                        flag = None
                

    def inorder_traverse(self, node):

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
            [[6, 7], [6, 8], [6, 12], [6, 13], [6, 14]],
            [[8, 15]],
            [[11, 16], [11, 17]]
]

ins_generic = Generic_tree(node_arr)

print(ins_generic.root.data)
ins_generic.inorder_traverse(ins_generic.root.firstchild)