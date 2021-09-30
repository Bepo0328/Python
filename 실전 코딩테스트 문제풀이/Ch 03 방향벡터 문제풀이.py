def baekJoon16956():
    R, C = map(int, input().split())
    M = [list(input()) for i in range(R)]

    dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]

    ck = False

    for i in range(R):
        for j in range(C):
            if M[i][j] == 'W':
                for w in range(4):
                    ii, jj = i + dx[w], j + dy[w]
                    if ii < 0 or ii == R or jj < 0 or jj == C:
                        continue
                    if M[ii][jj] == 'S':
                        ck = True
                        
    if ck:
        print(0)
    else:
        print(1)
        for i in range(R):
            for j in range(C):
                if M[i][j] not in 'SW':
                    M[i][j] = 'D'
                    
    for i in M:
        print(''.join(i))

def baekJoon14620():
    N = int(input())
    G = [list(map(int, input().split())) for i in range(N)]

    ans = 10000

    dx, dy = [0, 0, 0, 1, -1], [0, 1, -1, 0, 0]

    def ck(lst):
        ret = 0
        flow = []
        for flower in lst:
            x = flower // N
            y = flower % N
            
            if x == 0 or x == (N - 1) or y == 0 or y == (N - 1):
                return 10000
            
            for w in range(5):
                flow.append((x + dx[w], y + dy[w]))
                ret += G[x + dx[w]][y + dy[w]]
        if len(set(flow)) != 15:
            return 10000
        return ret
            
    for i in range(N * N):
        for j in range(N * N):
            for k in range(N * N):
                ans = min(ans, ck([i, j, k]))
                
    print(ans)

if __name__ == "__main__":
    baekJoon14620()