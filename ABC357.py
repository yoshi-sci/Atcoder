# %%
#A - Sanitize Hands
N, M = map(int, input().split())
H = list(map(int, input().split()))

hands = 0
count = 0
for i in range(N):
    hands += H[i]
    if hands <= M:
        count += 1

print(count)

# %%
# B - Uppercase and Lowercase
def judge_case(S):
    uppecase = 0
    lowercase = 0
    for i in S:
        if i.isupper():
            uppecase += 1
        elif i.islower():
            lowercase += 1
    if uppecase > lowercase:
        return "upper"
    else:
        return "lower"

def change_case(S):
    if judge_case(S) == "upper":
        return S.upper()
    else:
        return S.lower()


S = input()
print(change_case(S))

# %%
# C - Sierpinski carpet


