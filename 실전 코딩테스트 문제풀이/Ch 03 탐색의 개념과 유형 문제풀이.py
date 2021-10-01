def baekJoon1012():
    for _ in range(int(input())):
        M, N, K = map(int, input().split())

        data = [[0] * (M + 2)  for _ in range(N + 2)]
        
        for i in range(K):
            X, Y = map(int, input().split()) 
            data[Y + 1][X + 1] = 1
       
        result = [[False] * (M + 2) for _ in range(N + 2)]
        count = 0
        dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]

        def dfs(X, Y):
            result[X][Y] = True
            for w in range(4):
                XX, YY = X + dx[w], Y + dy[w]
                if data[XX][YY] == 0 or result[XX][YY]:
                    continue
                dfs(XX, YY)

        for i in range(1, N + 1):
            for j in range(1, M + 1):
                if data[i][j] == 0 or result[i][j]:
                    continue
                dfs(i, j)
                count += 1
                
        print(count)

def baekJoon16768():
    def new_array(N):
        return [[False for i in range(10)] for _ in range(N)]

    N, K = map(int, input().split())

    M = [list(input()) for _ in range(N)]

    ck = new_array(N)
    ck2 = new_array(N)

    dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]

    def dfs(x, y):
        ck[x][y] = True
        ret = 1
        for i in range(4):
            xx, yy = x + dx[i], y + dy[i]
            if xx < 0 or xx >= N or yy < 0 or yy >= 10:
                continue
            if ck[xx][yy] or M[x][y] != M[xx][yy]:
                continue
            ret += dfs(xx, yy)
        return ret

    def dfs2(x, y, val):
        ck2[x][y] = True
        M[x][y] = '0'
        for i in range(4):
            xx, yy = x + dx[i], y + dy[i]
            if xx < 0 or xx >= N or yy < 0 or yy >= 10:
                continue
            if ck2[xx][yy] or M[xx][yy] != val:
                continue
            dfs2(xx, yy, val)

    def down():
        for i in range(10):
            tmp = []
            for j in range(N):
                if M[j][i] != '0':
                    tmp.append(M[j][i])

            for j in range(N - len(tmp)):
                M[j][i] = '0'
            for j in range(N - len(tmp), N):
                M[j][i] = tmp[j - (N - len(tmp))]

    while True:
        exist = False
        ck = new_array(N)
        ck2 = new_array(N)
        for i in range(N):
            for j in range(10):
                if M[i][j] == '0' or ck[i][j]:
                    continue
                res = dfs(i, j) # 개수 세기
                if res >= K:
                    dfs2(i, j, M[i][j]) # 지우기
                    exist = True
                    
        if not exist:
            break
            
        down() # 내리기
            
    for i in M:
        print(''.join(i))

def baekJoon12100():
    from copy import deepcopy

    N = int(input())
    Board = [list(map(int, input().split())) for i in range(N)]

    def rotate90(N, B):
        NB = deepcopy(B)
        for i in range(N):
            for j in range(N):
                NB[j][N - i - 1] = B[i][j]
        return NB

    def convert(N, lst):
        newList = [i for i in lst if i]
        for i in range(1, len(newList)):
            if newList[i - 1] == newList[i]:
                newList[i - 1] *= 2
                newList[i] = 0
        newList = [i for i in newList if i]
        return newList + [0] * (N - len(newList))

    def dfs(N, B, count):
        ret = max([max(i) for i in B])
        if count == 0:
            return ret

        for _ in range(4):
            X = [convert(N, i) for i in B]
            if X != B:
                ret = max(ret, dfs(N, X, count - 1))
            B = rotate90(N, B)
        return ret

    print(dfs(N, Board, 5))

def baekJoon17406():
    from copy import deepcopy

    N, M, K = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(N)]
    Q = [tuple((map(int, input().split()))) for _ in range(K)]
    dx, dy = [1, 0, -1, 0], [0, -1, 0, 1]

    ans = 10000

    def value(arr):
        return min([sum(i) for i in arr])

    def convert(arr, qry):
        (r, c, s) = qry
        r, c = r - 1, c - 1
        new_arr = deepcopy(arr)
        for i in range(1, s + 1):
            rr, cc = r - i, c + i
            for w in range(4):
                for d in range(i * 2):
                    rrr, ccc = rr + dx[w], cc + dy[w]
                    new_arr[rrr][ccc] = arr[rr][cc]
                    rr, cc = rrr, ccc
        return new_arr
                    
    def dfs(arr, qry):
        global ans
        if sum(qry) == K:
            ans = min(ans, value(arr))
            return
        for i in range(K):
            if qry[i]:
                continue
            new_arr = convert(arr, Q[i])
            qry[i] = 1
            dfs(new_arr, qry)
            qry[i] = 0
            
    dfs(A, [0 for i in range(K)])
    print(ans)

if __name__ == "__main__":
    baekJoon17406()