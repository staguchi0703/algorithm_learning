# heapをpythonで実装してみた
## 目的
* アルゴリズムの学習のためheapをフルスクラッチする
* heapから最小値を取り出すメソッドを実装する
* heapを用いてheap sortを実装する

## 方針
* 一次元リストにヒープ構造のデータを格納する
    * 親子の関係性はindex(親)に対して 2*index + 1(子１)と2*index + 2(子２)である
    * とあるindexの親nodeは(index -1) //2である。
    * 親子ノードの値の大小関係は親値　＜　子値　とする（昇順）。
    * 故にルートは最小値をとる
* データの追加は最後尾に行い、percolate upでヒープ性を再構築する
* データの取り出し（最小値）はルート（index = 0）から取りだし、percolate downでヒープ性を再構築する
    * 親に対して子は二つあるので、downのほうが条件分岐が複雑になるので注意
    * 残りデータ数がN=1になるとめんどくさいので例外的に処理する
* ヒープソートは順番に取り出すだけ 

## 実装

``` python
def swap(arr, i , j):
    arr[i], arr[j] = arr[j], arr[i]
    return arr

class heap():
    """先頭が一番小さい昇順ヒープの実装"""

    def __init__(self, arr):
        self.list = []
        
        for num in arr:
            self.insert(num)

    def percolate_up(self):
        index = len(self.list) - 1
        while index != 0 and self.list[index] < self.list[(index - 1) // 2]:
            """ 一次元化されたヒープにおいて、あるindexの親ノードの位置は(index - 1) //2 """
            self.list = swap(self.list, index, (index -1)//2)
            index = (index-1)//2


    def insert(self, item):
        self.list.append(item)
        self.percolate_up()

    def percolate_down(self):
        if len(self.list) == 2:
            if self.list[0] > self.list[1]:
                self.list = swap(self.list, 0, 1)

        index = 0

        while (2*index + 2 <= len(self.list)-1):
            child_left_index = 2*index + 1
            child_right_index = 2*index + 2
            child_left = self.list[child_left_index]
            child_right = self.list[child_right_index]

            if self.list[index] > min(child_left, child_right):
                if child_left < child_right:
                    swap(self.list, index, child_left_index)
                    index = child_left_index 
                else:
                    self.list =swap(self.list, index, child_right_index)
                    index = child_right_index

    def pop_min(self):
        if len(self.list) == 1:
            return self.list[0]

        res = self.list[0]
        self.list[0] = self.list.pop(-1) 
        """
        最も子のノードのうちの最後の値を取り出して削除pop(-1)
        根にもってくるために値を代入　list[0] = pop(-1)
        pop(0)で根をとるとリストのindexがずれてヒープの形状が崩れるため、根をとるときは[0]
        list[0]は削除だから、pop(-1)で得た必ず子になる要素を入れて形を整える
        insertの時に使ったヒープ化処理と異なり、逆からたどる処理percolate_downを実行しヒープ性（heapify）を維持する
        """
        self.percolate_down()

        return res

    def sort(self):
        """ヒープソートを実装する"""
        temp_list = self.list
        return [self.pop_min() for _ in range(len(temp_list))]

```

[Git_hub](https://github.com/staguchi0703/algorithm_learning)


## 動作確認
``` python
my_list = [3, 1, 88, 15, 2, 61, 17, 2, 2, 18, 21]
print('my initial list >>>', my_list)

my_heap = heap(my_list)
print('insert 100 to heap')
my_heap.insert(100)
print('add 100 to heap >>>', my_heap.list)

res = my_heap.pop_min()
print('pop_min > ', res)
print('heap sort >>>', my_heap.sort())

```

``` out
my initial list >>> [3, 1, 88, 15, 2, 61, 17, 2, 2, 18, 21]
insert 100 to heap
add 100 to heap >>> [1, 2, 17, 2, 3, 88, 61, 15, 2, 18, 21, 100]
pop_min >  1
heap sort >>> [2, 2, 2, 3, 15, 17, 18, 21, 61, 88, 100]
```
## 感想
できたーーーー！　うれC！
次は二分探索でもやろうかしら・・・
以下の点が混乱しやすく何度も間違えていた。雰囲気はなんとなくわかったが白紙からもう一回やろうとすると同じと事で躓きそう。

* 親子indexの関係
* indexとnodeの値を取り違えていた
* whileの終了条件

## 参考
[入門　データ構造とアルゴリズム（オライリー社）](https://www.oreilly.co.jp/books/9784873116341/)
