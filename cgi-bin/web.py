#!/usr/bin/python

import cgi 
import cgitb
cgitb.enable()

print "Content-type: text/html"
print 
print "<html>Hello, Welcome to Mas's Presidential prediction system 2016</html>"


form = cgi.FieldStorage()

print """\
<div><img src="http://motleymoose.net/wp-content/uploads/2015/05/Election2016.png"></div>
<form  method=post >
 </br> May I have your name?:<br>
  <input type="text" name="firstname"><br>
<!--  Last name:<br>
  <input type="text" name="lastname"> -->
<input type="submit" value="Submit">
</form>
"""

hap = form.getfirst("firstname", "")
#hap1 = form.getfirst("lastname", "").upper()
sum = "I can speak  3 different lanaguages"
if hap == "" :
    print "Enter your name"
else: 

    print ("Oh hey %s , how are you?" % hap )
    print ("<br>My prediction is that Donald Trump will win the presidential election for 2016 , sorry ")
    print ("<br>Also did you know that %s" % str(sum) + ". Have a great day " + hap)

