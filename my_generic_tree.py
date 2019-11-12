class Node:
    def __init__(self, data):
        self.data = data
        self.firstchild = None
        self.nextsibling = None

class Generic_tree:
    def __init__(self, node_arr):
        self.root = None

        for i, family in enumerate(node_arr):
            self.insert(i, family)


    def insert(self, i, family):
        if self.root is None:
            self.root = Node(family[0][0])


            temp_node = self.root
            siblings = [contents[1] for contents in family]

            for sibling in siblings:
                temp_node.nextsibling = Node(sibling)
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
                            node.firstchild = Node(child)

                            temp_node = node.firstchild
                            siblings = [contents[1] for contents in family]

                            for sibling in siblings:
                                temp_node.nextsibling = Node(sibling)
                                temp_node = temp_node.nextsibling

                    flag = any(next_queue)

    
    def level_order_traversal(self, node, res= []):

        # 二分木化してしまっているので、レベルは右にいった高さで表現する必要あり
        # 要修正
        # insertも間違っているかも
        
        flag = True
        next_queue = [self.root] #初回のqueueを作成
        level = 1

        print('root', self.root.data)
        while flag:
            temp_queue, next_queue = next_queue, []
            for node in temp_queue:
                if node.nextsibling is not None:
                    print('level',level ,'  nextsibling', node.nextsibling.data)
                    next_queue.append(node.nextsibling)

            for node in temp_queue:
                if node.firstchild is not None:
                    level += 1
                    print('level',level ,'  firstchild', node.firstchild.data)
                    next_queue.append(node.firstchild)

            flag = any(next_queue)

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

ins = Generic_tree(node_arr)

print(ins.level_order_traversal([]))