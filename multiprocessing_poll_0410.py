# -*- coding: utf-8 -*-
# @version : Python3.6
# @Time    : 2017/4/10 15:20
# @Author  : Jianyang-Hu
# @contact : jianyang1993@163.com
# @File    : multiprocessing_poll_0410.py
# @Software: PyCharm

#进程池内部维护一个进程序列,当使用时，则去进程池中获取一个进程，如果进程池序列中没有可供使用的进进程，
# 那么程序就会等待，直到进程池中有可用进程为止。

"""
    方法:

    apply(func[, args[, kwds]]) ：使用arg和kwds参数调用func函数，结果返回前会一直阻塞，
    由于这个原因，apply_async()更适合并发执行，另外，func函数仅被pool中的一个进程运行。

    apply_async(func[, args[, kwds[, callback[, error_callback]]]]) ： apply()方法的一个变体，
    会返回一个结果对象。如果callback被指定，那么callback可以接收一个参数然后被调用，当结果准备好回调时会调用callback，
    调用失败时，则用error_callback替换callback。 Callbacks应被立即完成，否则处理结果的线程会被阻塞。

    close() ： 阻止更多的任务提交到pool，待任务完成后，工作进程会退出。

    terminate() ： 不管任务是否完成，立即停止工作进程。在对pool对象进程垃圾回收的时候，会立即调用terminate()。

    join() : wait工作线程的退出，在调用join()前，必须调用close() or terminate()。
    这样是因为被终止的进程需要被父进程调用wait（join等价与wait），否则进程会成为僵尸进程

进程池中有两个方法：

    apply
    apply_async

"""

from multiprocessing import Pool, TimeoutError
import time
import os


def f(x):
    return x * x


if __name__ == '__main__':
    # 创建4个进程
    with Pool(processes=4) as pool:

        # 打印 "[0, 1, 4,..., 81]"
        print(pool.map(f, range(10)))

        # 使用任意顺序输出相同的数字，
        for i in pool.imap_unordered(f, range(10)):
            print(i)

        # 异步执行"f(20)"
        res = pool.apply_async(f, (20,))  # 只运行一个进程
        print(res.get(timeout=1))  # 输出 "400"

        # 异步执行 "os.getpid()"
        res = pool.apply_async(os.getpid, ())  # 只运行一个进程
        print(res.get(timeout=1))  # 输出进程的 PID

        # 运行多个异步执行可能会使用多个进程
        multiple_results = [pool.apply_async(os.getpid, ()) for i in range(4)]
        print([res.get(timeout=1) for res in multiple_results])

        # 是一个进程睡10秒
        res = pool.apply_async(time.sleep, (10,))
        try:
            print(res.get(timeout=1))
        except TimeoutError:
            print("发现一个 multiprocessing.TimeoutError异常")

        print("目前，池中还有其他的工作")

    # 退出with块中已经停止的池
    print("Now the pool is closed and no longer available")
