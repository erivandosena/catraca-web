#!/usr/bin/python

from threading import Thread
from time import sleep, ctime, time
from dispositivos import sensor, leitor

#exitFlag = 0

class ThreadCatraca(Thread):

    def __init__(self, threadID, name):
        Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        #self.delay = delay

    def run(self):
        print "Starting " + self.name
        #sensor.ler_sensores()
        leitor.ler_cartao()
        
        #print_time(self.name, 1)
        #print "Exiting " + self.name

def print_time(threadName, delay):
    while True:
        #if exitFlag:
        #    thread.exit()
        sleep(delay)
        print "%s: %s" % (threadName, ctime(time()))
        #counter -= 1

