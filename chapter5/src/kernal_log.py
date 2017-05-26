"""
@ file  :  kernal_log.py
@ brief :Read kernel logs and write it to a file with name log-<date>-<time>.log """
from datetime import datetime
import os
file1 = open("test","w")
os.system("dmesg >> test")
print datetime.now().strftime('mylogfile->time->%H_%M_ date->%d_%m_%Y.log')
'mylogfile->08_48_04_02_2012.log'

