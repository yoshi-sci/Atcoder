# %%
'''
ITP1 Introduction to Programming I
https://judge.u-aizu.ac.jp/onlinejudge/finder.jsp?course=ITP1
'''

# %%
# ITP1_1_C
# 縦aマス、横bマスの長方形の面積を求める
I = input()  # a,bを入力
a, b = map(int, I.split())  # a,bをint型に変換
S = a * b
L = 2 * (a + b)
print(S, L)


# %%
# ITP1_1_D
def time_conversion(S):
    if S < 0 or S > 86400:
        return "Error"
    elif S > 3600:
        h = S // 3600
        m = S % 3600 // 60
        s = S % 60
    elif S > 60:
        h = 0
        m = S // 60
        s = S % 60
    else:
        h = 0
        m = 0
        s = S
    return h, m, s


input_S = int(input())
h, m, s = time_conversion(input_S)
print(f"{h}:{m}:{s}")  # f-string: {変数名}で変数を埋め込む, :でフォーマット指定

# %%
# ITP1_2_A
a, b = map(int, input().split())


def compare(a, b):
    if a < b:
        return "a < b"
    elif a > b:
        return "a > b"
    else:
        return "a == b"


print(compare(a, b))

# %%
# ITP1_2_B
a, b, c = map(int, input().split())


def judge(a, b, c):
    if a < b < c:
        return "Yes"
    else:
        return "No"


print(judge(a, b, c))
# %%
# ITP1_2_C
a, b, c = map(int, input().split())


def sort(a, b, c):
    if a > b:
        a, b = b, a  # aとbを入れ替える
    if b > c:
        b, c = c, b
    if a > b:
        a, b = b, a
    return a, b, c


print(*sort(a, b, c))
# %%
# ITP1_2_D
W, H, x, y, r = map(int, input().split())


def judge(W, H, x, y, r):
    if x + r > W or x - r < 0:  # x軸方向にはみ出す場合
        return "No"
    elif y + r > H or y - r < 0:  # y軸方向にはみ出す場合
        return "No"
    else:
        return "Yes"


print(judge(W, H, x, y, r))
# %%
# ITP1_3_A
for i in range(1000):
    print("Hello World")

# %%
# ITP1_3_B
while True:
    x = int(input())
    if x == 0:
        break
    print(f"Case {i}: {x}")
    i += 1

# %%
# ITP1_3_C
while True:
    x, y = map(int, input().split())
    if x == 0 and y == 0:
        break
    if x < y:
        print(x, y)
    else:
        print(y, x)

# %%
# ITP1_3_D
a, b, c = map(int, input().split())
count = 0
for i in range(a, b + 1):  # aからbまでの数を調べる
    if c % i == 0:
        count += 1
print(count)

# %%
# ITP1_4_A
a, b = map(int, input().split())
d = a // b  # 商
r = a % b  # 余り
f = a / b  # 小数
print(f"{d} {r} {f:.5f}")  # ;.nfで小数点以下n桁まで表示

# %%
# ITP1_4_B
r = float(input())
S = 3.14159265359 * r**2
L = 2 * 3.14159265359 * r
print(f"{S:.6f} {L:.6f}")

