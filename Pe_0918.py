
# input
"""num = input("숫자를 입력하세요")
print("number", int(num)) """

# type 객체의 자료형이 어떤것이냐
""" a = 12
print(type(a))
a = 54.82
print(type(a))
a = "a"
print(type(a))
a = "abcd"
print(type(a))
a = [1, 2, 3]
print(type(a)) """

# 혛변환
""" a = 65
print(str(a))
print(int(a))
print(hex(a)) #hex는 int 값으로
print(oct(a))
print(chr(a)) # chr은 정수ASCLL 코드 자주 쓰는 코드값이 매칭되어있음 a~특수문자까지
print(ord("A")) #ord는 문자열 """

# pow 제곱함수
""" print(pow(2, 2))
print(pow(2, 6))
print(pow(3, 4))
print(3 ** 4) """

# divmod = (몫, 나머지)로 나온다
""" print(divmod(10, 3)) """

# round = 반올림
""" print(round(3.14))  """

# list, tuple = 리스틑와 튜플로 바꾼다
""" a = (3, 5, 7)
b = list(a)
c = tuple(a)
print(b)
print(c)
print(type(a))
print(type(b))
print(type(c)) """

 # range = 범위 설정
""" for i in range(2, 7):
    print(i) 

for i in range(1, 28, 3):  # 1부터 28까지 3단위로 범위설정
    print(i) """
    
# max, min, sum = 최댓값, 최소값, 총합
""" a = [3, 5, 6, 9]
print(max(a))
print(min(a))
print(sum(a)) """

# abs = 절대값
""" print(abs(-3))
print(abs(-3.8))
print(abs(3.0)) """

# sorted = 오름차순 정렬
""" a = [5, 3, 1, 9, 4]
print(sorted(a))
print(sorted(a, reverse=True)) """ 

# enumerate
""" a = [5, 3.14, False, 9, "string" ]
print(enumerate(a))
print(*enumerate(a)) """

# zip = (enumerate와 비슷)
""" a = [1, 2, 3]
b = [4, 5, 6]
print(zip(a, b))
print(*zip(a, b)) """

# any, all
""" a = [True, True, False]
b = [True, True, True]
print(any(a))
print(all(a)) #모두가 True여야 True나옴
print(all(b)) """

# forment = 한문장으로 만든다
""" a = 20
b = 23
c = "a는 {}, b는{}".format(a, b, "python")
print(c) """

# globals, locals, dir
""" a = 3
print(globals())
print(locals())

print(dir(a)) """

#labda 함수 = 익명함수로, 간단한 작업을 수행하는 함수를 간결하게 정의할 때 사용합니다
""" add = lambda a, b : a + b
print(add(2, 3))

sub = lambda a, b : a - b
print(sub(5, 3))

mul = lambda a, b : a * b
print(mul(2, 3))

div = lambda a, b : a / b
print(div(6, 3)) """

# 사용자 정의 함수
""" def add_numbers(x, y):
    return x + y

# 함수 호출
result = add_numbers(4, 5)
print(result) 

def greet(name):
    print(name)
    print("Hello, " + name + ". how are you?")
greet("python")"""

# 매개변수(Parameters), 인자(arguments)
""" def add(a, b) : 
	print(a + b)

def sub(a, b) :
	return a - b

def mul() :
	return 2 * 4

def div() :
	print(4 / 2)

add(3, 5)
print(sub(3, 5))
print(mul())
div() """

# 입력받은 수가 짝수/홀수인지 판별하는 함수
""" def function(n):
    if n % 2 == 0:
        print("짝수")
    else:
        print("홀수")
        
num = input("숫자를 입력하세요")
function(int(num)) """
      
# 문자열을 입력받아 문자열 반대로 출력하는 함수
""" def function(s):
    return s [::-1]
    
in_str = input("문자를 입력하세요: ")
print(function(in_str)) """

# 두 수를 입력 받아 사칙연산 결과 출력하는 함수
""" def add(a, b) : 
	return int(a) + int(b)

def sub(a, b) :
	return int(a) - int(b)

def mul(a, b) : 
	return int(a) * int(b)

def dir(a, b) :
	return int(a) / int(b)

a = input("a를 입력하세요: ")
b = input("b를 입력하세요: ")

print("더하기: ", add(a, b))
print("빼기: ", sub(a, b))
print("곱하기: ", mul(a, b))
print("나누기: ", dir(a, b)) """
 
# 위에꺼 변형
""" def calc(a, b) : 
    print (int(a) + int(b))
    print (int(a) - int(b))
    print (int(a) * int(b))
    print (int(a) / int(b))
    
a = input("a를 입력하세요: ")
b = input("b를 입력하세요: ")
    
calc(a, b) """

# 5개의 숫자를 입력받아 총합을 출력하는 함수
def sum_num(num):
    return sum(num)
nums = []

for i in range(1, 6):
    innum = int(input(f"(i)번째 숫자입력 : "))
    nums.append(innum)
    
print(sum_num(nums))




