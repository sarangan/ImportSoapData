#!/usr/bin/python

import threading
import time
import urllib
import os
import re

exitFlag = 0

class myThread (threading.Thread):
    def __init__(self, synid):
        self.synid = synid
        threading.Thread.__init__(self)
    def run(self):
        print "Starting " + self.synid
        print_group(self.synid)
        print "Exiting " + self.synid

def print_group(synid):
    uf=urllib.urlopen("http://localhost/nusoapAlpha/samples/man.php?synid="+synid)
    fo=open("group.txt","ab")
    fo.write(re.sub('<[^<]+?>', '', uf.read()))
    fo.close()
    time.sleep(3)
    
    
        
