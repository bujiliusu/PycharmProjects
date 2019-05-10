import os
from multiprocessing import Process
import os, time, random

from multiprocessing import Pool

from multiprocessing import Queue

# def run_proc(name):
#     print 'Child process %s (%s) Running...' % (name,os.getpid())
#
# if __name__ == '__main__':
#     print 'Parent process %s.' %  os.getpid()
#     for i in range(5):
#         p = Process(target=run_proc,args=(str(i),))
#         print 'Process will start'
#         p.start()
#     p.join()
#     print 'Process end'

# print '*'*80
# def run_task(name):
#     print 'Task %s (pid = %s) is running...' %(name, os.getpid())
#     time.sleep(random.random() * 3)
#     print 'Task %s end.' %name
# if __name__ == '__main__':
#     print 'Parent process %s.' %  os.getpid()
#     p = Pool(processes=3)
#     for i in range(5):
#         p.apply_async(run_task,args=(i,))
#     print 'Waiting for all subprocesses done...'
#     p.close()
#     p.join()
#     print 'All subprocesses done.'
def proc_write(q,urls):
    print ('Process (%s) is running...' % os.getpid())
    for url in urls:
        q.put(url)
        print ('Put %s to quene...' % url)
        time.sleep(random.random())
def proc_read(q):
    print ('Process (%s) is running...' % os.getpid())
    while True:
        url = q.get(True)
        print ('Get %s from quene.' % url)
if __name__ == '__main__':
    q = Queue()
    proc_write1 = Process(target=proc_write, args=(q,['url_1', 'url_2', 'url_3']))
    proc_write2 = Process(target=proc_write, args=(q,['url_4', 'url_5', 'url_6']))
    proc_reader = Process(target=proc_read, args=(q,))
    proc_write1.start()
    proc_write2.start()
    proc_reader.start()
    proc_write1.join()
    proc_write2.join()
    proc_reader.terminate()