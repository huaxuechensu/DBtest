#coding: utf-8

import multiprocessing
import subprocess
from pyDOE import *
from numpy import *

from tran import *
from funs_shell import * 

'''
功能函数
'''

# 数据库连接信息
user = 'tenant'
database = 'testDB'
host = '192.168.100.78'
query_file_path = "/home/gpdba/DBtest/GPDB/tpcds/queries/"

# 查询映射
query_dict = {
1:17, 2:25, 3:26, 4:32, 5:33,
6:61, 7:62, 8:65, 9:71, 10:20,
11:8, 12:15, 13:18, 14:22, 15:27,
16:40, 17:46, 18:56, 19:60, 20:66,
21:70, 22:79, 23:82, 24:90
}

# 独立扫描表所用时间
# 输入表名
def scan_table(table_name):
    #clear_cache()
    q = multiprocessing.Queue()

    query_sql = "set optimizer=off;explain analyze select * from " + table_name
    p = multiprocessing.Process(target=scan_sql,args=(q,user,database,host,query_sql))
    p.start()
    p.join()

    fp = open("res_queries/scan/"+ table_name +".txt","a")
    while not q.empty():
        fp.write(q.get())
    fp.close()   

# 查询单独执行
# 查询：17、20、25、26、32、33、61、62、65、71
def exec_isolation(query_sql):
    clear_cache()
    q = multiprocessing.Queue()
    query_file = query_file_path + "query"  + str(query_sql)+".sql"
    #print query_file

    # 记录时间
    p = multiprocessing.Process(target=exec_isolation,args=(q,user,database,host,query_file))
    p.start()
    p.join()

    # 保存结果
    fp = open("res_queries/isolation/query"+str(query_sql)+".txt","a")
    while not q.empty():
        fp.write(q.get())
    fp.close()
    q.close()
    
# 查询并发度为2
def mpl2():
    print str_style("mpl2",fore="green")

	# 生成LHS
    #origin_mpl_2 = lhs(2,10)
    origin_mpl_2 = array([[0.3 , 0.5],
                    [0.9 , 0.7],
                    [0.4 , 1.0],
                    [0.8 , 0.1],
                    [0.2 , 0.8],
                    [0.1 , 0.4],
                    [0.7 , 0.2],
                    [1.0 , 0.6],
                    [0.5 , 0.9],
                    [0.6 , 0.3]])
    mpl_2 = ceil(origin_mpl_2*10)
    print mpl_2

    # 10个查询组合
    for r in range(10):
        clear_cache()
        q = multiprocessing.Queue()

        print mpl_2[r]
        # 两个并行的不相等得查询
        if mpl_2[r][0] == mpl_2[r][1]:
            continue

        # primary query
        query_file1 = "query"+str(query_dict[int(mpl_2[r][0])])+".sql"
        query_file1 = query_file_path + query_file1
        print query_file1
        p1 = multiprocessing.Process(target=exec_concurrent,args=(q,user,database,host,query_file1,r))

        # concurrent query
        query_file2 = "query"+str(query_dict[int(mpl_2[r][1])])+".sql"
        query_file2 = query_file_path + query_file2
        print query_file2
        p2 = multiprocessing.Process(target=exec_concurrent,args=(q,user,database,host,query_file2,r))

        p1.start()
        p2.start()
        p1.join()
        p2.join()

        # 在主进程中结束所有collectl
        print "一个查询组合执行结束"
        end_collectl()
 
        '''
        # 由于容量的限制，下面代码移动到了exec_concurrent
        # 把每个查询组合的结果存入文件
        subprocess.check_output(['echo -------------------------- >> run.log'],shell=True)
        fp = open("res_queries/mpl2/"+"mix"+str(r)+".txt","a")
        while not q.empty():
            fp.write(q.get())
        fp.close()

        # 清空队列
        q.close()
        '''

