#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
'''=================================================
@Project -> process_monitor   ：test -> test
@Author ：Mr. Wang
@Date   ：2020.04.07 17:00:00
@Email  : wangzhhbj@163.com
@Desc   ：
=================================================='''

import os
import sys
import time
import psutil
import argparse

import threading #在线程中检查,主线程接收标记

import signal #信号机制不支持windows



class cls_process():
    max_mem = 0
    __running = 1
    start_time = 0
    last_time = 0
    __mark = ''
    
    def __init__(self,
        pid = os.getpid(), #进程id号
        dir = ".",
        cpu_accuracy = 100.0,
        mem_accuracy = 1024,   #内存精度
        time_long = -1,  #监控时长
        interval = 1):  #时间间隔
        
        self.errno = 1
        self.dir  = dir
        
        if cpu_accuracy <= 0.0 :
            self.cpu_accuracy = 0.0
        else :
            self.cpu_accuracy = cpu_accuracy
        
        if mem_accuracy <= 0 :
            self.mem_accuracy = 0
        else :
            self.mem_accuracy = (mem_accuracy << 20)
        
        self.time_long  = time_long
        
        if interval > 300 :
            self.interval = 300
        elif interval < 1 :
            self.interval = 1
        else :
            self.interval = interval
            
        self.__pid = pid #获取id信息
        if pid > 0 :
            self.__process = psutil.Process(pid)
            self.log = dir + '/' + self.__process.name() + '-' + str(pid) + '-' + time.strftime('%Y%m%d-%H%M%S',time.localtime(time.time())) + ".mon.csv"
            print(self.log)
            self.errno = 0
    
    def monitor_loop(self):
        if 0 == self.__running :
            return
        
        self.start_time =  time.time() #更新一下时间
        self.last_time =  self.start_time #更新一下时间
        uss_last = 0 #初始化内存信息
        cpu_last = 0.0
        
        with open(self.log, "w") as f:
            f.write("time,cpu(%),mem(%),rss(M),vms(M),uss(M),pss(M),swap(M),mark\n") # titles
            #print("time,cpu(%),mem(%),rss(M),vms(M),uss(M),pss(M),swap(M),mark\n")
            self.__mark = 'monitor start'
            while self.__running :
                rss, vms, shared, text, lib, data, dirty, uss, pss, swap = self.__process.memory_full_info()
                cpu_percent = self.__process.cpu_percent()
                mem_percent = self.__process.memory_percent()
                
                time_now = time.time()
                if ((self.time_long > 0) and 
                    (time_now - self.start_time > self.time_long)) : #判断时间是否到达
                    self.stop()
                
                print(abs(uss - uss_last) , self.mem_accuracy, abs(cpu_percent - cpu_last) , self.cpu_accuracy)
                if ((abs(uss - uss_last) < self.mem_accuracy) and #内存精度
                    (abs(cpu_percent - cpu_last) < self.cpu_accuracy) and #cpu精度
                    (self.__mark == '')):   #是否有标记
                    
                    if self.interval > 1 :
                        if (time_now - self.last_time >= self.interval) : #判断周期是否到达
                            self.last_time = time_now
                        else:
                            time.sleep(1)
                            continue #需要继续sleep
                    else :
                        self.last_time = time_now
                
                uss_last = uss
                cpu_last = cpu_percent
                
                current_time = time.strftime('%Y%m%d-%H%M%S',time.localtime(time.time()))
                
                ''' 精确到小数
                rss_str = ("%.2d" % (float(rss)/1024/1024))
                vms_str = ("%.2f" % (float(vms)/1024/1024))
                uss_str = ("%.2f" % (float(uss)/1024/1024))
                pss_str = ("%.2f" % (float(pss)/1024/1024))
                swap_str = ("%.2f" % (float(swap)/1024/1024))
                '''
                
                rss_str = ("%d" % (rss/1024/1024))
                vms_str = ("%d" % (vms/1024/1024))
                uss_str = ("%d" % (uss/1024/1024))
                pss_str = ("%d" % (pss/1024/1024))
                swap_str = ("%d" % (swap/1024/1024))
                
                if self.__mark == '' :
                    line = current_time + ',' + str(cpu_percent) + ',' + ("%.3f" % mem_percent) + ',' + rss_str + ',' + vms_str + ',' + uss_str + ',' + pss_str + ',' + swap_str
                else :
                    line = current_time + ',' + str(cpu_percent) + ',' + ("%.3f" % mem_percent) + ',' + rss_str + ',' + vms_str + ',' + uss_str + ',' + pss_str + ',' + swap_str + ',' + self.__mark
                    self.__mark = ''
                #print (line)
                f.write(line + "\n")
                
                time.sleep(1)
                
                
        print("mon exit, name: %s, pid:%d" % (self.__process.name(), self.__pid))

    def stop(self) :
        self.__mark = 'monitor exit'
        self.__running = 0
    
    def mark(self, mark) :
        if self.__mark == '' :
            print( time.strftime('%Y%m%d-%H%M%S',time.localtime(time.time())) + " mark: " + mark)
            self.__mark = str(mark)
        else :
            print( time.strftime('%Y%m%d-%H%M%S',time.localtime(time.time())) + " Overwrite old mark: " + self.__mark + ", new mark:" + mark)
            self.__mark = str(mark)

# 自定义信号处理函数
def signal_handler(signum, frame):
    print("\n\nPlease wait a moment, Preparing to exit\n")
    global ob_process
    if ob_process is not None :
        ob_process.stop()
    global mon_thread
    if mon_thread is not None :
        mon_thread.join() #等待子线程结束
    print("monitor exit\n")
    sys.exit(0)


ob_process = None
mon_thread = None
parser = argparse.ArgumentParser( prog="process_monitor",
                                         description='monitor cpu & mem. version:0.1beta' )
parser.add_argument( '--mem_accuracy', dest='mem_accuracy', #精度
                        type=int, default=1024,
                        help='mem accuracy.(MB,default: 1024MB )' )
parser.add_argument( '--cpu_accuracy', dest='cpu_accuracy', #精度
                        type=float, default=100.0,
                        help='cpu accuracy.( cpu_percent, default: 100.0 )' )
parser.add_argument( '--pid', dest='pid', #进程ID号
                        type=int, default=os.getpid(),
                        help='process pid.(KB,default: current process pid )' )
parser.add_argument( '--dir', dest='dir',  #结果日志位置
                        default='.',
                        help='out file path.(default: "." )' )
parser.add_argument( '--time', dest='time',  #监控时长
                        type=int, default=-1,
                        help='How long to monitor.(seconds,default: forever )' )
parser.add_argument( '--interval', dest='interval',  #时间间隔
                        type=int, default=1,
                        help='time interval.(seconds, 1--300s, default: 1s )' )


# 设置相应信号处理的handler
signal.signal(signal.SIGINT, signal_handler)
signal.signal(signal.SIGHUP, signal_handler)
signal.signal(signal.SIGTERM, signal_handler)


if __name__ == '__main__':
    #处理参数
    argsParser = parser.parse_args( sys.argv[1:] )
    if argsParser.pid < 0 :
        parser.print_help()
        sys.exit( -1 )
    
    print("current pid:%d" % (os.getpid()))
    ob_process = cls_process(argsParser.pid, argsParser.dir, argsParser.cpu_accuracy, argsParser.mem_accuracy, argsParser.time, argsParser.interval)
    
    mon_thread = threading.Thread(target=cls_process.monitor_loop, args=(ob_process,))
    mon_thread.start()
    
    while(True):
        message = raw_input('Enter mark:')
        if ob_process is not None :
            ob_process.mark(message)
