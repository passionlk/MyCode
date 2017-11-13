#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep  2 23:48:11 2017

@author: passionlk
"""
#Regular Expression for a shot
import re
s = 'Hello from csev@umich.edu to cwen@iupui.edu about the meeting @2PM'
lst = re.findall('\S+@\S+', s)
print (lst)

#Create a random integer 
import random
random.randint(5, 10)



import socket
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
mysock.connect(('www.py4inf.com', 80))
mysock.send('GET http://www.py4inf.com/code/romeo.txt HTTP/1.0\r\n\r\n')

while True:
    
    data = mysock.recv(512)
    
    if ( len(data) < 1 ) :
        break
    
    print (data)
    
mysock.close()



import urllib

fhand = urllib.request.urlopen('http://www.py4inf.com/code/romeo.txt')
for line in fhand:
    line.strip()
    print (line.strip())
    
import tkinter
top = tkinter.Tk()
# 进入消息循环
top.mainloop()


















   
   
   
   
   

   