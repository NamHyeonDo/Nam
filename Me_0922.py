# callback 함수 = 함수를 쓸 때(호출) 해준다, (fx) 중요 

""" def prt_func() :
    print("hello")

def callfunc(fx) :
		fx()

callfunc(prt_func) """

""" def prt_func(n) :
    print("hello", n)

def callfunc(fx) :
    for i in range(5):		
        fx(i)
        
callfunc(prt_func) """

""" def update_msg(name: str) -> list:
    msg = []
    msg.append("Hello, " + name)
    msg.append("Bye, " + name)
    return msg

def greeting(in_name: str) -> list:
    gt_msg = None
    gt_msg = update_msg(in_name)
    return gt_msg 

res = greeting("python")

for message in res:
    print(message) """
    
# 재귀함수 = 함수 내에서 자기 자신을 호출하는 함수
""" def fun(n) :
    if n == 5 :
        return
    
    print(1, n)
    fun(n+1)
    
fun(1) """

# !5
""" def ploop(n):
    if n == 0:
        print("end")
        return 1
    else :
        print (n, n-1, "=", n + n-1)
        return n * ploop(n-1)
print(ploop(5)) """

# 피보나치 수열
""" def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        print(n)
        return fibonacci  """
        
# 모듈


# 사용자 정의 모듈
""" import calc
print(calc.add(1, 1))
print(calc.sub(1, 1))
print(calc.mul(1, 1))
print(calc.div(1, 1))

print(dir(calc)) """

""" import calc as cl
print(cl.add(1, 1))
print(cl.sub(1, 1))
print(cl.mul(1, 1))
print(cl.div(1, 1)) """

# 구조화 = 모듈은 모듈끼리 소스파일은 소스파일끼리, mod 사용
""" import mod.circle_mod as cm
print(cm.pi)
print(cm.cc_area(4))
print(cm.cc_len(5)) """

""" def cutword(st, wd, idx):
    tmp = st.split(wd)
    res = tmp [idx]
    return res

url = "https://www.notion.so/test/4-1/a1fe5ef0df1/41f7a1aa9ec01/3a859a"
res = smod.cutword(url, "/", 4)
print(res) """

""" import mod.circle_mod as smod
url = "https://www.notion.so/test/4-1/a1fe5ef0df1/41f7a1aa9ec01/3a859a"
res = smod.cutword(url, "/", 3)
print(res) """ # 어려움

# math 사용
""" import mod.utils as mu

res = mu.mt_sqrt(6)   
print(res)

sin = mu.mt_sin(math.pi / 2)
print(sin)

el = mu.mt_elog(math.e)
print(el)

ep = mu.mt_ep(3)
print(ep)

pi_res = mu.mt_pi
print(pi_res)

fc_res = math.factorial(4)
print(fc_res) """

# 랜덤함수

import random as rd
res = rd.randint(1, 100)
print(res)

my_list = ["apple", "banana", "cherry"]
lres = rd.choice(my_list)
print(lres)

fres = rd.random()
print(fres)

nvres = rd.normalvariate()
print(nvres)