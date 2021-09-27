def baekJoon1920():
    N = int(input())
    lst = list(map(int, input().split()))
    M = int(input())
    lst2 = list(map(int, input().split()))

    for i in lst2:
        if i in lst:
            print(1)
        else:
            print(0)

def baekJoon16165():
    # N, M = map(int, input().split())

    # group_list = []
    # group_number = []
    # group_member = dict()

    # for i in range(N):
    #     group_list.append(input())
    #     group_number.append(int(input()))
    #     member = []
    #     for _ in range(group_number[i]):
    #         member.append(input())
    #     member.sort()
    #     group_member[group_list[i]] = member

    # for i in range(M):
    #     question = input()
    #     question_kind = int(input())
        
    #     if question_kind == 0:
    #         for v in group_member[question]:
    #             print(v)
    #     elif question_kind == 1:
    #         for k, v in group_member.items():
    #             for v2 in v:
    #                 if v2 == question:
    #                     print(k)
    N, M = map(int, input().split())

    team_mem, mem_team = {}, {}

    for i in range(N):
        team_name, mem_num = input(), int(input())
        team_mem[team_name] = []
        for j in range(mem_num):
            name = input()
            team_mem[team_name].append(name)
            mem_team[name] = team_name
            
    for i in range(M):
        name, q = input(), int(input())
        if q:
            print(mem_team[name])
        else:
            for mem in sorted(team_mem[name]):
                print(mem)

def baekJoon17224():
    N, L, K = map(int, input().split())

    array = []

    for _ in range(N):
        sub1, sub2 = map(int, input().split())
        array.append((sub1, sub2))
        
    result = 0
    count = 0

    for i in range(N):
        sub1, sub2 = array[i]
        if sub1 <= L and sub2 <= L and count < K:
            result += 140
            count += 1
            array[i] = (float("inf"), float("inf"))
            
    for i in range(N):
        sub1, sub2 = array[i]
        if sub1 <= L and count < K:
            result += 100
            count += 1
            array[i] = (float("inf"), sub2)
        elif sub2 <= L and count < K:
            result += 40
            count += 1
            array[i] = (sub1, float("inf"))
            
    print(result)

def baekJoon9037():
    T = int(input())

    for _ in range(T):
        N = int(input())
        C = list(map(int, input().split()))

        count = 0

        for i in range(len(C)):
            if C[i] % 2 != 0:
                C[i] += 1
                
        while sorted(C)[0] != sorted(C)[-1]:
            B = []
            B.append(C[-1] // 2)
            for i in range(len(C)):
                if i < len(C) - 1:
                    B.append(C[i] // 2)
                C[i] = C[i] // 2
                    
            for i in range(len(C)):
                C[i] = C[i] + B[i]
                if C[i] % 2 != 0:
                    C[i] += 1
            count += 1
        print(count)

def baekJoon16769():
    C, M = [], []

    for _ in range(3):
        a, b = map(int, input().split())
        C.append(a)
        M.append(b)

    for i in range(100):
        idx = i % 3
        nxt = (idx + 1) % 3
        M[idx], M[nxt]= max(M[idx] - (C[nxt] - M[nxt]), 0), min(C[nxt], M[nxt] + M[idx])

    for i in M:
        print(i)
        
if __name__ == "__main__":
    baekJoon16769()