import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

x = np.linspace(0, 4*np.pi, 500)

fig, axs = plt.subplots(3, 1, figsize=(9, 8))
plt.subplots_adjust(left=0.1, bottom=0.35)

# Исходные настройки волн
ampl1, freq1 = 1, 1
ampl2, freq2 = 1, 2

wave1, = axs[0].plot(x, ampl1*np.sin(freq1*x), color='blue', label='Wave 1')
wave2, = axs[1].plot(x, ampl2*np.sin(freq2*x), color='green', label='Wave 2')
result_wave, = axs[2].plot(x, ampl1*np.sin(freq1*x) + ampl2*np.sin(freq2*x), color='red', label='Result')

# Слайдеры
axfreq1 = plt.axes([0.25, 0.25, 0.65, 0.03])
sfreq1 = Slider(axfreq1, 'Freq 1', 0.1, 10.0, valinit=freq1)

axampl1 = plt.axes([0.25, 0.2, 0.65, 0.03])
sampl1 = Slider(axampl1, 'Ampl 1', 0.1, 5.0, valinit=ampl1)

axfreq2 = plt.axes([0.25, 0.1, 0.65, 0.03])
sfreq2 = Slider(axfreq2, 'Freq 2', 0.1, 10.0, valinit=freq2)

axampl2 = plt.axes([0.25, 0.05, 0.65, 0.03])
sampl2 = Slider(axampl2, 'Ampl 2', 0.1, 5.0, valinit=ampl2)

def update(val):
    f1, a1, f2, a2 = sfreq1.val, sampl1.val, sfreq2.val, sampl2.val
    wave1.set_ydata(a1*np.sin(f1*x))
    wave2.set_ydata(a2*np.sin(f2*x))
    result_wave.set_ydata(a1*np.sin(f1*x) + a2*np.sin(f2*x))
    fig.canvas.draw_idle()

sfreq1.on_changed(update)
sampl1.on_changed(update)
sfreq2.on_changed(update)
sampl2.on_changed(update)

axs[0].set_title('Wave 1')
axs[1].set_title('Wave 2')
axs[2].set_title('Wave 1 + Wave 2')

plt.tight_layout()
plt.show()