#!/usr/bin/env python3

import re
import subprocess
import os

def is_running(process):
    global found
    s = subprocess.Popen(["pgrep", process],stdout=subprocess.PIPE)
    while True:
        found = s.stdout.readline().decode('utf-8')
        break
   # check = int(found)
    try:
        os.kill(int(found), 0)
        print("Your Job/Process id is " + str(found))
        print(".The Job is running")
        print("<br><input type=\"button\" value=\"Close this window\" onclick=\"self.close()\">")
    except:
        print("Job has been completed or terminated. Please check the log output")
        print("<br><input type=\"button\" value=\"Close this window\" onclick=\"self.close()\">")

#is_running(b"run.sh")


def is_log(file):
    read = open(file, 'r')
    for i in read:
        print(i)
    read.close()
