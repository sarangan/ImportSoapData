from soapthread import *
import time
import fileinput

t0 = time.time()
synlist=[]
for line in fileinput.input(["Missed_syn.txt"]):
    synid = line.split(';')
    if len(synid[0])>=0:
        if synid[0].find("itsla") == -1:  
            synlist.append(synid[0])
            #print synid[0] + "\n"
        else:
            print "itsla here! " + synid[0] +  "\n"
    
#synlist = ['940210-8378','510705-5906','951230-8694','941128-2479','470901-6036']
threads=[]
i=0
mycon=0

#while 1==1:
for item in synlist:
    i += 1
    if i >=mycon and i < mycon+100:
        x = myThread(item)
        threads.append(x)
        x.start()
    


for t in threads:
    t.join()
    #mycon +=10

print "Exiting the Main thread\n"
print time.time()-t0
