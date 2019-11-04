"""
扫描椭圆转换算法
"""

import matplotlib.pyplot as plt
import math
def main():
    a = int(input("please input the length of ellipse: "))
    b = int(input("please input the short radius of ellipse: "))
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.set(xlim=[-a-b,a+b], ylim = [-a-b,a+b])
    MidpointEllipse(a,b)
    plt.show()
def MidpointEllipse(a,b):
    x=0
    y=b
    d1 = b*b+a*a*(-b+0.25)
    plt.scatter(x,y,color='red')
    while b*b*(x+1)<a*a*(y-0.5):
        if d1<0:
            d1+=b*b*(2*x+3)
            x+=1
        else:
            d1+=(b*b*(2*x+3)+a*a*(-2*y+2))
            x+=1
            y-=1
        plt.scatter(x,y,color='red')
        plt.scatter(-x,y,color='red')
        plt.scatter(-x,-y,color='red')
        plt.scatter(x,-y,color='red')

    d2 = math.sqrt(b*(x+0.5)+math.sqrt(a*(y-1))-math.sqrt(a*b))
    while y>0:
        if d2<0:
            d2+=b*b*(2*x+2)+a*a*(-2*y+3)
            x+=1
            y-=1
        else:
            d2+=a*a*(-2*y+3)
            y-=1
        plt.scatter(x,y,color='red')
        plt.scatter(-x,y,color='red')
        plt.scatter(-x,-y,color='red')
        plt.scatter(x,-y,color='red')
main()