# 查询并发度为3
def mpl3():
    print str_style("mpl3",fore="green")

	# 生成LHS
    #origin_mpl_3 = lhs(3,10)
    #'''
    origin_mpl_3 = array(
        [[ 0.1, 1.0, 0.3],
        [  0.6, 1.0, 0.2],
        [  0.7, 0.6, 0.6],
        [  0.4, 0.5, 1.0],
        [  0.9, 0.7, 0.4],
        [  0.2, 0.4, 0.9],
        [  0.8, 0.8, 0.7],
        [  1.0, 0.3, 0.1],
        [  0.3, 0.2, 0.8],
        [  0.5, 0.9, 0.5]]
    )
    #'''
    #print origin_mpl_3
    mpl_3 = ceil(origin_mpl_3*10)
    print mpl_3

    for r in range(10):
        clear_cache()
        q = multiprocessing.Queue()

        print mpl_3[r]
        # 两个并行的不相等得查询
        #if mpl_2[r][0] == mpl_2[r][1]:
        #    continue
        #print int(mpl_2[r][c])
        #print query_dict[int(mpl_2[r][c])]

        # primary query
        query_file1 = "query"+str(query_dict[int(mpl_3[r][0])])+".sql"
        query_file1 = query_file_path + query_file1
        print query_file1
        #p1 = TranClass(q, user,database,host,query_file)
        p1 = multiprocessing.Process(target=exec_sql,args=(q,user,database,host,query_file1))
        p1.start()

        # concurrent query
        query_file2 = "query"+str(query_dict[int(mpl_3[r][1])])+".sql"
        query_file2 = query_file_path + query_file2
        print query_file2
        #p2 = TranClass(q, user,database,host,query_file)
        p2 = multiprocessing.Process(target=exec_sql,args=(q,user,database,host,query_file2))
        p2.start()

        # concurrent query
        query_file3 = "query"+str(query_dict[int(mpl_3[r][2])])+".sql"
        query_file3 = query_file_path + query_file3
        print query_file3
        #p2 = TranClass(q, user,database,host,query_file)
        p3 = multiprocessing.Process(target=exec_sql,args=(q,user,database,host,query_file3))
        p3.start()

        # 并行执行
        p1.join()
        p2.join()
        p3.join()
        
        # 把每个查询组合的结果存入文件
        fp = open("res_queries/mpl3/"+"mix"+str(r)+".txt","a")
        cnt = 0;
        while not q.empty():
            cnt = cnt+1
            if cnt==1 or cnt==4 or cnt==7:
                subprocess.check_output(['echo ' + q.get() + ' >> run.log'],shell=True)
                continue
            fp.write(q.get())
        fp.close()

        # 清空队列
        q.close()
        #break

# 查询并发度为4
def mpl4():
    print str_style("mpl2",fore="green")

	# 生成LHS
    #origin_mpl_4 = lhs(4,10)
    origin_mpl_4 = array([[0.3 , 0.5],
                    [0.9 , 0.7],
                    [0.4 , 1.0],
                    [0.8 , 0.1],
                    [0.2 , 0.8],
                    [0.1 , 0.4],
                    [0.7 , 0.2],
                    [1.0 , 0.6],
                    [0.5 , 0.9],
                    [0.6 , 0.3]])
    mpl_4 = ceil(origin_mpl_4*10)
    print mpl_4

    for r in range(10):
        clear_cache()
        q = multiprocessing.Queue()

        print mpl_4[r]
        # 两个并行的不相等得查询
        #if mpl_2[r][0] == mpl_2[r][1]:
        #    continue
        #print int(mpl_2[r][c])
        #print query_dict[int(mpl_2[r][c])]

        # primary query
        query_file1 = "query"+str(query_dict[int(mpl_4[r][0])])+".sql"
        query_file1 = query_file_path + query_file1
        print query_file1
        #p1 = TranClass(q, user,database,host,query_file)
        p1 = multiprocessing.Process(target=exec_sql,args=(q,user,database,host,query_file1))
        p1.start()

        # concurrent query
        query_file2 = "query"+str(query_dict[int(mpl_4[r][1])])+".sql"
        query_file2 = query_file_path + query_file2
        print query_file2
        #p2 = TranClass(q, user,database,host,query_file)
        p2 = multiprocessing.Process(target=exec_sql,args=(q,user,database,host,query_file2))
        p2.start()

        # concurrent query
        query_file3 = "query"+str(query_dict[int(mpl_4[r][2])])+".sql"
        query_file3 = query_file_path + query_file3
        print query_file3
        #p2 = TranClass(q, user,database,host,query_file)
        p3 = multiprocessing.Process(target=exec_sql,args=(q,user,database,host,query_file3))
        p3.start()

        # concurrent query
        query_file4 = "query"+str(query_dict[int(mpl_4[r][3])])+".sql"
        query_file4 = query_file_path + query_file4
        print query_file4
        #p2 = TranClass(q, user,database,host,query_file)
        p4 = multiprocessing.Process(target=exec_sql,args=(q,user,database,host,query_file4))
        p4.start()

        # 并行执行
        p1.join()
        p2.join()
        p3.join()
        p4.join()
        
        # 把每个查询组合的结果存入文件
        fp = open("res_queries/mpl4/"+"mix"+str(r)+".txt","a")
        cnt = 0;
        while not q.empty():
            cnt = cnt+1
            if cnt==1 or cnt==4 or cnt==7 or cnt == 10:
                subprocess.check_output(['echo ' + q.get() + ' >> run.log'],shell=True)
                continue
            fp.write(q.get())
        fp.close()

        # 清空队列
        q.close()
        #break

