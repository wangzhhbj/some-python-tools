#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
'''=================================================
@Project -> File   ：test -> test
@Author ：Mr. Wang
@Date   ：2020.3.24 22:00:00
@Email  : wangzhhbj@163.com
@Desc   ：
=================================================='''

import sys
import re
import timeit

class entry_object():
    max_latency = 0   #最大延迟
    avg_latency = 0.0   #平均延迟
    total_num = 0     #总次数
    
    total_time = 0   #总耗时
    
    latency0 = 0  # 0
    latency2 = 0  # 1 - 2
    latency4 = 0  # 2 - 4
    latency6 = 0  # 4 - 6
    latency8 = 0  # 6 - 8
    latency10 = 0 # 8 - 10
    latency20 = 0 # 10 - 20
    latency40 = 0 # 20 - 40
    latency60 = 0 # 40 - 60
    latency80 = 0 # 60 - 80
    latency100 = 0 # 80 - 100
    latency200 = 0 # 100 - 200
    latency400 = 0 # 200 - 400
    latency600 = 0 # 400 - 600
    latency800 = 0 # 600 - 800
    latency1000 = 0 # 800 - 1000
    latency2000 = 0 # 1000 - 2000
    latency4000 = 0 # 2000 - 4000
    latency6000 = 0 # 4000 - 6000
    latency8000 = 0 # 6000 - 8000
    latency10000 = 0 # 8000 - 10000
    latency20000 = 0 # 10000 - 20000
    latency40000 = 0 # 20000 - 40000
    latency60000 = 0 # 40000 - 60000
    latency80000 = 0 # 60000 - 80000
    latency100000 = 0 # 80000 - 100000
    latency_out_range = 0 # out of range
    
    
    def __init__(self,
        name = "Unknown",
        #min_latency_init = sys.maxint   #最小延迟初始化,python2
        min_latency_init = sys.maxsize,  #最小延迟,python3
        mode = "Unknown"):
        self.name = name #分析项名称
        self.min_latency  = min_latency_init #初始化最小延迟
        self.mode = mode; #模式信息
    
    def print_self(self):
        total_num = float(self.total_num) #python2除法无法计算小数，需要转换一下
        if self.total_num > 0:
            self.avg_latency = self.total_time / total_num
            if 1 == self.total_num :
                self.min_latency = self.max_latency
        else :
            self.min_latency = 0 #没有该项
        
        print(  ""
                " *************    %s:(%s)    ************* \n"
                "|---------------------------------------------------------------\n"
                "|                      max_latency : %d                         \n"
                "|---------------------------------------------------------------\n"
                "|                      min_latency : %d                         \n"
                "|---------------------------------------------------------------\n"
                "|                      avg_latency : %f                         \n"
                "|---------------------------------------------------------------\n"
                "|                      total_num   : %d                         \n"
                "|---------------------------------------------------------------\n"
                "|                      total_time  : %d                         \n"
                "|---------------------------------------------------------------"
                % 
                (self.name, self.mode,
                 self.max_latency,
                 self.min_latency,
                 self.avg_latency,
                 self.total_num,
                 self.total_time))

        if self.total_num <= 0:
            print("\n")
            return

        percent = 0.0
        sum_percent = 0.0
        print(  "|distribution        number        percent(%)       sum_percent(%)\n"
                "|---------------------------------------------------------------"
             )
        if self.latency0 :
            percent = self.latency0 * 100 / total_num
            sum_percent += percent
            print(  "|0               :   %d             %.2f               %.2f    " %
                 (self.latency0, percent, sum_percent))
        if self.latency2 :
            percent = self.latency2 * 100 / total_num
            sum_percent += percent
            print(  "|1-2             :   %d             %.2f               %.2f    " %
                 (self.latency2, percent, sum_percent))
        if self.latency4 :
            percent = self.latency4 * 100 / total_num
            sum_percent += percent
            print(  "|2-4             :   %d             %.2f               %.2f    " %
                 (self.latency4, percent, sum_percent))
        if self.latency6 :
            percent = self.latency6 * 100 / total_num
            sum_percent += percent
            print(  "|4-6             :   %d             %.2f               %.2f    " %
                 (self.latency6, percent, sum_percent))
        if self.latency8 :
            percent = self.latency8 * 100 / total_num
            sum_percent += percent
            print(  "|6-8             :   %d             %.2f               %.2f    " %
                 (self.latency8, percent, sum_percent))
        if self.latency10 :
            percent = self.latency10 * 100 / total_num
            sum_percent += percent
            print(  "|8-10            :   %d             %.2f               %.2f    " %
                 (self.latency10, percent, sum_percent))
        if self.latency20 :
            percent = self.latency20 * 100 / total_num
            sum_percent += percent
            print(  "|10-20           :   %d             %.2f               %.2f    " %
                 (self.latency20, percent, sum_percent))
        if self.latency40 :
            percent = self.latency40 * 100 / total_num
            sum_percent += percent
            print(  "|20-40           :   %d             %.2f               %.2f    " %
                 (self.latency40, percent, sum_percent))
        if self.latency60 :
            percent = self.latency60 * 100 / total_num
            sum_percent += percent
            print(  "|40-60           :   %d             %.2f               %.2f    " %
                 (self.latency60, percent, sum_percent))
        if self.latency80 :
            percent = self.latency80 * 100 / total_num
            sum_percent += percent
            print(  "|60-80           :   %d             %.2f               %.2f    " %
                 (self.latency80, percent, sum_percent))
        if self.latency100 :
            percent = self.latency100 * 100 / total_num
            sum_percent += percent
            print(  "|80-100          :   %d             %.2f               %.2f    " %
                 (self.latency100, percent, sum_percent))
        if self.latency200 :
            percent = self.latency200 * 100 / total_num
            sum_percent += percent
            print(  "|100-200         :   %d             %.2f               %.2f    " %
                 (self.latency200, percent, sum_percent))
        if self.latency400 :
            percent = self.latency400 * 100 / total_num
            sum_percent += percent
            print(  "|200-400         :   %d             %.2f               %.2f    " %
                 (self.latency400, percent, sum_percent))
        if self.latency600 :
            percent = self.latency600 * 100 / total_num
            sum_percent += percent
            print(  "|400-600         :   %d             %.2f               %.2f    " %
                 (self.latency600, percent, sum_percent))
        if self.latency800 :
            percent = self.latency800 * 100 / total_num
            sum_percent += percent
            print(  "|600-800         :   %d             %.2f               %.2f    " %
                 (self.latency800, percent, sum_percent))
        if self.latency1000 :
            percent = self.latency1000 * 100 / total_num
            sum_percent += percent
            print(  "|800-1000        :   %d             %.2f               %.2f    " %
                 (self.latency1000, percent, sum_percent))
        if self.latency2000 :
            percent = self.latency2000 * 100 / total_num
            sum_percent += percent
            print(  "|1000-2000       :   %d             %.2f               %.2f    " %
                 (self.latency2000, percent, sum_percent))
        if self.latency4000 :
            percent = self.latency4000 * 100 / total_num
            sum_percent += percent
            print(  "|2000-4000       :   %d             %.2f               %.2f    " %
                 (self.latency4000, percent, sum_percent))
        if self.latency6000 :
            percent = self.latency6000 * 100 / total_num
            sum_percent += percent
            print(  "|4000-6000       :   %d             %.2f               %.2f    " %
                 (self.latency6000, percent, sum_percent))
        if self.latency8000 :
            percent = self.latency8000 * 100 / total_num
            sum_percent += percent
            print(  "|6000-8000       :   %d             %.2f               %.2f    " %
                 (self.latency8000, percent, sum_percent))
        if self.latency10000 :
            percent = self.latency10000 * 100 / total_num
            sum_percent += percent
            print(  "|8000-10000      :   %d             %.2f               %.2f    " %
                 (self.latency10000, percent, sum_percent))
        if self.latency20000 :
            percent = self.latency20000 * 100 / total_num
            sum_percent += percent
            print(  "|10000-20000     :   %d             %.2f               %.2f    " %
                 (self.latency20000, percent, sum_percent))
        if self.latency40000 :
            percent = self.latency40000 * 100 / total_num
            sum_percent += percent
            print(  "|20000-40000     :   %d             %.2f               %.2f    " %
                 (self.latency40000, percent, sum_percent))
        if self.latency60000 :
            percent = self.latency60000 * 100 / total_num
            sum_percent += percent
            print(  "|40000-60000     :   %d             %.2f               %.2f    " %
                 (self.latency60000, percent, sum_percent))
        if self.latency80000 :
            percent = self.latency80000 * 100 / total_num
            sum_percent += percent
            print(  "|60000-80000     :   %d             %.2f               %.2f    " %
                 (self.latency80000, percent, sum_percent))
        if self.latency100000 :
            percent = self.latency100000 * 100 / total_num
            sum_percent += percent
            print(  "|80000-100000    :   %d             %.2f               %.2f    " %
                 (self.latency100000, percent, sum_percent))
        if self.latency_out_range :
            percent = self.latency_out_range * 100 / total_num
            sum_percent += percent
            print(  "|100000+         :   %d             %.2f               %.2f    " %
                 (self.latency_out_range, percent, sum_percent))
        print("\n")



