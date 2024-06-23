#%%
# A - Welcome to AtCoder Land
S,T = input().split()
def judge_words(S, T):
    if S == "AtCoder" and T == "Land":
        return "Yes"
    else:
        return "No"

print(judge_words(S, T))
# %%
# B - Ticket Counter
N, A = map(int, input().split())
times = list(map(int, input().split()))

def ticket_time(times_i, A, buy_time_prev):
    buy_time = max(times_i+A, buy_time_prev+A)
    return buy_time


buy_time = 0
for i in range(N):
    buy_time = ticket_time(times[i], A, buy_time)
    print(buy_time)

# %%
# C - Popcorn
# N個の店とM種類のポップコーンがある
# 店iはポップコーンS_iを持っている
# ポップコーンをM種類全て買うために必要な最小の店の数を求める
def max_popcorn(N, S:list, covered):
    max_popcorn = 0
    index = 0
    for i in range(N):
        count_i = bin(S[i]|covered).count('1')
        if count_i > max_popcorn:
            max_popcorn = count_i
            index = i
    return index

N, M = map(int, input().split())
S = []

for _ in range(N):
    s = input().replace('o', '1').replace('x', '0')
    S.append(int(s, 2))

count = 0
covered = 0  # 現在カバーされているポップコーンのビット集合

while covered != (1 << M) - 1:  # 全てのポップコーンをカバーするまで続ける
    count += 1
    index = max_popcorn(N, S, covered)
    covered |= S[index]  # 新しい店を加えることでカバーされるポップコーンを更新

print(count)

# %%
