#!/usr/bin/python3


# set html environment ##

import cgi,cgitb
import sys
from subprocess  import Popen, PIPE
import sys
from check_background  import is_running
from check_background import is_log
cgitb.enable()  #enable cgi debug 


print ("Content-Type: text/html; charset=utf-8\n\n");


#print "Content-type:text/html\r\n\r\n"
print ("<html>")
print ("<head>")
#print "<title>COS lookup </title>"
print ("</head>")
print ("<body>")
print ("Job Status<br>")
#print "<h2>Hello %s %s</h2>" % (mas, mas1)
print ("</body>")
print ("</html>")

form = cgi.FieldStorage()
mas =form.getvalue("log")




# end html environment ##
is_running(b"run.sh")





