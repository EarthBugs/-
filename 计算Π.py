from random import *
from math import *
from time import *
from paint import *

prepaint()

Amount_Of_Dots=int(input("请输入采样精度（整数）："))
Hits=0
for i in range(1,Amount_Of_Dots):
    x=random()
    y=random()
    if(sqrt(x**2+y**2)<=1):
        Hits+=1
        paint(x,y,1)
    else:paint(x,y,0)
print("Π≈"+str((Hits/Amount_Of_Dots)*4))