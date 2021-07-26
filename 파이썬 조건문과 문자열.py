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
# mystr = "a man goes into the room..."
def Excercis_21():
    mystr = "a man goes into the room..."
    print(mystr.strip("."))

# Exercise 22. 문자열 다루기 (strip)
# 주식 종목을 나타내는 종목코드에 공백과 줄바꿈 기호가 포함되어 있다. 공백과 잘바꿈 기호를 제거하고 종목코드만을 추출하라.
# code = '         000660\n            '
# 출력: '000660'
def Excercis_22():
    code = '         000660\n            '
    print(code.strip(' \n'))

# Exercise 23. 문자열 다루기 (count)
# 다음 문자열에서 'Python' 문자열의 빈도수를 출력하라.
# python_desc = "Python is an interpreted high-level programming language for general-purpose programming. Created by Guido van Rossum and first released in 1991, Python has a design philosophy that emphasizes code readability, notably using significant whitespace."
# 출력 예: 2
def Excercis_23():
    python_desc = "Python is an interpreted high-level programming language for general-purpose programming. Created by Guido van Rossum and first released in 1991, Python has a design philosophy that emphasizes code readability, notably using significant whitespace."
    count = python_desc.count("Python")
    print(count)

# Exercise 24. 문자열 다루기 (count)
# 다음 문자열에서 'p' 문자가 몇번 나오는지 빈도수를 출력하라.
# python_desc = "Python is an interpreted high-level programming language for general-purpose programming. Created by Guido van Rossum and first released in 1991, Python has a design philosophy that emphasizes code readability, notably using significant whitespace."
# 출력 예: 9
def Excercis_24():
    python_desc = "Python is an interpreted high-level programming language for general-purpose programming. Created by Guido van Rossum and first released in 1991, Python has a design philosophy that emphasizes code readability, notably using significant whitespace."
    count = python_desc.count("p")
    print(count)

# Exercise 25. 문자열 다루기 (문자열 인덱싱)
# letters 라는 변수에 들어 있는 문자열에서 두 번째와 네 번째 문자를 출력하라
# letters = "python"
# 출력 예:
# y
# h
def Excercis_25():
    letters = "python"
    print(letters[1])
    print(letters[3])

# Exercise 26. 문자열 다루기 (문자열 인덱싱)
# letters 라는 변수에 사용자로부터 문자열을 입력받아서 문자 n 이 들어있는지를 출력하라 ( n 이 들어 있으면 0, 안들어있으면 -1을 출력하라)
def Excercis_26():
    letters = input("입력해주세요: ")
    if letters.find("n") >= 0:
        print ("0")
    else:
        print ("-1")

# Exercise 27. 문자열 다루기 (문자열 인덱싱)
# letters 라는 변수에 사용자로부터 문자열을 입력받아서 문자 n 이 들어있는지를 출력하라
# n 이 들어 있으면 'n 이 들어있습니다.', 안들어있으면 'n 이 안들어있습니다.' 를 출력하라
def Excercis_27():
    letters = input("입력해주세요: ")
    if letters.find("n") >= 0:
        print("n 이 들어있습니다.")
    else:
        print("n 이 안들어있습니다.")

# Exercise 28. 문자열 다루기 (문자열 인덱싱)와 조건문
# 주민등록번호의 뒷 자리 7자리 중 두번째부터 세번째는 출생 지역 코드입니다.
# 다음 표를 참조하여 사용자로부터 주민 등록 번호를 입력 받은 후 출생지를 출력하세요.
# 지역 코드	출생 지역
# 00 ~ 08	서울
# 09 ~ 12	부산
def Excercis_28():
    inputStr = input("주민등록번호를 입력해주세요: ")
    inputStr = int(inputStr[8:10])
    print(inputStr)
    if inputStr >= 0 and inputStr <= 8:
        print ("서울")
    elif inputStr >= 9 and inputStr <= 12:
        print ("부산")
    else:
        print("알수없습니다.")


# Exercise 29. 문자열 다루기 (split)
# letters 라는 변수에 Dave,David,Andy,2222,3123123,LLL 가 들어있다. 해당 변수값을 , 를 기준으로 분리해서 출력하라
# 출력 예: 
# Dave
# David
# Andy
# 2222
# 3123123
# LLL
def Excercis_29():
    letters = "Dave,David,Andy,2222,3123123,LLL"
    lettersList = letters.split(",")
    for letter in lettersList:
        print(letter)

# Exercise 30. 문자열 다루기 (split)
# 다음과 같은 파일 이름(확장자 포함)에서 확장자를 제거한 파일 이름만 출력하세요.
# filename = 'exercise01.docx'
def Excercis_30():
    filename = 'exercise01.docx'
    print(filename.split(".")[0])

if __name__ == '__main__':
    Excercis_30()