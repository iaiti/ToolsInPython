#-*- coding:utf-8 -*-	

#this is a comment

# Script Name : FunctionAndArgs
# Author : iaiti
# Created : 2015-7-27 16:45:04
# Description : use argv and function to return something

#use sys package argv feature
from sys import argv
#create a function to return 
def myfun(*args):
	arg1 ,arg2 = args
	print arg1,arg2
	return arg2+arg1

#get the input 
a,b,c = argv
d = myfun(b,c)
print d





