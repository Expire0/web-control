#!/usr/bin/python3

### run a backgroup process and send the stout to a file.   Use the file for a status update and delete 
### http://stackoverflow.com/questions/1996518/retrieving-the-output-of-subprocess-call

# set html environment ##

import cgi,cgitb
import sys
from subprocess  import Popen, PIPE
import sys
from check_background  import is_running
cgitb.enable()  #enable cgi debug 


print ("Content-Type: text/html; charset=utf-8\n\n");
#mas = input("Enter model: ")
#mas1 = input("Service Type: ")

form = cgi.FieldStorage()
mas =form.getvalue("checking")
argv1 = str(mas)



#print "Content-type:text/html\r\n\r\n"
print ("<html>")
print ("<head>")
#print "<title>COS lookup </title>"
print ("</head>")
print ("<body>")
print ("Processing your request. Depending on the batch side. Please wait 5-10 min and use the check progress option<br>")
#print "<h2>Hello %s %s</h2>" % (mas, mas1)
print ("</body>")
print ("</html>")



# end html environment ##

## command to run 
app = "./run.sh"


## run background process

code= Popen([app, argv1 ],stdout=PIPE, stderr=PIPE)
while True:
    line = code.stdout.readline().decode('utf-8')
    file = open('../html/log/check.txt','w+')

    if "log" in line:
        file.write(line)
        print("<div> <b>Your log file is:" +line+ ", Please make a note of it. </b></div>")
       # print("Batch received\n")
    break
file.close()
## check if process is running
is_running(b"run.sh")

