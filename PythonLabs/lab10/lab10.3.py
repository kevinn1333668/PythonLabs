import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

fig, ax = plt.subplots()
t = np.linspace(0, 2*np.pi, 1000)

line, = ax.plot([], [], lw=2)
ax.set_xlim(-1, 1)
ax.set_ylim(-1, 1)
ax.grid(True)
ax.set_title('Анимация фигуры Лиссажу')

def animate(i):
    freq = i / 100  # параметр изменяется от 0 до 1
    x = np.sin(t)
    y = np.sin(freq * t)
    line.set_data(x, y)
    return line,

ani = animation.FuncAnimation(fig, animate, frames=100, interval=50)
plt.show()