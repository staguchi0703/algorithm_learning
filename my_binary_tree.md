# 二分木を理解するために
## 二分木とは
木構造を有する非線形データ構造の一種である。

木ADTでは要素の順序は考慮しない。

二分木はどのノードも子を0から2個有す。よって、ルートとルートより左に展開する左部分木と、右に展開する右部分木で一般に可視化できる。

[Wiki pedia による二分木の解説](https://ja.wikipedia.org/wiki/%E6%9C%A8%E6%A7%8B%E9%80%A0_(%E3%83%87%E3%83%BC%E3%82%BF%E6%A7%8B%E9%80%A0))

![二分木の図解](https://upload.wikimedia.org/wikipedia/commons/thumb/6/67/Sorted_binary_tree.svg/250px-Sorted_binary_tree.svg.png)

## 目的
* 二分木を学ぶことで、データ構造とアルゴリズムに対する理解を深めたい。
* pythonで二分木データ構造を実装する。
* 単に二分木を実装するだけではなく、二分木データ構造の取り扱いかたのハウツーを理解する。
* * 二分探索木の理解を深めるため基礎となる二分木を深堀する　⇒　[親記事](https://qiita.com/tagtagtag/items/0e04c584f17ebfb7afbb)

## 内容
### データ構造とノードの定義
* ノードは値をもつ（`node.data`）
* 子ノードへの接続を持つ（`node.left = Node(data)`）
* 子の数は0, 1, 2個のいずれかである
* 最上位のノードはルートノード（`self.root, ins.root`）である
  
### 二分木実装
#### Node()オブジェクトの生成

Nodeオブジェクトを生成し、コンストラクタで下記を生成しする。
生成時には他との関係がないので.left, .right もNone

* ノードの値：　`self.data = data`
* 左部分木の子ノードへのリンク: `self.left = None`
* 右部分木の子ノードへのリンク: `self.right = None`

```pthon3 Node_class.py
class Node:
    """ Node is user data structure　as binary tree  """
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
```



#### 二分木の生成
1. Nodeオブジェクトを生成する
1. 子に要素がない部分を探して、Nodeを挿入する。
1. Nodeを横断（traversal）するメソッドは訪問する順番を考慮し、複数有す。

##### 実装時のポイント
* コンストラクタでroot nodeを作成する。
* コンストラクタに、値を挿入する関数を登場させる。
* 上記の実装はインスタンスメソッドとして後ろに登場して定義される
* メソッド中のwhile内からメソッドを抜けたいときは、returnで終わらせる


``` python 
class BinaryTree:
    """ user difine data structure BinaryTree """
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
            level = 1
            flag = True
            next_queue = [self.root] #初回のqueueを作成
            while flag:   #flagは要素が全てNoneのときFalseになる
                temp_queue, next_queue = next_queue, []
                level += 1

                for node in temp_queue:
                    # 左分木
                    # 現在nodeのchiled nodeを次回操作のqueueに加えていく
                    if node.left is not None:
                        next_queue.append(node.left)
                    # child nodeにNoneが見つかったときには新たにdataを使ってnodeを生成する
                    else:
                        node.left = Node(data)
                        print('In level {}, {} is inseted'.format(level, data))
                        """
                        （AA）
                        dataをnodeに追加したらこの回のinsertは終了する
                        ここはfor < while < insert methodの中なのでreturnを使って一発でメソッドを終了させる 
                        """
                        return 

                    # 右分木
                    # 現在nodeのchiled nodeを次回操作のqueueに加えていく
                    if node.right is not None:
                        next_queue.append(node.right)
                    # child nodeにNoneが見つかったときには新たにdataを使ってnodeを生成する
                    else:
                        node.right = Node(data)
                        print('In level {}, {} is inseted'.format(level, data))
                        """
                        （AA）参照
                        """
                        return

                flag = any(next_queue)

    ##########################
    #  Tree traversal
    ##########################
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
                    print('queue', item.left.data)
                    queue.append(item.left)
                    not_none_cnt += 1

                if item.right is not None:
                    res.append(item.right.data)
                    print('queue', item.right.data)
                    queue.append(item.right)
                    not_none_cnt += 1

            if not_none_cnt == 0:
                return #最後にこの関数を呼び出したところに戻る

        self.level_order_traversal(queue, res)

        return res

```

#### 二分木のメソッド

最大値の探索、値の有無を探索、サイズの調査、高さの調査を行うメソッドを実装した。
ポイントはコード中のコメントを参照されたい。

``` python
# 二分木のメソッド
class BT_method(BinaryTree):
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
```

### 実行

下記のようにコードを実行した。


```python

ins = BinaryTree(range(1,16))

print('--------------------------')
print('start preoder traversal')
print(ins.preoder_traversal(ins.root, []))

print('--------------------------')
print('start inoder traversal')
print(ins.inoder_traversal(ins.root, []))

print('--------------------------')
print('start postoder traversal')
print(ins.postorder_traversal(ins.root, []))

print('--------------------------')
print('start level order traversal')
print(ins.level_order_traversal([]))

#
print('=====================================')

ins2 = BT_method(range(1,16))
print('--------------------------')
print('find max')
print(ins2.max_in_binary_tree(ins2.root, 0))
print('--------------------------')
print('find value')
print('looking for 7', ins2.find_val(ins2.root, 7))
print('looking for 17', ins2.find_val(ins2.root, 17))


#  search size
print('--------------------------')
print('detect node size')
print(ins2.size(ins2.root))

```




### 実行結果

print分が逐次挙動を教えてくれています

```
....
try inserting  1
Root node is ....
1
....
try inserting  2
In level 2, 2 is inseted
....
try inserting  3
In level 2, 3 is inseted
....
try inserting  4
In level 3, 4 is inseted
....
try inserting  5
In level 3, 5 is inseted
....
try inserting  6
In level 3, 6 is inseted
....
try inserting  7
In level 3, 7 is inseted
....
try inserting  8
In level 4, 8 is inseted
....
try inserting  9
In level 4, 9 is inseted
....
try inserting  10
In level 4, 10 is inseted
....
try inserting  11
In level 4, 11 is inseted
....
try inserting  12
In level 4, 12 is inseted
....
try inserting  13
In level 4, 13 is inseted
....
try inserting  14
In level 4, 14 is inseted
....
try inserting  15
In level 4, 15 is inseted
--------------------------
start preoder traversal
queue 1
queue 2
queue 4
queue 8
queue 9
queue 5
queue 10
queue 11
queue 3
queue 6
queue 12
queue 13
queue 7
queue 14
queue 15
[1, 2, 4, 8, 9, 5, 10, 11, 3, 6, 12, 13, 7, 14, 15]
--------------------------
start inoder traversal
queue 8
queue 4
queue 9
queue 2
queue 10
queue 5
queue 11
queue 1
queue 12
queue 6
queue 13
queue 3
queue 14
queue 7
queue 15
[8, 4, 9, 2, 10, 5, 11, 1, 12, 6, 13, 3, 14, 7, 15]
--------------------------
start postoder traversal
queue 8
queue 9
queue 4
queue 10
queue 11
queue 5
queue 2
queue 12
queue 13
queue 6
queue 14
queue 15
queue 7
queue 3
queue 1
[8, 9, 4, 10, 11, 5, 2, 12, 13, 6, 14, 15, 7, 3, 1]
--------------------------
start level order traversal
root 1
queue 2
queue 3
queue 4
queue 5
queue 6
queue 7
queue 8
queue 9
queue 10
queue 11
queue 12
queue 13
queue 14
queue 15
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
=====================================
....
try inserting  1
Root node is ....
1
....
try inserting  2
In level 2, 2 is inseted
....
try inserting  3
In level 2, 3 is inseted
....
try inserting  4
In level 3, 4 is inseted
....
try inserting  5
In level 3, 5 is inseted
....
try inserting  6
In level 3, 6 is inseted
....
try inserting  7
In level 3, 7 is inseted
....
try inserting  8
In level 4, 8 is inseted
....
try inserting  9
In level 4, 9 is inseted
....
try inserting  10
In level 4, 10 is inseted
....
try inserting  11
In level 4, 11 is inseted
....
try inserting  12
In level 4, 12 is inseted
....
try inserting  13
In level 4, 13 is inseted
....
try inserting  14
In level 4, 14 is inseted
....
try inserting  15
In level 4, 15 is inseted
--------------------------
find max
15
--------------------------
find value
looking for 7 True
looking for 17 False
--------------------------
detect node size
15

```

## 参考文献
+ [入門　データ構造とアルゴリズム（オライリー社）](https://www.oreilly.co.jp/books/9784873116341/)
+ [Wiki pedia による二分木の解説](https://ja.wikipedia.org/wiki/%E6%9C%A8%E6%A7%8B%E9%80%A0_(%E3%83%87%E3%83%BC%E3%82%BF%E6%A7%8B%E9%80%A0))
