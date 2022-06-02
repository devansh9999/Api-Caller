from Module import main
from multiprocessing import Process
from Module import ProgressBar
import datetime

datetime1 = datetime.datetime.now()

def Run(url,key):
    procs=[]
    for i in range(5):
        procs.append(Process(target=main.starter,args=(url,key)))
    ProgressBar.printProgressBar(0, 5, prefix = 'Progress:', suffix = 'Complete', length = 50)
    for proc in procs:
        proc.start()
    i=0
    for proc in procs:
        proc.join()
        i+=1
        ProgressBar.printProgressBar(i, 5, prefix = 'Progress:', suffix = 'Complete', length = 50)