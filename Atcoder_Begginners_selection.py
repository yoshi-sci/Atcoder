#%%
'''
計算量の見積もり
https://qiita.com/drken/items/f909b79ee03e679c7142
https://qiita.com/drken/items/872ebc3a2b5caaa4a0d0
'''

'''
Atcoder Begginners Selection https://atcoder.jp/contests/abs
過去問精選 10 問 https://qiita.com/drken/items/fd4e5e3630d0f5859067


Atcoder problems https://kenkoooo.com/atcoder/#/table/
ABC 042 ～最新を解く
・https://qiita.com/e869120/items/eb50fdaece12be418faa
・https://qiita.com/drken/items/e77685614f3c6bf86f44
'''

'''
pythonの標準ライブラリ

アルゴリズムの基本
・全探索（bit 全探索、順列全探索を含む）
・二分探索
・深さ優先探索（DFS）
・幅優先探索（BFS）
・動的計画法（bitDP などを含む）
・ダイクストラ法（最短経路問題）
・ワーシャルフロイド法（最短経路問題）
・クラスカル法（最小全域木問題）
・高速な素数判定法
・べき乗を高速に計算するアルゴリズム
・逆元を計算するアルゴリズム
・累積和

データ構造の基本
・グラフ（グラフ理論）
・木
・Union-Find
'''

#%%
#PracticeA - Welcome to AtCoder
a = int(input())
b, c = map(int, input().split())
s = input()
sum = a + b + c
print(sum, s)

#%%
# ABC086 A - Product
a, b = map(int, input().split())
if a * b % 2 == 0:
    print('Even')
else:
    print('Odd')

#%%
# ABC081 A - Placing Marbles
s = input()
count = s.count('1')
print(count)

# %%
# ABC081 B - Shift only
N = int(input())
A = list(map(int, input().split()))
count = 0
while True:
    if all(a % 2 == 0 for a in A):
        A = [a // 2 for a in A]
        count += 1
    else:
        break
print(count)

# %%
# ABC087 B - Coins
A, B, C, X = [int(input()) for _ in range(4)]
count = 0
for i in range(A+1):
    for j in range(B+1):
        for k in range(C+1):
            if 500*i + 100*j + 50*k == X:
                count += 1
print(count)

# %%
# ABC083 B - Some Sums
N, A, B = map(int, input().split())
ans_N = 0
for i in range(1, N+1):
    sum_N = sum(map(int, str(i)))  # map(function, list)でリストの各要素にfunctionを適用
    if A <= sum_N <= B:
        ans_N += i
print(ans_N)