# Jason Coleman 12/19/14
# testing timestamps for optostim

import datetime, time
from scipy.io import matlab

clockstamp_total = []
timestamp_frames = []

def procedure():
    time.sleep(0.1)
    
def procedure2():
    global clockstamp_1
    time.sleep(5)
    clockstamp_1 = float(time.time())

# create a file to store stim sequence info
file_timestamps = open("file_timestamps.txt", "wb")

for i in range(10):
    #timestamp_0 = float(time.clock())
    #procedure()
    #print float(time.clock()) - timestamp_0, "seconds process time"
    
    #clockstamp_0 = float(time.time())
    #procedure()
    #print float(time.time()) - clockstamp_0, "clock timestamp"
    
    clockstamp_0 = float(time.time())
    procedure2()
    print float(clockstamp_1-clockstamp_0), "time from last process"
    h = float(clockstamp_0)
    if i==0:
        k = float(clockstamp_0)
    clockstamp_total.append(h)
    timestamp_frames.append(h-k) # elapsed time
    file_timestamps.write(str(h-k)+"\n") # write the elapsed time to a new line each loop
    
file_timestamps.close()
    
savedVariables = {"clockstamp_total": clockstamp_total, "timestamp_frames": timestamp_frames}
matlab.savemat('timestampTests.mat', savedVariables)





## measure process time
#t0 = time.clock()
#procedure()
#a=time.clock() - t0
#print time.clock() - t0, "seconds process time"
#procedure2()
#print time.clock() - a, "seconds process time"
#
## measure wall time
#t0 = time.time()
#procedure()
#print time.time() - t0, "seconds wall time"
#t02 = time.time()
#procedure2()
#print time.time() - t0, "proc2 wall time"