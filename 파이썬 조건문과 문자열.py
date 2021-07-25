# Exercise 12. 기본 자료형
# 10, 2.2, "fun-coding" 각각을 변수에 넣고, 각 데이터 타입을 출력하세요.
def Excercis_12():
    val_1 = 10
    val_2 = 2.2
    val_3 = "fun-coding"
    print(type(val_1))
    print(type(val_2))
    print(type(val_3))

# Exercise 13. 기본 자료형
# 다음 코드를 실행해보고 \t와 \n의 역할을 설명하세요.
# code = '000660\n00000102\t12312312'
# print (code)
def Excercis_13():
    code = '000660\n00000102\t12312312'
    print(code)
    print()
    print("개행과 탭 문자를 쓰고 있다.\n\\n는 개행문자 \\t는 탭이다.")

# Exercise 14. 조건문
# 사용자로부터 두 개의 숫자를 입력 받은 후 큰 숫자를 화면에 출력하세요.
def Excercis_14():
    num1 = int(input("num1: "))
    num2 = int(input("num2: "))
    print("더 큰 숫자는: ")
    if num1 > num2:
        print(num1)
    else:
        print(num2)

# Exercise 15. 조건문
# 사용자로부터 입력 받은 숫자가 홀수인지 짝수인지 출력하세요.
def Excercis_15():
    num = int(input("num: "))
    if num % 2 == 0: 
        print("입력받은 숫자 {0}는 짝수 입니다.".format(num))
    else:
        print("입력받은 숫자 {0}는 홀수 입니다.".format(num))

# Exercise 16. 조건문
# 사용자로부터 세 개의 숫자를 입력 받은 후 가장 작은 숫자를 출력하세요.
def Excercis_16():
    print("숫자를 입력해주세요: ", end='')
    num = list(map(int, input().split()))
    num.sort()
    print(num)
    print("가장 작은 숫자는: {0}".format(num[0]))

# Exercise 17. 조건문
# 사용자로부터 점수를 입력 받은 후 등급을 출력하라.
# (A: 100 ~ 81, B: 80 ~ 61, C: 60 ~ 0)
def Excercis_17():
    num = int(input("점수를 입력해주세요: "))
    if 100 >= num and num >= 81:
        print("A등급 입니다.")
    elif 80 >= num and num >= 61:
        print("B등급 입니다.")
    elif 60 >= num and num >= 0:
        print("C등급 입니다.")
    else:
        print("알수 없는 등급 입니다.")

# Exercise 18. 데이터 구조 (리스트)
# 사용자로부터 주민등록번호를 입력받아 출생 연도를 출력하세요.
# 예) 800001-1231231 주민번호를 입력받으면 80을 출력하면 됨
def Excercis_18():
    strNumber = input("주민번호를 입력해주세요: ")
    print("출생연도는: ", strNumber[0:2])

# Exercise 19. 데이터 구조 (리스트)
# 사용자로부터 주민등록번호를 입력받아 뒷자리 맨 앞의 숫자를 출력하세요.
# 주민등록번호 뒷자리 맨 앞자리는 성별을 나타냄
# 예) 800001-1231231 주민번호를 입력받으면 1을 출력하면 됨
# 1은 남성을 의미, 2는 여성을 의미, 최근 아이들은 3과 4를 사용함
def Excercis_19():
    strNumber = input("주민번호를 입력해주세요: ")
    print("주민번호 뒷자리의 맨 앞자리 번호는: ", strNumber[7])

# Exercise 20. 데이터 구조 (리스트)
# 사용자로부터 주민등록번호를 입력받아, 성별을 '남성' 또는 '여성'으로 출력하세요.
# 주민등록번호 뒷자리 맨 앞자리는 성별을 나타냄
# 예) 800001-1231231 주민번호를 입력받으면 1을 출력하면 됨
# 1이면 남성, 2이면 여성을 출력하면 됨 (최근 아이들은 3과 4를 사용하지만 이 경우는 고려하지 않기로 함)
def Excercis_20():
    strNumber = input("주민번호를 입력해주세요: ")
    gender = strNumber[7]
    if gender == "1":
        print("남성입니다.")
    elif gender == "2":
        print("여성입니다.")
    else:
        print("알수없습니다.")

# Exercise 21. 문자열 다루기 (strip)
# 다음 문자열에서 ...를 제거하라.
def Excercis_21():
    print()

if __name__ == '__main__':
    Excercis_20()