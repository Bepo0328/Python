def baekJoon1439():
    S, tot = input(), 0
    for i in range(1, len(S)):
        if S[i] != S[i - 1]:
            tot += 1
    print((tot + 1) // 2)

def baekJoon16676():
    N = input()
    S = '1' * len(N)

    if len(N) == 1:
        print(1)
    elif int(N) >= int(S):
        print(len(N))
    else:
        print(len(N) - 1)

def baekJoon2437():
    N, A = int(input()), sorted(list(map(int, input().split())))

    ans = 0

    for i in A:
        if i <= ans + 1:
            ans += i
        else:
            break

    print(ans + 1)

def baekJoon1080():
    N, M = map(int, input().split())
    A = [list(map(int, list(input()))) for _ in range(N)]
    B = [list(map(int, list(input()))) for _ in range(N)]
    def flip(x, y, A):
        for i in range(3):
            for j in range(3):
                A[x + i][y + j] ^= 1
            
    ans = 0

    for i in range(N - 2):
        for j in range(M - 2):
            if A[i][j] != B[i][j]:
                flip(i, j, A)
                ans += 1
                
    if A != B:
        print(-1)
    else:
        print(ans)

def baekJoon2014():
    import heapq
    from copy import deepcopy

    K, N = map(int, input().split())
    p_list = list(map(int, input().split()))
    lst, ck = deepcopy(p_list), set()

    heapq.heapify(lst)
    ith = 0

    while ith < N:
        mn = heapq.heappop(lst)
        if mn in ck:
            continue
        ith += 1
        ck.add(mn)
        for i in p_list:
            heapq.heappush(lst, mn * i)

    print(mn)

if __name__ == "__main__":
    baekJoon2014()