# %%
# ITP1_4_C
while True:
    a, op, b = input().split()
    a, b = int(a), int(b)
    if op == "?":
        break
    if op == "+":
        print(a + b)
    elif op == "-":
        print(a - b)
    elif op == "*":
        print(a * b)
    elif op == "/":
        print(a // b)

# %%
# ITP1_4_D
n = int(input())
n_list = list(map(int, input().split()))
print(min(n_list), max(n_list), sum(n_list))

# %%
# ITP1_5_A
while True:
    H, W = map(int, input().split())
    if H == 0 and W == 0:
        break
    for i in range(H):
        print("#" * W)
    print()  # 空行を入れる

# %%
# ITP1_5_B
while True:
    H, W = map(int, input().split())
    if H == 0 and W == 0:
        break
    for i in range(H):
        if i == 0 or i == H - 1:
            print("#" * W)
        else:
            print("#" + "." * (W - 2) + "#")  # +で文字列を連結
    print()

# %%
# ITP1_5_C
while True:
    H, W = map(int, input().split())
    if H == 0 and W == 0:
        break  # 終了条件
    for i in range(H):
        if i % 2 == 0:  # 偶数行
            if W % 2 == 0:
                print("#." * (W // 2))
            else:
                print("#." * (W // 2) + "#")
        else:  # 奇数行
            if W % 2 == 0:
                print(".#" * (W // 2))
            else:
                print(".#" * (W // 2) + ".")
    print()

# %%
# ITP1_5_D
#

# %%
# ITP1_6_A
n = int(input())
a = list(map(int, input().split()))
a.reverse()  # リストを逆順にする
print(*a)  # *でリストの中身を展開して表示

# %%
# ITP1_6_B
n = int(input())
cards = [0] * 52  # カードの山 0:なし, 1:あり, S:0-12, H:13-25, C:26-38, D:39-51
# カードの山にカードを追加
for i in range(n):
    mark, num = input().split()  # マークと数字を入力
    num = int(num)
    if mark == "S":
        cards[num - 1] = 1
    elif mark == "H":
        cards[num + 12] = 1
    elif mark == "C":
        cards[num + 25] = 1
    elif mark == "D":
        cards[num + 38] = 1
# カードの山にないカードを表示
for i in range(52):
    if cards[i] == 0:
        if i < 13:
            print("S", i + 1)
        elif i < 26:
            print("H", i - 12)
        elif i < 39:
            print("C", i - 25)
        else:
            print("D", i - 38)

# ITP1_6_B 別解
n = int(input())
# 2次元配列でカードの山を表現 13*4
cards = [
    [0] * 13 for _ in range(4)
]  # 内包表記：[式 for 変数 in イテラブルオブジェクト]
# カードの山にカードを追加
for i in range(n):
    mark, num = input().split()  # マークと数字を入力
    num = int(num)
    if mark == "S":
        cards[0][num - 1] = 1
    elif mark == "H":
        cards[1][num - 1] = 1
    elif mark == "C":
        cards[2][num - 1] = 1
    elif mark == "D":
        cards[3][num - 1] = 1
# カードの山にないカードを表示
for i in range(13):
    for j in range(4):
        if cards[j][i] == 0:
            if j == 0:
                print("S", i + 1)
            elif j == 1:
                print("H", i + 1)
            elif j == 2:
                print("C", i + 1)
            else:
                print("D", i + 1)

# %%
# ITP1_6_C
n = int(input())
rooms = [
    [[0] * 10 for _ in range(3)] for _ in range(4)
]  # 3次元配列で部屋を表現 4棟*3階*10部屋
for i in range(n):
    b, f, r, v = map(int, input().split())
    rooms[b - 1][f - 1][r - 1] += v
    if rooms[b - 1][f - 1][r - 1] < 0:  # 負の数になった場合は、0にする
        rooms[b - 1][f - 1][r - 1] = 0
    elif rooms[b - 1][f - 1][r - 1] > 9:
        rooms[b - 1][f - 1][r - 1] = 9

for i in range(4):
    for j in range(3):
        print(
            " " + " ".join(map(str, rooms[i][j]))
        )  # joinでリストを文字列に変換して表示, m
    if i < 3:  # 最後の棟以外は区切りを入れる
        print("#" * 20)

# %%
# ITP1_6_D
n, m = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(n)]  # m*n行列Aを入力
b = [int(input()) for _ in range(m)]  # ベクトルbを入力


def matrix_product(A, b):
    result = [0] * n
    for i in range(n):
        for j in range(m):
            result[i] += A[i][j] * b[j]
    return result


print(*matrix_product(A, b))  # *はアンパック演算子でiterableオブジェクトを展開して表示


# %%
# ITP1_7_A
def score(mid, final, reexam):
    if mid == -1 or final == -1:
        return "F"
    elif mid + final >= 80:
        return "A"
    elif mid + final >= 65:
        return "B"
    elif mid + final >= 50:
        return "C"
    elif mid + final >= 30:
        if reexam >= 50:
            return "C"
        else:
            return "D"
    else:
        return "F"


while True:
    mid, final, reexam = map(int, input().split())
    if mid == -1 and final == -1 and reexam == -1:
        break  # 終了条件
    print(score(mid, final, reexam))


# %%
# ITP1_7_B
def count_pair(n, x):  # 全探索
    count = 0
    for i in range(1, n - 1):
        for j in range(i + 1, n):  # iより大きい数から調べる
            for k in range(j + 1, n + 1):
                if i + j + k == x:
                    count += 1
    return count


while True:
    n, x = map(int, input().split())
    if n == 0 and x == 0:
        break  # 終了条件
    print(count_pair(n, x))

# %%
# ITP1_7_C
r, c = map(int, input().split())
array = [[0] * (c + 1) for _ in range(r + 1)]  # (r+1)*(c+1)の2次元配列を作成

for i in range(r):
    array[i] = list(map(int, input().split()))  # 行列を入力
    array[i].append(
        sum(array[i])
    )  # 行の合計を追加 itterable.append()でリストの最後に要素を追加

for i in range(c + 1):
    sum_column = 0
    for j in range(r):
        sum_column += array[j][i]  # 列の合計を計算
    array[r][i] = sum_column  # 列の合計を追加

for i in range(r + 1):
    print(" ".join(map(str, array[i])))  # joinでリストを文字列に変換して表示


# %%
# ITP1_7_D
def matrix_product(A, B):
    C = [[0] * l for _ in range(n)]  # n*l行列Cを作成
    for i in range(n):
        for j in range(l):
            for k in range(m):
                C[i][j] += A[i][k] * B[k][j]
    return C


n, m, l = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(n)]  # n*m行列Aを入力
B = [list(map(int, input().split())) for _ in range(m)]  # m*l行列Bを入力
C = matrix_product(A, B)
for i in range(n):
    print(" ".join(map(str, C[i])))  # joinでリストを文字列に変換して表示


# %%
# ITP1_8_A
def change_case(s):
    return s.swapcase()  # swapcaseで大文字と小文字を入れ替える


s = input()
print(change_case(s))


# %%
# ITP1_8_A_別解
def change_case(s):
    result = ""
    for c in s:
        if c.islower():
            result += c.upper()
        else:
            result += c.lower()
    return result


s = input()
print(change_case(s))


# %%
# ITP1_8_B
def sum_digits(n):  # 各桁(digit)の数字の和を計算
    sum = 0
    for c in str(n):
        sum += int(c)  # int()で文字列を数値に変換
    return sum


while True:
    n = input()
    if n == "0":
        break  # 終了条件
    print(sum_digits(n))


# %%
# ITP1_8_C
def count_alphabet(str):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    count = [0] * 26
    for c in str:
        if c.isalpha():  # isalpha()でアルファベットかどうか判定
            c = c.lower()  # 小文字に変換
            count[alphabet.index(c)] += 1  # index()でアルファベットのインデックスを取得
    return count


input_str = input()
count = count_alphabet(input_str)

for i in range(26):
    print(f"{chr(i+97)} : {count[i]}")  # ACSIIコードで97がa, 98がb, ... 122がz
# %%
# ITP1_8_D
s = input()
p = input()
# sを2倍してpが含まれるかどうかを調べる
if (
    p in s * 2
):  # 検索文字列 in 対象文字列：対象文字列に検索文字列が含まれるかどうかを検索
    print("Yes")
else:
    print("No")

# %%
# ITP1_9_A
w = input()
count = 0  # ループの中に入れると毎回初期化される
while True:
    t = input()
    if t == "END_OF_TEXT":
        break
    t = t.lower().split()  # 小文字に変換して単語単位にリストに分割
    for (
        word
    ) in (
        t
    ):  # lower()で小文字に変換, split()で文字列型を単語に分割、引数なしで空白文字で分割
        if word == w:
            count += 1
print(count)


# %%
# ITP1_9_B
def shuffle(cards, h_shuffle):
    return (
        cards[h_shuffle:] + cards[:h_shuffle]
    )  # リストのスライス: cards[start:end]でstartからend-1までの要素を取得


cards = input()
m_shuffle = int(input())
for i in range(m_shuffle):
    h_shuffle = int(input())
    cards = shuffle(cards, h_shuffle)
print(cards)
# %%
# ITP1_9_C
n = int(input())
taro = 0
hanako = 0

for i in range(n):
    taro_card, hanako_card = input().split()
    if (
        taro_card > hanako_card
    ):  # 文字列の比較は辞書順(アルファベット順)で早い方が小さい値、ex) "a" < "b"
        taro += 3
    elif taro_card < hanako_card:
        hanako += 3
    else:
        taro += 1
        hanako += 1

print(taro, hanako)


# %%
# ITP1_9_D
def order_str(str, order, a, b, p=None):  # p=Noneでデフォルト引数を設定
    if order == "replace":
        return str[:a] + p + str[b + 1 :]
    elif order == "reverse":
        return (
            str[:a] + str[a: b + 1][::-1] + str[b + 1:]
        )  # [x:y:z]の第一引数:開始位置, 第二引数:終了位置, 第三引数:ステップ、-1で逆順
    elif order == "print":
        print(str[a: b + 1])
        return str  # strをそのまま返す


str = input()
q = int(input())
for i in range(q):
    I = input().split()
    order, a, b = I[0], int(I[1]), int(I[2])
    p = I[3] if order == "replace" else None  # Noneとは
    a, b = int(a), int(b)
    str = order_str(str, order, a, b, p)


# %%
# ITP1_10_A
def euclidean_distance(x1, y1, x2, y2):  # 2点間のユークリッド距離を計算
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5


x1, y1, x2, y2 = map(float, input().split())  # float型に変換
print(f"{euclidean_distance(x1, y1, x2, y2):.5f}")  # 小数点以下5桁まで表示
# %%
# ITP1_10_A_別解
import math
def euclidean_distance(x1, y1, x2, y2):  # 2点間のユークリッド距離を計算
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)


x1, y1, x2, y2 = map(float, input().split())  # float型に変換
print(f"{euclidean_distance(x1, y1, x2, y2):.5f}")  # 小数点以下5桁まで表示
# %%
# ITP1_10_B
import math
a, b, C = map(int, input().split())
C = math.radians(
    C
)  # math.radians()で度数法をラジアンに変換, math.degrees()でラジアンを度数法に変換
h = b * math.sin(C)  # sin(C) = h/b
S = 0.5 * a * h
L = a + b + math.sqrt(a**2 + b**2 - 2 * a * b * math.cos(C))  # 余弦定理
print(f"{S:.5f}")
print(f"{L:.5f}")
print(f"{h:.5f}")


# %%
# ITP1_10_C
def std_deviation(n, scores):
    mean = sum(scores) / n
    variance = sum([(score - mean) ** 2 for score in scores]) / n
    return variance**0.5


while True:
    n = int(input())
    if n == 0:  # 終了条件
        break
    scores = list(map(float, input().split()))
    std_dev = std_deviation(
        n, scores
    )  # 関数と変数名は衝突を避けるため、異なる名前をつける
    print(f"{std_dev:.5f}")


# %%
# ITP1_10_D
def minkowski_distance(x, y, p):  # ミンコフスキー距離を計算
    if p == float("inf"):  # p=∞:チェビシェフ距離
        min_dis = max([abs(x_i - y_i) for x_i, y_i in zip(x, y)])
    else:  # p=1:マンハッタン距離, p=2:ユークリッド距離
        min_dis = sum([abs(x_i - y_i) ** p for x_i, y_i in zip(x, y)]) ** (
            1 / p
        )  # x_i, y_iをzip()で同時に取り出す, zip()はイテラブルオブジェクトをまとめる
    return min_dis


n = int(input())
v1 = list(map(int, input().split()))
v2 = list(map(int, input().split()))

# p=1,2,3,∞の場合のv1とv２のミコンフスキー距離を出力
for p in [1, 2, 3, float("inf")]:  # 飛び飛びの値をリストで指定、無限はfloat('inf')
    print(f"{minkowski_distance(v1, v2, p):.6f}")


# %%
# ITP1_11_A
class Dice:
    def __init__(
        self, labels
    ):  # __init__はクラスのコンストラクタ(生成時に実行されるメソッド)
        self.labels = labels  # selfはインスタンス自身を指す, self.variableでインスタンス変数を定義

    def roll(self, direction):
        if direction == "N":
            self.labels = [
                self.labels[1],
                self.labels[5],
                self.labels[2],
                self.labels[3],
                self.labels[0],
                self.labels[4],
            ]
        elif direction == "E":
            self.labels = [
                self.labels[3],
                self.labels[1],
                self.labels[0],
                self.labels[5],
                self.labels[4],
                self.labels[2],
            ]
        elif direction == "W":
            self.labels = [
                self.labels[2],
                self.labels[1],
                self.labels[5],
                self.labels[0],
                self.labels[4],
                self.labels[3],
            ]
        elif direction == "S":
            self.labels = [
                self.labels[4],
                self.labels[0],
                self.labels[2],
                self.labels[3],
                self.labels[5],
                self.labels[1],
            ]

    def get_top(self):
        return self.labels[0]  # サイコロの上面[0]を返す


dice_labels = list(map(int, input().split()))
dice_1 = Dice(dice_labels)
directions = input()
for direction in directions:
    dice_1.roll(direction)
print(dice_1.get_top())

# %%
# ITP1_11_B

# %%
# ITP1_11_C

# %%
# ITP1_11_D
