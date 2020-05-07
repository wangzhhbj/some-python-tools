monitor process CPU & mem


usage: process_monitor [-h] [--mem_accuracy MEM_ACCURACY]

                       [--cpu_accuracy CPU_ACCURACY] [--pid PID] [--dir DIR]
                       
                       [--time TIME] [--interval INTERVAL]

monitor cpu & mem. version:0.1beta


optional arguments:

  -h, --help            show this help message and exit
  
  --mem_accuracy MEM_ACCURACY
  
                        mem accuracy.(MB,default: 1024MB )
                        
  --cpu_accuracy CPU_ACCURACY
  
                        cpu accuracy.( cpu_percent, default: 100.0 )
                        
  --pid PID             process pid.(KB,default: current process pid )
  
  --dir DIR             out file path.(default: "." )
  
  --time TIME           How long to monitor.(seconds,default: forever )
  
  --interval INTERVAL   time interval.(seconds, 1--300s, default: 1s )
  
