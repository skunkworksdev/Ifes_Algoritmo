from vpython import *

scene = canvas(title='<h1>Oscilador harmónico simples</h1>', autoscale=0,
               width=500, height=500, range=7, forward=vec(0,0,-1))
chao = box(pos=vec(0,-6.1,0),size=vec(20,0.1,10),texture=textures.wood)
parede = box(pos=vec(0,3.85,-5.05),size=vec(20,20,0.1), color=vec(0.7,0.7,0.7))
sitio = text(pos=vec(0,3.85,-5), text='def.fe.up.pt', color=color.blue,
              align='center', depth=0)

 # Mola e cilindro
bar0 = curve(radius=0.03)
for ang in arange(pi,-pi/2.,-0.1):
    bar0.append(vec(0, 5.2+0.23*sin(ang), 0.23*cos(ang)))
bar0.append(pos=vec(0,4.5,0))
bar0.append(pos=vec(0,4.5,0.3))
mola1 = helix(pos=vec(0,4.5,0), radius=0.3, thickness=0.05, coils=30,
              axis = vec(0,-5.8,0))

bar1 = curve(radius=0.03, pos=[vec(0,-1.6,0),vec(0,-1.3,0),vec(0,-1.3,0.3)])
c1 = cylinder(pos=vec(0,-2,0),radius=0.5,axis=vec(0,0.4,0),
              color=vec(0.3,0.3,0.3))

 # Barras do suporte
s1 = cylinder(pos=vec(3,5.2,0),radius=0.2, axis=vec(-4,0,0))
s2 = cylinder(pos=vec(2.5,5.2,0),radius=0.6, axis=vec(-1,0,0),color=vec(0.5,0.5,0.6))
s3 = cylinder(pos=vec(2,-5,0.4),radius=0.2, axis=vec(0,11,0))
s4 = cylinder(pos=vec(2,-6.05,0.4),radius=0.8, axis=vec(0,1,0),color=vec(0.9,0.9,0.6))

 # Função que alonga/comprime a mola y1 unidades
def alongar_mola(y1):
    c1.pos.y = y1 - 2
    bar1.origin = vec(0,y1,0)
    mola1.axis.y = y1 - 5.8

def uf(rf):          # velocidade no espaço de fase
    a = (-k1*rf.y-b1*rf.z)/m1
    return vec(0,rf.z, a)

rf = vec(0, 0.9, 0)
m1 = 0.3; k1 = 16; b1 = 0.02
dt = 0.01
alongar_mola(rf.y)

while True:
    rate(100)
    uf1 = uf(rf)
    uf2 = uf(rf + dt*uf1 / 2.)
    uf3 = uf(rf + dt*uf2 / 2.)
    uf4 = uf(rf + dt*uf3)
    ufm = (uf1 + 2*uf2 + 2*uf3 + uf4)/6.
    rf += dt*ufm
    alongar_mola(rf.y)