'''
 *******************************************************************************************************
'''



def analysis_relist(re_list, ob_entry, entry_position, time_position):
    
    time = int(re_list[time_position])
    if time < 0 : #小于0认为是无效数据
        return
    
    ob_entry.total_num += 1
    ob_entry.total_time += time
    
    if (time > ob_entry.max_latency) :
        ob_entry.max_latency = time
    elif (time < ob_entry.min_latency) :
        ob_entry.min_latency = time
    
    if time <= 10 :
        if time <= 2 :
            if 0 == time :
                ob_entry.latency0 += 1
            else :
                ob_entry.latency2 += 1;
        elif time <= 4 :
            ob_entry.latency4 += 1;
        elif time <= 6 :
            ob_entry.latency6 += 1;
        elif time <= 8 :
            ob_entry.latency8 += 1;
        else:
            ob_entry.latency10 += 1;
    elif time <= 100 :
        if time <= 20 :
            ob_entry.latency20 += 1;
        elif time <= 40 :
            ob_entry.latency40 += 1;
        elif time <= 60 :
            ob_entry.latency60 += 1;
        elif time <= 80 :
            ob_entry.latency80 += 1;
        else:
            ob_entry.latency100 += 1;
    elif time <= 1000 :
        if time <= 200 :
            ob_entry.latency200 += 1;
        elif time <= 400 :
            ob_entry.latency400 += 1;
        elif time <= 600 :
            ob_entry.latency600 += 1;
        elif time <= 800 :
            ob_entry.latency800 += 1;
        else :
            ob_entry.latency1000 += 1;
    elif time <= 10000 :
        if time <= 2000 :
            ob_entry.latency2000 += 1;
        elif time <= 4000 :
            ob_entry.latency4000 += 1;
        elif time <= 6000 :
            ob_entry.latency6000 += 1;
        elif time <= 8000 :
            ob_entry.latency8000 += 1;
        else :
            ob_entry.latency10000 += 1;
    elif time <= 100000 :
        if time <= 20000 :
            ob_entry.latency20000 += 1;
        elif time <= 40000 :
            ob_entry.latency40000 += 1;
        elif time <= 60000 :
            ob_entry.latency60000 += 1;
        elif time <= 80000 :
            ob_entry.latency80000 += 1;
        else :
            ob_entry.latency100000 += 1;
    else:
        ob_entry.latency_out_range += 1;
    
    

