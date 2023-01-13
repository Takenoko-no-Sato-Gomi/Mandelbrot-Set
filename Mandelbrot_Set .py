import matplotlib.pyplot as plt
import matplotlib.cm as cm
import numpy as npy

#中心
Real_Mid = 0
Imaginaly_Mid = 0

#範囲
Length = 3

Right = Real_Mid + (1/2)*Length
Left = Real_Mid - (1/2)*Length
Top = Imaginaly_Mid + (1/2)*Length
Botom = Imaginaly_Mid - (1/2)*Length

wideth = Right - Left
hight = Top - Botom

#サイズ
Bit_num = 150
Bit_len = Length/Bit_num

#繰り返し数
repeat = 300

#弾く絶対値上限
lim = 3

#小数点切り捨て
Dig = 2

#描画する関数
def fan(z):
    return z**2 + c



fig, ax = plt.subplots()

ax.set_xlim(Left, Right)
ax.set_ylim(Botom, Top)

def Abso(z):
    return z*npy.conjugate(z)

def man(c):
    z = [0]
    for i in range(1,repeat):
        z.append((round(npy.real(fan(z[i-1])),Dig) + round(npy.imag(fan(z[i-1])),Dig)*1.j))
        if Abso(z[i-1])>lim**2:
            break
    return z[len(z)-1]

for x in range(Bit_num):
    for y in range(Bit_num):
        c = (Left + Bit_len*x) + (Botom + Bit_len*y)*1.j
        z = [0]
        for i in range(1,repeat):
            z.append((round(npy.real(fan(z[i-1])),Dig) + round(npy.imag(fan(z[i-1])),Dig)*1.j))
            if Abso(z[i-1])>lim**2:
                break
        z_lim = len(z)
        z_max = Abso(z[i-1])
        plt.axvspan(npy.real(c), npy.real(c) + Bit_len, y/Bit_num, (y+1)/Bit_num, color=cm.jet(z_lim/Bit_num))

plt.show()