from numpy import *
from vpython import *


#Variáveis físicas
m1=0.17575
m2=0.16105
m3=0.20865
g=9.8
r0=1
tmax=5;

#Cálculo das Posições
precisao=0.12
indices=int(tmax/precisao)

tempos   = linspace(0, (indices - 1) * precisao, indices)

xpontoponto = (m1*m2-4*m2*m3+m1*m3)*g/(m1*m2+4*m2*m3+m1*m3)
ypontoponto = 2*m1*(m3-m2)*g/(m1*m2+m1*m3-4*m2*m3)

#Fator de divisão apenas para ajustar as unidades do vpython
xpontoponto=xpontoponto/100000
ypontoponto=ypontoponto/100000

a1 = -xpontoponto;
a2 = -ypontoponto + xpontoponto;
a3 = ypontoponto + xpontoponto;

#Montar a simulação 3D
canvas(visible=True,center=vector(0,-r0/1.8,0))
massa1=box(height=0.40, length=0.08,width=0.08, color = vector(1,0.752,0.329))
polia1 = ring(pos=vector(-0.1,r0,0),axis=vector(0,0,1),radius=0.1,thickness=0.01, color=0.5*vector(1,1,1))
polia2 = ring(pos=polia1.pos-vector(polia1.radius,r0,0),axis=vector(0,0,1),radius=0.1,thickness=0.01, color=0.5*vector(1,1,1))
corda1=cylinder(pos=vector(0,r0,0),axis=massa1.pos-polia1.pos-vector(polia1.radius,0,0),radius=0.01,color=vector(1,1,1))
corda2=cylinder(pos=polia2.pos+vector(0,r0,0),axis=polia2.pos-polia1.pos+vector(polia1.radius,0,0),radius=0.01,color=vector(1,1,1))
massa2=box(pos=polia2.pos+vector(-polia2.radius,-r0,0),height=0.40, length=0.08,width=0.08, color = vector(1,0.752,0.329))
massa3=box(pos=polia2.pos+vector(polia2.radius,-r0,0),height=0.40, length=0.08,width=0.08, color = vector(1,0.752,0.329))
corda3=cylinder(pos=polia2.pos+vector(polia2.radius,0,0),axis=massa2.pos-polia2.pos+vector(polia2.radius,0,0),radius=0.01,color=vector(1,1,1))
corda4=cylinder(pos=polia2.pos+vector(-polia2.radius,0,0),axis=massa3.pos-polia2.pos+vector(-polia2.radius,0,0),radius=0.01,color=vector(1,1,1))
n=8 #Número de raias na polia
for i in range(0,n):
    cylinder(pos=polia1.pos,axis=vector(polia1.radius*cos(i*2*pi/n),polia1.radius*sin(i*2*pi/n),0),radius=0.01,color=0.5*vector(1,1,1)) #Raias da polia 1

raia21=cylinder(pos=polia2.pos,axis=vector(polia2.radius*cos(1*2*pi/n),polia2.radius*sin(1*2*pi/n),0),radius=0.01,color=0.5*vector(1,1,1))
raia22=cylinder(pos=polia2.pos,axis=vector(polia2.radius*cos(2*2*pi/n),polia2.radius*sin(2*2*pi/n),0),radius=0.01,color=0.5*vector(1,1,1))
raia23=cylinder(pos=polia2.pos,axis=vector(polia2.radius*cos(3*2*pi/n),polia2.radius*sin(3*2*pi/n),0),radius=0.01,color=0.5*vector(1,1,1))
raia24=cylinder(pos=polia2.pos,axis=vector(polia2.radius*cos(4*2*pi/n),polia2.radius*sin(4*2*pi/n),0),radius=0.01,color=0.5*vector(1,1,1))
raia25=cylinder(pos=polia2.pos,axis=vector(polia2.radius*cos(5*2*pi/n),polia2.radius*sin(5*2*pi/n),0),radius=0.01,color=0.5*vector(1,1,1))
raia26=cylinder(pos=polia2.pos,axis=vector(polia2.radius*cos(6*2*pi/n),polia2.radius*sin(6*2*pi/n),0),radius=0.01,color=0.5*vector(1,1,1))
raia27=cylinder(pos=polia2.pos,axis=vector(polia2.radius*cos(7*2*pi/n),polia2.radius*sin(7*2*pi/n),0),radius=0.01,color=0.5*vector(1,1,1))
raia28=cylinder(pos=polia2.pos,axis=vector(polia2.radius*cos(8*2*pi/n),polia2.radius*sin(8*2*pi/n),0),radius=0.01,color=0.5*vector(1,1,1))
raias2=compound([raia21,raia22,raia23,raia24,raia25,raia26,raia27,raia28],pos=polia2.pos)


#Cálculo das Posições
for i in range(indices-1):
    rate(14)
    try:
        t=i*tmax;
        massa1.pos.y=a1*t*t/2
        polia2.pos.y=-a1*t*t/2
        massa2.pos.y=-r0+a2*t*t/2
        massa3.pos.y=-r0+a3*t*t/2
        corda1.axis=massa1.pos-polia1.pos-vector(polia1.radius,0,0)
        corda2.axis=polia2.pos-polia1.pos+vector(polia1.radius,0,0)
        corda3.axis=massa3.pos-polia2.pos+vector(-polia2.radius,0,0)
        corda3.pos=polia2.pos+vector(polia2.radius,0,0)
        corda4.axis=massa2.pos-polia2.pos+vector(polia2.radius,0,0)
        corda4.pos=polia2.pos+vector(-polia2.radius,0,0)
        raias2.pos=polia2.pos
    except FloatingPointError:
        break
