import numpy
import math
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker



# Phase response of transfer function IIR filter
def transfer_function(m,a,b,omega):
    cos_val = numpy.cos(numpy.arange(m+1) * omega)
    sin_val = numpy.sin(numpy.arange(m+1) * omega)
    re_num = numpy.sum(a * cos_val)
    im_num = -numpy.sum(a * sin_val)
    re_den = -numpy.sum(b * cos_val)
    im_den = numpy.sum(b * sin_val)
    Phase = math.atan2(im_num, re_num) - math.atan2(im_den, re_den)
    
    return Phase


m = int(input("Enter digital filter'order: "))
a = numpy.zeros(m + 1)
b = numpy.zeros(m + 1)
for i in range(m + 1):
    a[i] = float(input(f"Enter {i}th coefficient a: "))
b[0] = -1
for i in range(1, m + 1):
    b[i] = float(input(f"Enter {i}th coefficient b: "))


l = int(input("Enter number of discrete frequencies: "))
omega = numpy.arange(l) * ((2 * math.pi) * (1 / (l - 1)))
Phase = numpy.zeros(l)
for i in range(l):
    Phase[i] = transfer_function(m,a,b,omega[i])
lim = math.ceil(max(Phase))

# plotting
fig, ax = plt.subplots()
fig.suptitle (r"ФЧХ $\phi$($\omega$)")

unit = 1/9.5
x_tick = numpy.arange(-unit, 2 + unit, unit)
x_label = [r"$" + format(r, ".2g")+ r"\pi$" for r in x_tick]
ax.set_xlim(0, 2 * math.pi)
ax.set_ylim(-lim, lim)
ax.spines['top'].set_visible(False)
ax.spines['bottom'].set_position('center')
ax.spines['bottom'].set_linewidth(2.0)
ax.spines['left'].set_linewidth(2.0)
ax.xaxis.set_major_locator(ticker.MultipleLocator(math.pi / 9.5))
ax.yaxis.set_major_locator(ticker.MultipleLocator(1.0))
ax.tick_params(axis = 'x', labelrotation = 45, width = 2)
ax.tick_params(axis = 'y', width = 2)
ax.set_xticklabels(x_label)
ax.grid(axis = 'y', linewidth = 1.0)
ax.plot(omega, Phase, linewidth = 2.5)

plt.show()


