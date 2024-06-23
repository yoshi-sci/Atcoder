#%%
# A - Count Takahashi
N = int(input())
count = 0
for i in range(N):
    S = input()
    if S == "Takahashi":
        count += 1

print(count)
# %%
# B - Couples
N = int(input())
A = list(map(int, input().split()))
count = 0

for i in range(2*N-2):
    if A[i] == A[i+2]:
        count += 1
print(count)
# %%
# C - Tile Distance 2
Sx, Sy = map(int, input().split())
Tx, Ty = map(int, input().split())
dy_abs = abs(Ty - Sy)
dx_abs = abs(Tx - Sx)

# xの方向を決める
x_direction = "neutral"
if Tx < Sx:
    x_direction = "negative"
elif Tx > Sx:
    x_direction = "positive"

#Sxが偶数の場合
if (Sx+Sy) % 2 == 0 and x_direction == "positive":
    dx_abs -= 1
elif (Sx+Sy) % 2 == 1 and x_direction == "negative":
    dx_abs -= 1

count = 0
if dx_abs <= dy_abs:
    count += dy_abs
else:
    count = dy_abs + (dx_abs - dy_abs+1)//2 

print(count)

# %%
# D- Avoid K Palindrome
N, K = map(int, input().split())
S = input()

#%%
# E - Water Tank
N = int(input())
H = list(map(int, input().split()))

Times = []
Max_H = 0

for i in range(N):
    if H[i] > Max_H:
        Time_i = H[i]*(i+1)+1
        Times.append(Time_i)
        Max_H = H[i]
    else:
        Time_i = Times[i-1] + H[i]
        Times.append(Time_i)

print(*Times)
# %%