# 查询并发度为5
def mpl5():
    print str_style("mpl5",fore="green")

	# 生成LHS
    origin_mpl_5 = lhs(5,10)
    '''
    origin_mpl_5 = array([[0.3 , 0.5],
                    [0.9 , 0.7],
                    [0.4 , 1.0],
                    [0.8 , 0.1],
                    [0.2 , 0.8],
                    [0.1 , 0.4],
                    [0.7 , 0.2],
                    [1.0 , 0.6],
                    [0.5 , 0.9],
                    [0.6 , 0.3]])
    '''
    mpl_5 = ceil(origin_mpl_5*10)
    print mpl_5

    for r in range(10):
        clear_cache()
        q = multiprocessing.Queue()

        print mpl_5[r]
        # 两个并行的不相等得查询
        #if mpl_2[r][0] == mpl_2[r][1]:
        #    continue
        #print int(mpl_2[r][c])
        #print query_dict[int(mpl_2[r][c])]

        # primary query
        query_file1 = "query"+str(query_dict[int(mpl_5[r][0])])+".sql"
        query_file1 = query_file_path + query_file1
        print query_file1
        p1 = multiprocessing.Process(target=exec_sql,args=(q,user,database,host,query_file1))
        p1.start()

        # concurrent query
        query_file2 = "query"+str(query_dict[int(mpl_5[r][1])])+".sql"
        query_file2 = query_file_path + query_file2
        print query_file2
        p2 = multiprocessing.Process(target=exec_sql,args=(q,user,database,host,query_file2))
        p2.start()

        # concurrent query
        query_file3 = "query"+str(query_dict[int(mpl_5[r][2])])+".sql"
        query_file3 = query_file_path + query_file3
        print query_file3
        p3 = multiprocessing.Process(target=exec_sql,args=(q,user,database,host,query_file3))
        p3.start()

        # concurrent query
        query_file4 = "query"+str(query_dict[int(mpl_5[r][3])])+".sql"
        query_file4 = query_file_path + query_file4
        print query_file4
        p4 = multiprocessing.Process(target=exec_sql,args=(q,user,database,host,query_file4))
        p4.start()

        # concurrent query
        query_file5 = "query"+str(query_dict[int(mpl_5[r][4])])+".sql"
        query_file5 = query_file_path + query_file5
        print query_file5
        p5 = multiprocessing.Process(target=exec_sql,args=(q,user,database,host,query_file5))
        p5.start()

        # 并行执行
        p1.join()
        p2.join()
        p3.join()
        p4.join()
        p5.join()
        
        # 把每个查询组合的结果存入文件
        fp = open("res_queries/mpl5/"+"mix"+str(r)+".txt","a")
        cnt = 0;
        while not q.empty():
            cnt = cnt+1
            if cnt==1 or cnt==4 or cnt==7 or cnt == 10 or cnt == 13:
                subprocess.check_output(['echo ' + q.get() + ' >> run.log'],shell=True)
                continue
            fp.write(q.get())
        fp.close()

        # 清空队列
        q.close()
        #break

if __name__ == '__main__':
    print "funs.py"
    
    mpl3()
