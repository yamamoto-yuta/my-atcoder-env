# 文字列を受け取る場合
S = input()
print(S)

# 整数を受け取る場合
N = int(input())
print(N)

# 小数を受け取る場合
F = float(input())
print(F)

# 文字列を受け取る場合
A, B = input().split()
print(A, B)

# 整数を受け取る場合
X, Y, Z = map(int, input().split())
print(X, Y, Z)

# 小数を受け取る場合
H, M, S = map(float, input().split())
print(H, M, S)

# 文字列を受け取る場合
A = input().split()
print(A)

# 整数列を受け取る場合
A = list(map(int, input().split()))
print(A)

# 小数列を受け取る場合
A = list(map(float, input().split()))
print(A)

# 複数行の文字列を受け取る場合
A = [input().split() for _ in range(N)]
print(A)

# 複数行の整数列を受け取る場合
A = [list(map(int, input().split())) for _ in range(N)]
print(A)

# 複数行の小数列を受け取る場合
A = [list(map(float, input().split())) for _ in range(N)]
print(A)
