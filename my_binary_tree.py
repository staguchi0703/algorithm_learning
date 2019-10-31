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
            print('try inserting ', inserted_node_data)
            self.insert(inserted_node_data)

    def insert(self, data):     # 挿入の処理（ルート生成　⇒　各ノードの枝を生成）・・・左枝がは現在ノードより小さい値が入る
        if self.root == None:   # ルートノードはtreeの解析の基準となる特別なノードなので.rootとして区別して生成するための場合分け
            print('Root node is ....')
            self.root = Node(data) # Node()インスタンスを生成して代入する
            print(self.root.data)

        else:
            _insert(self.root, data) # クラス外にに定義した再帰関数 。ノードの枝を進んでいく

    ##########################
    #  Tree traversal
    ###############################
    def preoder_traversal(self, node, res):
        if node == None:
            return res
        
        print('queue', node.data)
        res.append(node.data)

        # 前順序で左部分木
        self.preoder_traversal(node.left, res)
        # 前順序で右部分木
        self.preoder_traversal(node.right, res)


    def inoder_traversal(self, node, res):
        if node == None:
            return res

        # 間順序で左部分木
        self.inoder_traversal(node.left, res)

        print('queue', node.data)
        res.append(node.data)


        # 間順序で右部分木
        self.inoder_traversal(node.right, res)


    def postorder_traversal(self, node, res):
        if node == None:
            return res
        
        self.postorder_traversal(node.left, res)
        self.postorder_traversal(node.right, res)
        print(node.data)
        res.append(node.data)


    def level_order_traversal(self, node, res):
        print(node.data)
        res.append(node.data)

        if node.left == None:
            pass
        else:
            if node.left.data <= node.data:
                self.level_order_traversal(node.left, res)
        if node.right == None:
            pass
        else:
            self.level_order_traversal(node.right, res)


# 二分木の問題
class BST_method(BST):
    def __init__(self, arr):
        super().__init__(arr)

    def max_in_binary_tree(self):
        root_val = self.root.data





# BSTクラス内で使用する再帰関数
def _insert(temp_node, data): #とあるノードに対して左枝と右枝へ条件分岐しながら再帰で進んで、treeの末端に到達したらノードを生成する
    if data <= temp_node.data: # 左枝
        if temp_node.left == None: # 末端だったら
            temp_node.left = Node(data) # ノードを生成
            print('insert {} to left branch'.format(temp_node.left.data))
            return
        else:
            _insert(temp_node.left, data) #ノードが占有されていたら、再帰して（.leftを付け足して）進んでいく
    else: #上の処理の右枝版
        if temp_node.right == None:
            temp_node.right = Node(data)
            print('insert {} to right branch'.format(temp_node.right.data))
            return
        else:
            _insert(temp_node.right, data)



ins = BST([24,12,3, 5,14,5,16,7,8, 11, 99])


# TODO 探索の方法を確認して実装する
print('--------------------------')
print('start preoder traversal')
ins.preoder_traversal(ins.root, [])

print('--------------------------')
print('start inoder traversal')
ins.inoder_traversal(ins.root, [])

print('--------------------------')
print('start postoder traversal')
ins.postorder_traversal(ins.root, [])

print('--------------------------')
print('start level order traversal')
ins.level_order_traversal(ins.root, [])

