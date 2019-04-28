#! /usr/bin/env python3

import cgi
import cgitb
cgitb.enable()

f = open("src/syusyoku_nayamu_neet_man.png","rb")
print("Content-Type: text/html")
# print("Content-Type: image/jpeg")
print("")

print("<html><body>")
print(f.read())
print(result)
print("</body><html>")