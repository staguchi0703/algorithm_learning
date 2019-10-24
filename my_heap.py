# %%
import random


#%%
def swap(arr, i , j):
    arr[i], arr[j] = arr[j], arr[i]
    return arr

#%%
class heap():
    """先頭が一番小さい昇順ヒープの実装"""

    def __init__(self, arr):
        self.list = []
        
        for num in arr:
            self.insert(num)

    def percolate_up(self):
        index = len(self.list) - 1
        while index != 0 and self.list[index] < self.list[(index - 1) // 2]:
            """ 一次元化されたヒープのindexの親ノードの位置は(index - 1) //2 """
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
        while 2*index + 2 < len(self.list):
            if self.list[index] > min(self.list[2*index + 1], self.list[2*index + 2]):
                if self.list[2*index + 1] < self.list[2*index + 2]:
                    swap(self.list, index, 2*index +1)
                    index = 2*index + 1
                else:
                    swap(self.list, index, 2*index + 2)
                    index = 2*index + 2

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
        insertの時に使ったヒープ化処理(percolate_down)を実行する
        """
        self.percolate_down()

        return res

    def sort(self):
        temp_list = self.list
        return [self.pop_min() for _ in range(len(temp_list))]

#%%
my_list = [3, 1, 88, 15, 2, 61, 17, 2, 2, 18, 21]
print('my initial list >>>', my_list)

my_heap = heap(my_list)
print('insert 100 to heap')
my_heap.insert(100)
print('heap with 100', my_heap.list)

res = my_heap.pop_min()
print('pop_min > ', res)

print('heap sort', my_heap.sort())


#%%
my_list = [random.randint(1,100) for _ in range(6)]
my_heap = heap(my_list)
#%%
%%timeit
my_heap.sort()

#%%
%%timeit
sorted(my_list)

#%%
