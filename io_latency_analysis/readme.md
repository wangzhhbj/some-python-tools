
a tool to analysis latency，support python3 & python2.7

可以快速的帮助开发者分析函数的总耗时，平均耗时，执行次数等。能获取到函数耗时的分布情况，百分比。

```
please input file path & entry position &time position
Note: support python3 & python2.7 
:<python command>  <filepath>   <entry_position> <time_position> [mode] [target_name_list]
eg1: <python command>  nfsd_io.log        2             3                                
eg2: <python command>  nfsd_io.log        2             3             us                 
eg3: <python command>  nfsd_io.log        2             3             us    nfsd_dispatch
eg4: <python command>  nfsd_io.log        2             3             us    nfsd_dispatch,nfs_write
```

#python analysis_time.py nfs_io.log 2 3 us

out输出示范：
```
 *************    vfs_writev:(us)    ************* 
|---------------------------------------------------------------
|                      max_latency : 9651                         
|---------------------------------------------------------------
|                      min_latency : 10                         
|---------------------------------------------------------------
|                      avg_latency : 20.077030                         
|---------------------------------------------------------------
|                      total_num   : 200000                         
|---------------------------------------------------------------
|                      total_time  : 4015406                         
|---------------------------------------------------------------
|distribution        number        percent(%)       sum_percent(%)
|---------------------------------------------------------------
|8-10            :   4             0.00               0.00    
|10-20           :   142075             71.04               71.04    
|20-40           :   55585             27.79               98.83    
|40-60           :   1305             0.65               99.48    
|60-80           :   406             0.20               99.69    
|80-100          :   197             0.10               99.79    
|100-200         :   270             0.14               99.92    
|200-400         :   98             0.05               99.97    
|400-600         :   24             0.01               99.98    
|600-800         :   16             0.01               99.99    
|800-1000        :   6             0.00               99.99    
|1000-2000       :   7             0.00               100.00    
|2000-4000       :   6             0.00               100.00    
|8000-10000      :   1             0.00               100.00
```
