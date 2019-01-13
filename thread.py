import threading
import time


def func(i):
    print("我是第%s个进程,开始时间是%s" % (i + 1, time.ctime()))
    time.sleep(2)  # 子程序等2秒。。
    print("我是第%s个进程,结束时间是%s" % (i + 1, time.ctime()))


threads = [threading.Thread(target=func, args=(i,)) for i in range(5)]
# print(threads)
for t in threads:
    # t.setDaemon(True)
    t.start()
    # threads[0].setDaemon(True)
# threads[4].join(1)
print('program is end')
