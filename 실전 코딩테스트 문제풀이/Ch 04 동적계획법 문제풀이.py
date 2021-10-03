def baekJoon1932():
    N = int(input())
    # DP[i][j] : i, j 도착했을 때 최댓값
    # DP[i][j] = max(DP[i - 1][j - 1], DP[i - 1][j]) + A[i][j]
    A = [[0 for _ in range(N + 1)] for _ in range(N + 1)]
    DP = [[0 for _ in range(N + 1)] for _ in range(N + 1)]

    for i in range(1, N + 1):
        tmp = list(map(int, input().split()))
        for j in range(1, i + 1):
            A[i][j] = tmp[j - 1]

    for i in range(1, N + 1):
        for j in range(1, i + 1):
            DP[i][j] = max(DP[i - 1][j - 1], DP[i - 1][j]) + A[i][j]

    print(max(DP[-1]))

def baekJoon11055():
    from copy import deepcopy
    N, A = int(input()), list(map(int, input().split()))

    DP = deepcopy(A)

    for i in range(1, N):
        for j in range(i):
            if A[i] > A[j]:
                DP[i] = max(A[i] + DP[j], DP[i])

    print(max(DP))

def baekJoon14002():
    from copy import deepcopy
    N, A = int(input()), list(map(int, input().split()))
    
    # DP[i] : i 까지 왔을 때, 합의 최대
    DP = deepcopy(A)
    rev = [i for i in range(N)]
    result = []
    idx = 0

    for i in range(1, N):
        for j in range(i):
            if A[i] > A[j] and DP[i] < A[i] + DP[j]:
                DP[i] = A[i] + DP[j]
                rev[i] = j
                
        if DP[idx] < DP[i]:
            idx = i
            
    while rev[idx] != idx:
        result.append(A[idx])
        idx = rev[idx]

    result.append(A[idx])

    print(len(result))
    for i in result[::-1]:
        print(i, end=" ")

def baekJoon2167():
    N, M = map(int, input().split())

    A = [list(map(int, input().split())) for _ in range(N)]
    DP = [[0 for i in range(M + 1)] for _ in range(N + 1)]


    for i in range(1, N + 1):
        for j in range(1, M + 1):
            DP[i][j] = DP[i - 1][j] + DP[i][j - 1] - DP[i - 1][j - 1] + A[i - 1][j - 1]        
            
    for _ in range(int(input())):
        i, j, x, y = map(int, input().split())
        print(DP[x][y] - DP[i - 1][y] - DP[x][j - 1] + DP[i - 1][j - 1])

def baekJoon1915():
    N, M = map(int, input().split())
    A = [[0 for _ in range(M + 1)] for _ in range(N + 1)]
    DP = [[0 for _ in range(M + 1)] for _ in range(N + 1)]

    for i in range(N):
        for j, result in enumerate(list(map(int, list(input())))):
            A[i + 1][j + 1] = result

    for i in range(1, N + 1):
        for j in range(1, M + 1):
            if A[i][j]:
                DP[i][j] = min(DP[i - 1][j], DP[i][j - 1], DP[i - 1][j - 1]) + 1 

    print(max([max(i) for i in DP]) ** 2)

def baekJoon12849():
    DP = [1, 0, 0, 0, 0, 0, 0, 0]

    def nxt(state):
        tmp = [0 for _ in range(8)]
        tmp[0] = state[1] + state[2]
        tmp[1] = state[0] + state[2] + state[3]
        tmp[2] = state[0] + state[1] + state[3] + state[4]
        tmp[3] = state[1] + state[2] + state[4] + state[5]
        tmp[4] = state[2] + state[3] + state[5] + state[7]
        tmp[5] = state[3] + state[4] + state[6]
        tmp[6] = state[5] + state[7]
        tmp[7] = state[4] + state[6]
        for i in range(8):
            tmp[i] %= 1000000007
        return tmp
        
    for i in range(int(input())):
        DP = nxt(DP)

    print(DP[0])

def baekJoon11066():
    def process():
        N = int(input())
        A = [0 for _ in range(N + 1)]
        for i, result in enumerate(list(map(int, input().split()))):
            A[i + 1] = result
            
        S = [0 for _ in range(N + 1)]
        for i in range(1, N + 1):
            S[i] = S[i - 1] + A[i]

        DP = [[0 for i in range(N + 1)] for _ in range(N + 1)]
        for i in range(2, N + 1): # 부분파일의 길이
            for j in range(1, N + 2 - i): # 시작점
                DP[j][j + i - 1] = min([DP[j][j + k] + DP[j + k + 1][j + i - 1] for k in range(i - 1)]) + S[j + i - 1] - S[j - 1]

        print(DP[1][N])
        
    for _ in range(int(input())):
        process()

if __name__ == "__main__":
    baekJoon11066()