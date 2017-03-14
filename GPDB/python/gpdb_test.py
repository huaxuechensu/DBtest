#coding: utf-8

import multiprocessing
import threading
import Queue
import os
import time
import random
import subprocess  
import paramiko

from shell_color import str_style
from tran import TranClass

'''
测试多租户
'''
# 测试函数
def func(msg):
	print "msg:", msg
	time.sleep(2)
	print "end"

# 执行root命令
def sshclient(strcomd):
    hostname='192.168.100.78'
    username='root'
    password='jipeng1008'

    # paramiko.util.log_to_file('paramiko.log')  
    s = paramiko.SSHClient()

    s.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    s.connect(hostname = hostname,username=username, password=password)
    stdin, stdout, stderr = s.exec_command(strcomd)
    print stdout.read()
    s.close()

database = 'testDB'
host = '192.168.100.78'

def tenant0():
    print 'tenant0'

# 租户进程
def tenant1():
    print 'tenant1'
    user = 'tenant1'
    queue = Queue.Queue()
    strsql1 = '/home/gpadmin/DBtest/GPDB/python/queries/photoobjall-1.sql'
    strsql2 = '/home/gpadmin/DBtest/GPDB/python/queries/photoobjall-2.sql'
    strsql3 = '/home/gpadmin/DBtest/GPDB/python/queries/photoobjall-1_1.sql'

    print "tenant1 start time is: ", time.strftime("%a %b %d %Y %H:%M:%S", time.localtime())
    print str_style('tenant1 query start', fore = 'green')
    start = time.time()

	# query sql
    p1 = TranClass(queue, user,database,host,strsql1)
    p2 = TranClass(queue, user,database,host,strsql2)
    p3 = TranClass(queue, user,database,host,strsql3)
    p1.start()
    p2.start()
    p3.start()
    p1.join()
    p2.join()
    p3.join()

    end = time.time()   
    print str_style("tenant1 query completed", fore = 'green')
    print "tenant1 end time is: ",time.strftime("%a %b %d %Y %H:%M:%S", time.localtime())
    print 'tenant1 task runs %0.2f seconds.' %(end - start)

    fo = open("res_process/tenant1.txt","w+")
    while not queue.empty():
        fo.write(queue.get())
    fo.close()

# 租户进程
def tenant2():
    print 'tenant2'
    user = 'tenant2'
    queue = Queue.Queue()
    strsql1 = '/home/gpadmin/DBtest/GPDB/python/queries/photoobjall-2.sql'
    strsql2 = '/home/gpadmin/DBtest/GPDB/python/queries/photoobjall-2_1.sql'
    strsql3 = '/home/gpadmin/DBtest/GPDB/python/queries/photoobjall-3_1.sql'

    print "tenant2 start time is: ",time.strftime("%a %b %d %Y %H:%M:%S", time.localtime())
    print str_style('tenant2 query start', fore = 'green')
    start = time.time()

	# query sql
    p1 = TranClass(queue, user,database,host,strsql1)
    p2 = TranClass(queue, user,database,host,strsql2)
    p3 = TranClass(queue, user,database,host,strsql3)
    p1.start()
    p2.start()
    p3.start()
    p1.join()
    p2.join()
    p3.join()

    end = time.time()   
    print str_style("tenant2 query completed", fore = 'green')
    print "tenant2 end time is: ",time.strftime("%a %b %d %Y %H:%M:%S", time.localtime())
    print 'tenant2 task runs %0.2f seconds.' %(end - start)

    fo = open("res_process/tenant2.txt","w+")
    while not queue.empty():
        fo.write(queue.get())
    fo.close()

