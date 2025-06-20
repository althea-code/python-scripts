import psutil
import platform
from datetime import datetime
import os

#create a logs directory if needed
LOG_DIR = "logs" 
os.makedirs(LOG_DIR, exist_ok=True)                                                     

#log filename
timestamp = datetime.now().strftime("%d/%m/%Y, %H:%M:%S")                               
log_file = os.path.join(LOG_DIR, f"system_metrics_{timestamp}.log")

#collect system information
system = platform.system()                                                              
node = platform. node()
release = platform.release()
boot_time = datetime.fromtimestamp(psutil.boot_time()).strftime('%Y-%m-%d %H:%M:%S')

#collect metrics
cpu_usage = psutil.cpu_percent(interval=1)
mem = psutil.virtual_memory()
disk = psutil.disk_usage('/')
net = psutil.net_io_counters()

#format log
log = f"""

System Report

==============

Timestamp : {timestamp}
System : {system} {release}
Hostname : {node}
Boot Time : {boot_time}

CPU Usage : {cpu_usage}
Mem Usage : {mem.percent}% ({mem.used // (1024**2)}MB used of {mem.total // (1024**2)}MB)
Disk Usage : {disk.percent}% ({disk.used // (1024**3)}GB used of {disk.total // (1024**3)}GB)
Network I/O : Sent = {net.bytes_sent // (1024**2)}MB, Received = {net.bytes_recv // (1024**2)}MB

"""

#Print
print(log)





