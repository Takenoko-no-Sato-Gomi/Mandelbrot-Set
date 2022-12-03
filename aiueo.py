#マンデルブロ集合
import matplotlib.pyplot as plt
import numpy as npy
from matplotlib.widgets import Slider

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
        if Abso(man(c))<lim**2:
            plt.axvspan(npy.real(c), npy.real(c) + Bit_len, y/Bit_num, (y+1)/Bit_num)

slider_pos_Length = plt.axes([0.1, 0.01, 0.8, 0.03])
threshold_slider = Slider(slider_pos_Length, 'Length', 0, 5, valinit=0)
plt.show()