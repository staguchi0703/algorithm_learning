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
            print(node.data)
            res.append(node.data)
        return res

    def level_order_traversal(self, node, res, level = 0):

        if node is self.root :
            # it's root
            print(node.data)
            res.append(node.data)
            level += 1
            upper_node_list = [self.root]

            if level != 0:
                raise ValueError('Inital node is geven as root. But level you set isn\'t 0.')
        else:
            # ここをどうやって再帰するか考えられていない
            upper_node_list = []
            # このlevelのノードを書き出す
            for item in upper_node_list:
                print(item.left)
                res.append(item.left)
                upper_node_list.append(item.left)
                print(item.right)
                res.append(item.right)
                upper_node_list.append(item.right)

        return res

# 二分木の問題
class BT_method(BST):
    def __init__(self, arr):
        super().__init__(arr)

    def max_in_binary_tree(self):
        root_val = self.root.data





# BSTクラス内で使用する再帰関数
# 与えられたの順にノードに追加していく
def _insert(temp_node, data): #とあるノードに対して左枝と右枝へ条件分岐しながら再帰で進んで、treeの末端に到達したらノードを生成する
    if temp_node.left != None:
        if temp_node.right != None:
            _insert(temp_node.left, data)
        else:
            print('inserting to right')
            temp_node.right = Node(data)
    else:
        print('inserting to left')
        temp_node.left = Node(data)


ins = BST(range(1,16))


# TODO 探索の方法を確認して実装する
print('--------------------------')
print('start preoder traversal')
print(ins.preoder_traversal(ins.root, []))

print('--------------------------')
print('start inoder traversal')
ins.inoder_traversal(ins.root, [])

print('--------------------------')
print('start postoder traversal')
ins.postorder_traversal(ins.root, [])

print('--------------------------')
print('start level order traversal')
ins.level_order_traversal(ins.root, [])

