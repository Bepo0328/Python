def baekJoon2480():
    dice1, dice2, dice3 = map(int, input().split())

    money = 0

    if dice1 == dice2 and dice2 == dice3:
        money += (10000 + dice1 * 1000)
    elif dice1 == dice2:
        money += (1000 + dice1 * 100)
    elif dice2 == dice3:
        money += (1000 + dice2 * 100)
    elif dice1 == dice3:
        money += (1000 + dice1 * 100)
    else:
        money += max(dice1, dice2, dice3) * 100
        
    print(money)

def baekJoon2484():
    N = int(input())
    max_money = 0

    for _ in range(N):
        dice = sorted(list(map(int, input().split())))
        money = 0
        
        if len(set(dice)) == 1:
            money += (50000 + dice[0] * 5000)
        elif len(set(dice)) == 2:
            if dice[1] == dice[2]:
                money += (10000 + dice[1] * 1000)
            else:
                money += (2000 + dice[1] * 500 + dice[2] * 500)
        elif len(set(dice)) == 3:
            if dice[0] == dice[1]:
                money += (1000 + dice[0] * 100)
            elif dice[1] == dice[2]:
                money += (1000 + dice[1] * 100)
            else:
                money += (1000 + dice[2] * 100)
        else:
            money += (dice[3] * 100)
        max_money = max(max_money, money)

    print(max_money)

def baekJoon16675():
    def rockPaperScissors(M_L, M_R, T_L, T_R):
        M = [M_L, M_R]
        T = [T_L, T_R]
        R = ['S', 'R', 'P']

        if M_L == M_R:
            for i in range(len(R)):
                if M_L == R[i]:
                    if i < 2:
                        if T_L == R[i + 1] or T_R == R[i + 1]:
                            return "TK"
                    else:
                        if T_L == R[0] or T_R == R[0]:
                            return "TK"
        if T_L == T_R:
            for i in range(len(R)):
                if T_L == R[i]:
                    if i < 2:
                        if M_L == R[i + 1] or M_R == R[i + 1]:
                            return "MS"
                    else:
                        if M_L == R[0] or M_R == R[0]:
                            return "MS"

        return "?"

    M_L, M_R, T_L, T_R = input().split()
    print(rockPaperScissors(M_L, M_R, T_L, T_R))

def baekJoon17413():
    S = list(input())

    pass_str = False
    change_str = []

    for idx, s in enumerate(S):
        if s == '<':
            for j in change_str[::-1]:
                print(j, end='')
            change_str = []
            print(s, end='')
            pass_str = True
        elif s == '>':
            print(s, end='')
            pass_str = False
        elif pass_str:
            print(s, end='')
            continue
        elif s == ' ':
            for i in change_str[::-1]:
                print(i, end='')
            print(s, end='')
            change_str = []
        else:
            change_str.append(s)

    if len(change_str) > 0:
        for i in change_str[::-1]:
            print(i, end='')

if __name__ == "__main__":
    baekJoon17413()