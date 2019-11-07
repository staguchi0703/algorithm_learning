# %%
class Node:
    """ Node is user difine data structure. It is binary tree  """
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
# %%
class BST:
    """ user difine data structure BST """
    def __init__(self, arr):
        self.root = None # 今後の処理の基準にするために空のrootを作成する

        for inserted_node_data in arr: #リストに格納されているノードの値を順次挿入する処理
            print('....')
            print('try inserting ', inserted_node_data)
            self.insert(inserted_node_data)

    def insert(self, data):     # 挿入の処理（ルート生成　⇒　各ノードの枝を生成）・・・左枝がは現在ノードより小さい値が入る
        if self.root == None:   # ルートノードはtreeの解析の基準となる特別なノードなので.rootとして区別して生成するための場合分け
            print('Root node is ....')
            self.root = Node(data) # Node()インスタンスを生成して代入する
            print(self.root.data)
            
        else:
            flag = True
            queue = [self.root]
            level = 1
            while flag:
                level += 1
                temp_list, queue = queue, []

                for i, node in enumerate(temp_list):
                    
                    if node.left is not None:
                        queue.append(node.left)
                    if node.right is not None:
                        queue.append(node.right)

                    if node.left is None:
                        node.left = Node(data)
                        queue.append(node.left)
                        print('inseting level {}'.format(level))
                        print('inserting {}th block'.format(i))
                        flag = False

                    elif node.right is None:
                        node.right = Node(data)
                        queue.append(node.right)
                        print('inseting level {}'.format(level))
                        print('inserting {}th block'.format(i))
                        flag = False
                    else:
                        if not any(queue):
                            temp_list[0].left = Node(data)
                            print('inseting level {}'.format(level))
                            print('inserting {}th block'.format(0))
                            flag = False
                # insertを要修正　for loop中のinsertする場所がおかしい




    ##########################
    #  Tree traversal
    ###############################
    def preoder_traversal(self, node, res):
        if node != None:
            print('queue', node.data)
            res.append(node.data)

            # 前順序で左部分木
            self.preoder_traversal(node.left, res)
            # 前順序で右部分木
            self.preoder_traversal(node.right, res)

        return res

    def inoder_traversal(self, node, res):
        if node != None:
                
            # 間順序で左部分木
            self.inoder_traversal(node.left, res)

            print('queue', node.data)
            res.append(node.data)


            # 間順序で右部分木
            self.inoder_traversal(node.right, res)
        return res

    def postorder_traversal(self, node, res):
        if node != None:
        
            self.postorder_traversal(node.left, res)
            self.postorder_traversal(node.right, res)
            print('queue', node.data)
            res.append(node.data)
        return res

    def level_order_traversal(self, queue, res= []):

        if queue == [] :
            # it's root
            print('root', self.root.data)
            res.append(self.root.data)
            queue.append(self.root)

        else:
            # このlevelのノード は引数のqueueだからforで回す
            temp_list, queue = queue, []
            not_none_cnt = 0

            for item in temp_list:
                if item.left is not None:
                    res.append(item.left.data)
                    print(item.left.data)
                    queue.append(item.left)
                    not_none_cnt += 1

                if item.right is not None:
                    res.append(item.right.data)
                    print(item.right.data)
                    queue.append(item.right)
                    not_none_cnt += 1
            
            if not_none_cnt == 0:
                return #最後にこの関数を呼び出したところに戻る
            
        self.level_order_traversal(queue, res)

        return res



# 二分木の問題
class BT_method(BST):
    def __init__(self, arr):
        super().__init__(arr)

    def max_in_binary_tree(self, node, temp_max):
        """実装は親と子の関係で最大値を示す
        traversしながらLIFOして、大きい値を残していっても同じ。
        順探索でtraversしながら最大値を覚えておくのと同じこと"""
        if node is not None:
            temp_root_val = node.data
            left_val = self.max_in_binary_tree(node.left, temp_max)
            right_val = self.max_in_binary_tree(node.right, temp_max)

            temp_max = max(temp_root_val, left_val, right_val, temp_max)

        return temp_max

    def find_val(self, node, val, flag=False):
        if node != None:
            if node.data == val:
                return True

            else:
                flag_left = self.find_val(node.left, val) #再帰の結果をreturnで返しているので変数で受け取る
                flag_right = self.find_val(node.right, val)
            
                if flag_left or flag_right:
                    return True

        return False


    def size(self, node):
        if node is None: #nodeがNoneのところで数え上げを終了
            return 0 #0を返せば数え上げされない
        else:
            left_cnt = self.size(node.left)
            right_cnt = self.size(node.right)

            return 1 + left_cnt + right_cnt #自分（not None）が１と左右木中の数（仮想の探索を再帰関数で実現）


    def hight(self, level=0):
        flag = True
        queue = [self.root]

        while flag:
            level += 1
            temp_list, queue = queue, []
            for node in temp_list:
                if node.left is not None:
                    queue.append(node.left)
                if node.right is not None:
                    queue.append(node.right)


            flag = any(queue)

        return level




    # def highest_node(self, queue=[]):

    #     if queue == [] :
    #         queue.append(self.root)

    #     else:
    #         # このlevelのノード は引数のqueueだからforで回す
    #         temp_list , queue = queue, []
    #         not_none_cnt = 0

    #         for item in temp_list:
    #             if item.left is not None:
    #                 queue.append(item.left)
    #                 not_none_cnt += 1

    #             if item.right is not None:
    #                 queue.append(item.right)
    #                 not_none_cnt += 1
            
    #         if not_none_cnt == 0:
    #             return
            
    #     self.highest_node(queue)
    #     return 

# ins = BST(range(1,16))


# # TODO 探索の方法を確認して実装する
# print('--------------------------')
# print('start preoder traversal')
# print(ins.preoder_traversal(ins.root, []))

# print('--------------------------')
# print('start inoder traversal')
# print(ins.inoder_traversal(ins.root, []))

# print('--------------------------')
# print('start postoder traversal')
# print(ins.postorder_traversal(ins.root, []))

# print('--------------------------')
# print('start level order traversal')
# print(ins.level_order_traversal([]))

# # 二分木の問題6.6.7
# print('=====================================')

ins2 = BT_method(range(1,7))
# print('--------------------------')
# print('find max')
# print(ins2.max_in_binary_tree(ins2.root, 0))
# print('--------------------------')
# print('find value')
# print('looking for 7', ins2.find_val(ins2.root, 7))
# print('looking for 17', ins2.find_val(ins2.root, 17))


#6-6 search size
# print('--------------------------')
# print('detect node size')
# print(ins2.size(ins2.root))

#6-10 search hight
print('--------------------------')
print('detect node hight')
print(ins2.hight())

#6-12 highest node
# print('--------------------------')
# print('detect highest node')
# print(ins2.highest_node())



# 次は6.7N分木
# 次は6.112分探索木