import time
#装饰器，打印当前时间
def printTime(f):
    def wrapper(*args,**kwargs):
        print("Time:",time.ctime())
        return f(*args,**kwargs)
    return wrapper

@printTime
def hellow():
    print("hellow world")

hellow()