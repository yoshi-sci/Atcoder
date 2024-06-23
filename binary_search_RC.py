#%%
'''
応用例1. 
年齢当てゲーム
応用例2.
std::lower_boundの活用例
応用例3.
最適化問題を判定問題に
応用例4.
メディアンを求める

6.4 6.6
'''

# %%
# 応用例1. 年齢当てゲーム
# 20歳以上35歳以下の年齢を当てるゲーム
# 20歳未満、36歳以上は入力されないと仮定
# 4回の質問をした後に年齢を当てる

def age_guess():
    left = 20
    right = 36
    for _ in range(4):
        mid = (left + right) // 2
        print(left, mid, right)
        while True:
            print(f'あなたの年齢は{mid}歳以上ですか？ [yes/no]')
            ans = input().strip().lower()
            if ans in ['yes', 'no']:
                break
            print('無効な入力です。yes か no で答えてください。')
        
        if ans == 'yes':  # mid以上
            left = mid
        else:  # mid未満
            right = mid
    print(left, mid, right)
    print(f'あなたの年齢は{left}歳です')


age_guess()


# %%
# 応用例2. std::lower_boundの活用例
'''
N個の整数a_0, a_1, ..., a_{N-1}とb_0, b_1, ..., b_{N-1}が与えられる
２組の整数のペア(i, j)について、a_i + b_j >= Kを満たすもののうち、最小値を求める
但し、a_i + b_j >= Kを満たすペア(i, j)は少なくとも１つは存在すると仮定

1. a_iを固定してb_jを二分探索
2. b_j >= K - a_i を満たす最小のb_jを求める
'''

# ソートされたリストAから、target以上の値を持つ最小のインデックスを返す
def lower_bound(A: list, target: int) -> int:
    left = 0
    right = len(A)
    while left < right:
        mid = (left + right) // 2
        if A[mid] >= target:
            right = mid
        else:
            left = mid + 1
    return left


# 入力の受け取り
a_list = list(map(int, input().split()))
b_list = list(map(int, input().split()))
K = int(input())

b_list.sort()  # リスト型のsort()は元のリストを書き換える破壊的メソッド

min_value = float('inf') # 無限大で初期化
for a in a_list:
    idx = lower_bound(b_list, K - a)
    if idx < len(b_list):
        b = b_list[idx]
        min_value = min(min_value, a + b)
print(min_value)

# %%
# 応用例3. 最適化問題を判定問題に
'''
ABC 023 D - 射撃王
https://atcoder.jp/contests/abc023/tasks/abc023_d
N個の風船があり、i番目の風船は初期状態で高度h_i、1秒後ごとにS_iだけ高度が上昇する
開始時に一つの風船をわり、１秒ごとに一つの風船を割ることができる
ペナルティは、風船を割った時の高度の最大値である
ペナルティの最小値を求める

計算量: O(N log N log M) (N: 風船の数, M: 高度の最大値)
'''

N = int(input())
heights = [0] * N
speeds = [0] * N
for i in range(N):
    heights[i], speeds[i] = map(int, input().split())

max_height = max(heights[i] + speeds[i] * N for i in range(N))


def binary_search_min_height(heights, speeds, n):
    left = 0


# %%
# 応用例4. メディアンを求める
'''
N個の非負整数a_0, a_1, ..., a_{N-1}が与えられる
x未満の整数がちょうど(N+1)/2個以上あるようなxの最小値を求める
'''


# %%
# 6.4
'''
a_0, a_1, ..., a_{N-1}が与えられる(a_0=<a_1=<...=<a_{N-1})
N個からM個選び、選んだ点の距離の最小値の最大値を求める
'''

def is_feasible(A, N, M, d):
    # 最初の点を選ぶ
    count = 1
    last_position = A[0]
    for i in range(1, N):
        if A[i] - last_position >= d:
            count += 1
            last_position = A[i]
            if count >= M:
                return True
    return False

def binary_search_max_min_distance(A:list, N, M):
    left = 0
    right = A[-1] - A[0]
    while right - left > 1:
        mid = (left + right) // 2
        if is_feasible(A, N, M, mid):
            left = mid
        else:
            right = mid
    return left

# 入力の受け取り
N = int(input())
A = list(map(int, input().split()))
M = int(input())

# 距離の最小値の最大値を求める
max_min_distance = binary_search_max_min_distance(A, N, M)
print(max_min_distance)


# %%
# 6.6
'''
ABC 026 D - 高橋君ボール1号
正の整数A, B, Cが与えられる
A * t + B * sin(C * t * pi) = 100 となるtを求める
f(t)-100の絶対値≦e-6であれば、正解
(1≦A,B,C≦100)
'''
import math

# 入力の受け取り
A, B, C = map(int, input().split())

def f(t):
    return A * t + B * math.sin(C * t * math.pi)

# 二分探索
left = 0
right = 200  # 初期範囲設定 
eps = 1e-7   # 精度

while True:
    mid = (left + right) / 2
    if abs(100 - f(mid)) < eps:
        break
    if f(mid) < 100:
        left = mid
    else:
        right = mid

# 結果の出力
print(mid)
# %%