def print_entry_dict(entry_dict) :
    for k in entry_dict.keys() :
        entry_dict[k].print_self()



'''
file：要分析的文件
entry_position：项的位置
time_position：耗时位置
mode：模式信息
'''
def analysis_file( file, entry_position, time_position , mode):
    entry_dict = {} #创建一个字典，用来存项数
    position_tmp = entry_position + 1
    
    if entry_position < time_position :
        position_tmp = time_position + 1
    
    with open(file,'r') as f:
        for line in f.readlines():
            #去除换行，同时兼容linux和windows
            re_list = re.split(',', line.replace('\n', '').replace('\r', ''))
            
            #判断项数是否足够
            if len(re_list) < position_tmp :
                continue
            
            #判断时间项是否为数字
            if not re_list[time_position].isdigit() :
                continue
            
            #匹配到已有的项
            if re_list[entry_position] not in entry_dict:
                # 新的项
                new_entry = entry_object(name = re_list[entry_position],
                                         min_latency_init = int(re_list[time_position]),
                                         mode = mode)
                entry_dict[re_list[entry_position]] = new_entry
            
            analysis_relist(re_list,
                            entry_dict[re_list[entry_position]],
                            entry_position,
                            time_position)
    
    return entry_dict

'''
file：要分析的文件
entry_position：项的位置
time_position：耗时位置
mode：模式信息
target_name：目标信息
'''
def analysis_file_target_entry( file, entry_position, time_position , mode, target_list):
    if 0 == len(target_list) :
        return {}

    entry_dict = {} #创建一个字典，用来存项数
    for entry in target_list : 
        # 新的项
        new_entry = entry_object(name = entry,
                                 mode = mode)
        entry_dict[entry] = new_entry

    position_tmp = entry_position + 1
    if entry_position < time_position :
        position_tmp = time_position + 1
        
    with open(file,'r') as f:
        for line in f.readlines():
            #去除换行，解决linux和windows
            re_list = re.split(',', line.replace('\n', '').replace('\r', ''))
            
            #判断项数是否足够
            if len(re_list) < position_tmp :
                continue
            
            #检查是否在字典中,且判断时间项是否为数字
            if ((re_list[entry_position] in entry_dict) 
                and re_list[time_position].isdigit()):
                analysis_relist(re_list,
                                entry_dict[re_list[entry_position]],
                                entry_position,
                                time_position)
    return entry_dict


