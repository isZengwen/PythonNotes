import threading, time

class MyThread(threading.Thread):
    def __init__(self, arg):
        super(MyThread, self).__init__()
        self.arg = arg
    def run(self):
        time.sleep(2)
        print("The arg for this thread is {}".format(self.arg))

for i in range(1,5):
    t = MyThread(i)
    t.start()
    t.join()

print("All Done")