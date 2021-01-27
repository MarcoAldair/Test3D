"""
Intersection example
"""
import matplotlib.pyplot as plt 
import numpy as np
from math import sin, cos, radians,sqrt
import tools3d 

#______Coordenadas iniciales
xg=[]
yg=[]
zg=[]

#Cordenadas centrales
xc=80
yc=40
zc=40

#Plano y linea de sistema
x=[40,30,80]
y=[60,10,60]
z=[-10,10,10]

def llenarglobales():
    for i in range(len(x)):
        xg.append(x[i]+xc)
        yg.append(y[i]+yc)
        zg.append(z[i]+zc)

#____Plotear el sistema 
#def plotPlaneLine(xg,yg,zg,xh,yh,xhg,yhg,hitcolor):
def plotPlaneLine(xg,yg,zg,A,A1,A2):
    plt.axis([0,300,150,0])
    plt.axis('on')
    plt.grid(False)
    plt.plot([xg[0],xg[1]],[yg[0],yg[1]],color='k')#plano
    plt.plot([xg[1],xg[2]],[yg[1],yg[2]],color='k')
    plt.plot([xg[0],xg[2]],[yg[0],yg[2]],color='k')
    plt.plot([xg[0],xg[3]],[yg[0],yg[3]],color='k',linestyle='dashed')
    plt.plot([xg[1],xg[3]],[yg[1],yg[3]],color='k',linestyle='dashed')
    plt.plot([xg[2],xg[3]],[yg[2],yg[3]],color='k',linestyle='dashed')
    plt.scatter(xg[3],yg[3],color='r')

    plt.text(20,75,int(A))
    plt.text(30,75,int(A1))
    plt.text(40,75,int(A2))
    #plt.text(30,100,A1)
    #plt.text(40,100,A2)
    if (A1+ A2) > A:
        plt.text(50,100,'Fuera')
    if (A1+ A2) < A:
        plt.text(50,100,'Dentro')

    plt.show()

def hitpoint(x,y,z):
    #_____distance point 0 to 1
    a=x[0]-x[1]
    b=y[0]-y[1]
    c=z[0]-z[1]
    Q01=sqrt(a*a+b*b+c*c)
    a=x[1]-x[2]
    b=y[1]-y[2]
    c=z[1]-z[2]
    Q12=sqrt(a*a+b*b+c*c)
    a=x[0]-x[2]
    b=y[0]-y[2]
    c=z[0]-z[2]
    Q02=sqrt(a*a+b*b+c*c)
    s = (Q01+Q12+Q02)/2
    A = sqrt(s*(s-a)*(s-b)*(s-c))
    print(A)
    a=x[0]-x[3]
    b=y[0]-y[3]
    c=z[0]-z[3]
    Q01=sqrt(a*a+b*b+c*c)
    a=x[3]-x[2]
    b=y[3]-y[2]
    c=z[3]-z[2]
    Q12=sqrt(a*a+b*b+c*c)
    a=x[0]-x[2]
    b=y[0]-y[2]
    c=z[0]-z[2]
    Q02=sqrt(a*a+b*b+c*c)
    s = (Q01+Q12+Q02)/2
    A1 = sqrt(s*(s-a)*(s-b)*(s-c))
    a=x[0]-x[1]
    b=y[0]-y[1]
    c=z[0]-z[1]
    Q01=sqrt(a*a+b*b+c*c)
    a=x[1]-x[3]
    b=y[1]-y[3]
    c=z[1]-z[3]
    Q12=sqrt(a*a+b*b+c*c)
    a=x[0]-x[3]
    b=y[0]-y[3]
    c=z[0]-z[3]
    Q02=sqrt(a*a+b*b+c*c)
    s = (Q01+Q12+Q02)/2
    A2 = sqrt(s*(s-a)*(s-b)*(s-c))
    return A,A1,A2


while True:
    axis=input("Ingrese s para ingresar las coordenadas o el num control para salir ?:")
    if axis == '18390579':
        break
    if axis == 's':
        hx = int(input('coordenada x hitpoint: '))
        hy = int(input('coordenada y hitpoint: '))
        x.append(hx)
        y.append(hy)
        z.append(-10)
        llenarglobales()
        A,A1,A2 = hitpoint(x,y,z)
        plotPlaneLine(xg,yg,zg,A,A1,A2)
