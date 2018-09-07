import _thread as thread
import time
import threading

def loop1():
    print("Start loop 1 at:", time.ctime())
    time.sleep(4)
    print("End loop 1 at:", time.ctime())



def loop2():
    print("Start loop 2 at:", time.ctime())
    time.sleep(2)
    print("End loop 2 at:", time.ctime())






def loop3(in1):
    print("loop3 start at:", time.ctime())
    print("arg is: ", in1)
    time.sleep(4)
    print("loop3 end at:", time.ctime())


def loop4(in1, in2):
    print("loop4 start at:", time.ctime())
    print("arg is: ", in1, in2)
    time.sleep(2)
    print("loop4 end at:", time.ctime())

def main():
    t1 = threading.Thread(target=loop3, args=('sb1',))
    t1.start()

    t2 = threading.Thread(target=loop4, args=('sb2','sb3'))
    t2.start()

    t1.join()
    t2.join()

    print("All Done at:", time.ctime())




if __name__ == '__main__':
    main()