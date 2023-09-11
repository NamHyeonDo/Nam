#집합 리스트 차이점 중복, 정렬 X
""" my_set = {1, 2, 3, 4, 5}
setItem = {5, 3, 1} """

""" my_set = {5, 8, 3, 7, 1, "h"}
print(my_set)
print(*my_set)

my_set = set([5, 8, 3, 7, 1, "h"])
print(my_set)

set_tmp = set("hello")
print(set_tmp)"""

# |, .union = 합집합
""" my_set = {5, 8, 3, 7, 1, "h"}
set_item = {7, 8, 4, 2, "h"}
print(my_set | set_item) 
print(my_set.union(set_item))  """

# &, .intersection = 차집합
""" my_set = {5, 8, 3, 7, 1, "h"}
set_item = {7, 8, 4, 2, "h"}
print(my_set | set_item)
print(my_set & set_item) 
print(my_set.intersection(set_item))  """

# .add, .update = 추가
""" my_set = {5, 8, 3, 7, 1, "h"}
print(my_set)
my_set.add(9)
print(my_set)

my_set = {5, 8, 3, 7, 1, "h"}
print(my_set)
my_set.update([5, 9, 7, 4])
print(my_set) """

# .clear() = 전체삭제
""" my_set = {5, 8, 3, 7, 1, "h"}
print(my_set)
my_set.clear() """

# .remove, .discard = 삭제, 없는 요소 삭제시 프로그램 다운 or 그냥 넘어가기
""" my_set = {5, 8, 3, 7, 1, "h"}
print(my_set)
my_set.remove(5)
print(my_set)
my_set = {5, 8, 3, 7, 1, "h"}
print(my_set)
my_set.discard(2)
print(my_set) """

# .difference_update = 공통된 요소 삭제
""" my_set = {5, 8, 3, 7, 1, "h"}
set_item = {7, 8, 4, 2, "h"}
print(my_set)
my_set.difference_update(set_item)
print(my_set) """

# 타입변환 (정수형인데 스틸링형 or 리스트나 등등)
""" my_int = 10
my_str = str(my_int)
print(my_str) """

""" my_int = 10
print(my_int)
print(my_int + 10) """

# 변환진행
""" my_int = 10
print(my_int)
print(my_int + 10)
my_str = str(my_int)
print(my_str) """

""" # print(my_str + 10) 
print(my_str + " hello") """

# 문자열을 정수로 변환
""" my_str = '10'
my_int = int(my_str)
print(my_int) """

""" my_str = '10'
print(my_str)
my_int = int(my_str)
print(my_int)

print(my_int + 10)

my_int2 = int(my_str)
print(my_int2) """



# 연사자와 표현

# 사칙연산
""" a = 10
b = 3
print(a + b)    
print(a - b)    
print(a / b)    
print(a * b)   
print(a // b)   
print(a % b)   
print(a ** b)  """  

# 할당연상자
""" a = 0
print(a)

a += 2
print(a)

a -= 1
print(a)

a *= 4
print(a)

a /= 2
print(a)

a **= 3
print(a) """

# 비교, 관계 연산자
""" a = 10
b = 4

print(a > b)    
print(a < b)    
print(a >= b)   
print(a <= b)   
print(a != b)    """

# 논리 연산자
""" x = True
y = False

print(x and y)  
print(x or y)   
print(not x)    
print(not y)   """  

# 비트 연산자
a = 10
b = 3
print(a & b)   
print(a | b)   
print(a ^ b)   
print(~a)      
print(a << 2)  

#
my_list = [9, 4, 3, 7, 8, 'hi']
print(4 in my_list)

print(2 in my_list)
print(2 not in  my_list)

my_dic = {"key1" : "v1", "k2" : "v2"}
print("k" in my_dic)