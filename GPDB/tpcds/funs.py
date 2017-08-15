#coding: utf-8

import multiprocessing
import subprocess
import os
import paramiko
from pyDOE import *
from numpy import *
from tran import *

'''
功能函数
'''

# 数据库连接信息
user = 'tenant'
database = 'testDB'
host = '192.168.100.78'

# 查询映射
query_dict = {
1:17, 2:25, 3:26, 4:32, 5:33,
6:61, 7:62, 8:65, 9:71, 10:20
}

# 执行shell root命令
def sshclient(host,user,passwd,strcomd):
    str_host = host
    print str_style(str_host, fore = 'green')
    # paramiko.util.log_to_file('paramiko.log')  
    s = paramiko.SSHClient()
    s.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    s.connect(hostname = host,username=user, password=passwd)
    stdin, stdout, stderr = s.exec_command(strcomd)
    print stdout.read()
    s.close()

# 清空集群中所有节点的缓存
def clear_cache():
    user = 'root'
    passwd = 'jipeng1008'
    strcmd = 'sync; echo 1 > /proc/sys/vm/drop_caches'
    print str_style('clear caches', fore = 'green')
    sshclient('JPDB2',user,passwd,strcmd)
    sshclient('node1',user,passwd,strcmd)
    sshclient('node2',user,passwd,strcmd)
    sshclient('node3',user,passwd,strcmd)
    #sshclient('node4',user,passwd,strcmd)
    sshclient('node5',user,passwd,strcmd)
    #sshclient('node6',user,passwd,strcmd)

def mpl2():
    print str_style("mpl2",fore="green")
    q = Queue.Queue()

	# 生成LHS
    #origin_mpl_2 = lhs(2,10)
    origin_mpl_2 = array([[0.3 , 0.5],
                    [0.9 , 0.7],
                    [0.4 , 0.10],
                    [0.8 , 0.1],
                    [0.2 , 0.8],
                    [0.1 , 0.4],
                    [0.7 , 0.2],
                    [0.10 , 0.6],
                    [0.5 , 0.9],
                    [0.6 , 0.3]])
    mpl_2 = ceil(origin_mpl_2*10)
    print mpl_2

    for r in range(10):
        print mpl_2[r]
        # 两个并行的不相等得查询
        if mpl_2[r][0] == mpl_2[r][1]:
            continue
        #print int(mpl_2[r][c])
        #print query_dict[int(mpl_2[r][c])]

        # primary query
        query_file = "query"+str(query_dict[int(mpl_2[r][0])])+".sql"
        query_file = "/home/gpdba/DBtest/GPDB/tpcds/IO-bound/"+query_file
        print query_file
        #p1 = TranClass(q, user,database,host,query_file)
        p1 = multiprocessing.Process(target=exec_sql,args=(q,user,database,host,query_file))
        p1.start()

        # concurrent query
        query_file = "query"+str(query_dict[int(mpl_2[r][1])])+".sql"
        query_file = "/home/gpdba/DBtest/GPDB/tpcds/IO-bound/"+query_file
        print query_file
        #p2 = TranClass(q, user,database,host,query_file)
        p2 = multiprocessing.Process(target=exec_sql,args=(q,user,database,host,query_file))
        p2.start()

        # 并行执行
        p1.join()
        p2.join()
        
        # 存入文件
        fp = open("res_queries/"+"mix"+str(r)+".txt","a")
        while not q.empty():
            fp.write(q.get())
        fp.close()

        # 清空队列
        with q.mutex:
            q.queue.clear()
        #break
    
def mpl3():
    print str_style("mpl3",fore="green")

def mpl4():
    print str_style("mpl4",fore="green")

def mpl5():
    print str_style("mpl5",fore="green")

def str_style(string, mode = '', fore = '', back = ''):
    STYLE = { 
        'fore':
        {   # 前景色
            'black'    : 30,   #  黑色
            'red'      : 31,   #  红色
            'green'    : 32,   #  绿色
            'yellow'   : 33,   #  黄色
            'blue'     : 34,   #  蓝色
            'purple'   : 35,   #  紫红色
            'cyan'     : 36,   #  青蓝色
            'white'    : 37,   #  白色
        },  

        'back' :
        {   # 背景
            'black'     : 40,  #  黑色
            'red'       : 41,  #  红色
            'green'     : 42,  #  绿色
            'yellow'    : 43,  #  黄色
            'blue'      : 44,  #  蓝色
            'purple'    : 45,  #  紫红色
            'cyan'      : 46,  #  青蓝色
            'white'     : 47,  #  白色
        },  

        'mode' :
        {   # 显示模式
            'mormal'    : 0,   #  终端默认设置
            'bold'      : 1,   #  高亮显示
            'underline' : 4,   #  使用下划线
            'blink'     : 5,   #  闪烁
            'invert'    : 7,   #  反白显示
            'hide'      : 8,   #  不可见
        },  

        'default' :
        {   
            'end' : 0,
        },  
    }   
    mode  = '%s' % STYLE['mode'][mode] if STYLE['mode'].has_key(mode) else ''
    fore  = '%s' % STYLE['fore'][fore] if STYLE['fore'].has_key(fore) else ''
    back  = '%s' % STYLE['back'][back] if STYLE['back'].has_key(back) else ''
    style = ';'.join([s for s in [mode, fore, back] if s]) 
    style = '\033[%sm' % style if style else ''
    end   = '\033[%sm' % STYLE['default']['end'] if style else ''
    return '%s%s%s' % (style, string, end)

if __name__ == '__main__':
    #clear_cache()
    mpl2()   