# 租户进程
def tenant3():
    print 'tenant3'
    user = 'tenant3'
    queue = Queue.Queue()
    strsql1 = '/home/gpadmin/DBtest/GPDB/python/queries/photoobjall-3.sql'
    strsql2 = '/home/gpadmin/DBtest/GPDB/python/queries/photoobjall-3_1.sql'
    strsql3 = '/home/gpadmin/DBtest/GPDB/python/queries/photoobjall-4_2.sql'

    print "tenant3 start time is: ",time.strftime("%a %b %d %Y %H:%M:%S", time.localtime())
    print str_style('tenant3 query start', fore = 'green')
    start = time.time()

	# query sql
    p1 = TranClass(queue, user,database,host,strsql1)
    p2 = TranClass(queue, user,database,host,strsql2)
    p3 = TranClass(queue, user,database,host,strsql3)
    p1.start()
    p2.start()
    p3.start()
    p1.join()
    p2.join()
    p3.join()

    end = time.time()   
    print str_style("tenant3 query completed", fore = 'green')
    print "tenant3 end time is: ",time.strftime("%a %b %d %Y %H:%M:%S", time.localtime())
    print 'tenant3 task runs %0.2f seconds.' %(end - start)

    fo = open("res_process/tenant3.txt","w+")
    while not queue.empty():
        fo.write(queue.get())
    fo.close()

# 租户进程
def tenant4():
    print 'tenant4'
    user = 'tenant4'
    queue = Queue.Queue()
    strsql1 = '/home/gpadmin/DBtest/GPDB/python/queries/photoobjall-4.sql'
    strsql2 = '/home/gpadmin/DBtest/GPDB/python/queries/photoobjall-4_1.sql'
    strsql3 = '/home/gpadmin/DBtest/GPDB/python/queries/photoobjall-4_2.sql'

    print "tenant4 start time is: ",time.strftime("%a %b %d %Y %H:%M:%S", time.localtime())
    print str_style('tenant4 query start', fore = 'green')
    start = time.time()

	# query sql
    p1 = TranClass(queue, user,database,host,strsql1)
    p2 = TranClass(queue, user,database,host,strsql2)
    p3 = TranClass(queue, user,database,host,strsql3)
    p1.start()
    p2.start()
    p3.start()
    p1.join()
    p2.join()
    p3.join()

    end = time.time()   
    print str_style("tenant4 query completed", fore = 'green')
    print "tenant4 end time is: ",time.strftime("%a %b %d %Y %H:%M:%S", time.localtime())
    print 'tenant4 task runs %0.2f seconds.' %(end - start)

    fo = open("res_process/tenant4.txt","w+")
    while not queue.empty():
        fo.write(queue.get())
    fo.close()

# 租户进程
def tenant5():
    print 'tenant5'
    user = 'tenant5'
    queue = Queue.Queue()
    strsql1 = '/home/gpadmin/DBtest/GPDB/python/queries/photoobjall-2.sql'
    strsql2 = '/home/gpadmin/DBtest/GPDB/python/queries/photoobjall-3.sql'
    strsql3 = '/home/gpadmin/DBtest/GPDB/python/queries/photoobjall-4.sql'

    print "tenant5 start time is: ",time.strftime("%a %b %d %Y %H:%M:%S", time.localtime())
    print str_style('tenant5 query start', fore = 'green')
    start = time.time()

	# query sql
    p1 = TranClass(queue, user,database,host,strsql1)
    p2 = TranClass(queue, user,database,host,strsql2)
    p3 = TranClass(queue, user,database,host,strsql3)
    p1.start()
    p2.start()
    p3.start()
    p1.join()
    p2.join()
    p3.join()

    end = time.time()   
    print str_style("tenant5 query completed", fore = 'green')
    print "tenant5 end time is: ",time.strftime("%a %b %d %Y %H:%M:%S", time.localtime())
    print 'tenant5 task runs %0.2f seconds.' %(end - start)

    fo = open("res_process/tenant5.txt","w+")
    while not queue.empty():
        fo.write(queue.get())
    fo.close()

if __name__ == "__main__":
    pool = multiprocessing.Pool(processes = 5)

    # 清空缓存
    print str_style('clear caches', fore = 'green')
    #sshclient('sync; echo 1 > /proc/sys/vm/drop_caches')

    '''
    # 测试pool
    for i in xrange(5):
        msg = "hello %d" %(i)
        pool.apply_async(func, (msg, ))  # 向pool中添加进程
    '''

    print str_style("main process eecution", fore = "yellow")
    start = time.time()

    for i in xrange(5):
        pool.apply_async(globals().get('tenant'+str(i)),())

    # 关闭pool，使其不再接受新的任务
    pool.close()
    # 主进程阻塞，等待子进程的退出 
    pool.join()
    end = time.time()
    print 'process run %0.2f seconds.' %(end - start)
    print str_style("Sub-process(es) done.", fore = "yellow")