if __name__ == "__main__":
    if len(sys.argv) < 4 :
        print("Version : 0.91beta \n"
              "Note    : support python3 & python2.7 \n"
              "please input file path & entry position &time position\n\n"
              "   : <python command>  <filepath>   <entry_position> <time_position> [mode] [target_list]\n"
              "eg1: <python command>  nfsd_io.log        2             3                                \n"
              "eg2: <python command>  nfsd_io.log        2             3             us                 \n"
              "eg3: <python command>  nfsd_io.log        2             3             us    nfsd_dispatch\n"
              "eg4: <python command>  nfsd_io.log        2             3             us    nfsd_create,nfsd_write\n"
             )
        exit(-1)
    
    start = timeit.default_timer()
    
    mode = "Unknown"
    if len(sys.argv) >= 5:
        mode = sys.argv[4]
    
    print( "\n    analyzing \"%s\" , Please wait a moment  \n\n" % (sys.argv[1]))
    
    if len(sys.argv) >= 6:
        #查找指定项目
        target_list = re.split(',', sys.argv[5])
        entry_dict = analysis_file_target_entry(sys.argv[1], int(sys.argv[2]) - 1, int(sys.argv[3]) - 1, mode, target_list)
        print_entry_dict(entry_dict)
    else :
        #自动分析所有项目
        entry_dict = analysis_file(sys.argv[1], int(sys.argv[2]) - 1, int(sys.argv[3]) - 1, mode)
        print_entry_dict(entry_dict)
    
    end = timeit.default_timer()
    
    print( "takes %s seconds\n" % (str(end-start)))
    exit(0)
