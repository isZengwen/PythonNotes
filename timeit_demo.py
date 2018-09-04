import timeit
#测量代码块的执行时间
c ='''
sum=[]
for i in range(0,1000):
    sum.append(i)
'''
t1 = timeit.timeit(stmt="[i for i in range(0,1000)]",number=100000)
t2 = timeit.timeit(stmt=c,number=100000)
print(t1,t2)
print("#"*20)


#测量不含参数函数的执行时间
def doIt():
    n = 3
    for i in range(n):
        print(i)
t3 = timeit.timeit(stmt=doIt,number=10)
print(t3)


#测量含参数的函数执行时间
s = '''
def doIt(n):
    for i in range(n):
        pass
'''
t4 = timeit.timeit("doIt(n)",setup=s+"n=3",number=100000)
print(t4)