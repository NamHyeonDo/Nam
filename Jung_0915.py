# 식별 연산
""" x = [1, 2, 3]
y = [1, 2, 3]
z = x

print(x is y)  
print(x is z)  
print(x is not y)  

a = 5
b = 5
print(a is b) 
print(a is not b)  """ 
 
""" a = 3
b = 3.0


print(a is b) 
print(a is not b) 
print(a == b)  """

""" a = [3, 5, 1]
b = a
print(a is b)

a[0] = 2
print(a, b)
print(a is b) """

# 연산자 우선순위
""" x = 2 ** 3 ** 2
print(x)    

x = 2 + 3 * 4
print(x)  
x = 10 / 5 / 2
print(x)
x = 2** 3 **2
y = 2 ** (3 ** 2)
print(x, y)
x = 1 + 2 > 3 and 4 - 1 < 2
print (x)
x = not False and True
print(x)
x = not True or False and True
print(x)
x = 1 & 2 | 3 ^ 4
print(x)
x = 5 in [3, 4, 5] or 2 not in [1, 2, 3]
print(x)
x = 2 * -3 // 2
print(x)
x = 1 == 2 != 3
print(x) """

# 조건문과 반복문

# 조건문
""" x = 10
if x > 0:
    print("x is positive")
elif x < 0:
    print("x is negative")
else:
    print("x is zero")
 """
 
""" a = 10
if a % 2 == 1 :
    print("홀수")
else :  
    print("짝수") """

""" a = 10
b = 9
if a is b:
    print("같다")
    
else :
    print("다르다") """
    
""" x = b
if x is a:
    print("a 입니다")
elif x is b:
    print("b 입니다")
else :
    print("아무것도 입니다") """
    
# 반복문
""" fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

my_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

for row in my_list:
    for num in row:
        print(num)
     """

""" for i in range(10):
    print(i) """

""" for char in "python":
    print(char) """
    
""" fruits = ["apple", "banana", "cherry"]

for fruit in reversed(fruits):
    print(fruit) 
    
for fruit in sorted(fruits): # sorted 둘은 같다 reversed=True
    print(fruit)  """
    
""" for i in range(1, 10):
    for j in range(1, 10):
        print(i, "*", j, "=", i*j) """
        
# for ~ else 문
""" rang = [5, 8, 3, 1, 6]
for i in rang:
	print("element : ", i)
else :
	print("end process")     """
    
""" for i in range(10):
    if i == 7:
        print("break", i)
        break
    elif i == 1:
        print("continue", i)
        continue
    else:
        print("pass", i)
        pass
    print(i)
 """
 
# while 문
""" i = 1
while i <= 5:
    print(i)
    i += 1 """
    
""" i = 0  
while i <= 10:
    print(i)
    i += 1 """
    
""" word = "love"
idx = 0
while idx < len(word):
    print(word[idx])
    idx += 1 """
    
""" sum = 0
i = 1
while i <= 10:
    sum += i
    i += 1
    print(sum) """
    
""" i = 1
while i <= 100:
 
    if i%2 == 0:
        print("짝수", i)
        
    else:
        print("홀수", i)
    i += 1    """ 
    
i = 1    
while i <= 100:
    if i%7 == 0:
        print(i)
    i += 1
        









