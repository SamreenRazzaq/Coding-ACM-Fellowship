#1.Find Average of N numbers:
"""num=int(input("How many numbers: "))
total_sum=0
for n in range (num):
    numbers=float(input("Enter any number: "))
    total_sum+=numbers
avg=total_sum/num
print("Average is : ",avg)"""

#2.How to sum of the First N Positive Integers:
"""n=int(input("Enter Number:"))
sum=(n*(n+1))/2
print(sum)"""

#3.How to get time of a Pyhton program's execution:
"""import time
def myFunc():
    start_time=time.time()
    s=0
    for i in range(1,n+1):
        s=s+i
    end_time=time.time()
    return s, end_time-start_time
n=5
print(myFunc())"""

#4.How to get current username:
"""import getpass
print(getpass.getuser())"""

#5.How to get environmental variables:
"""import os
print(os.environ['PATH'])"""

#6.How to do a Profile a Python script:
"""import cProfile
def sum():
    print(1,3)
cProfile.run('sum()')"""

#7.How to List all Files of a Directory:
"""from os import listdir
from os.path import isfile,join
files_list=[f for f in listdir('/Users')if isfile(join('/Users',f))]"""

#8.How to find out the version of Python you are using:
"""import sys
print("Python Version")
print(sys.version)
print(sys.version_info)"""

#9.How to print current date and time:
"""import datetime
now=datetime.datetime.now()
print("Current date and time is: ")
print(now.strftime("%y-%m-%d %H:%M:%S"))"""

#10.How to find area of circle:
"""from math import pi
r=float(input("write the radius of circle: "))
print("the area of circle is: " +str(pi*r**2))"""

