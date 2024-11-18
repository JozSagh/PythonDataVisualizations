%matplotlib notebook
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.animation as animation
sns.set(rc={'axes.facecolor':'lavender', 'figure.facecolor':'white'})

x_data = np.linspace(1,20,20)
y_data = [12, 18, 20, 19, 80, 19 , 20, 22, 20, 23, 21 , 24, 27, 25, 42, 46, 47, 44, 45, 48]

figr,ax = plt.subplots(figsize=(4,3))
figr.suptitle("# of Customers by Date")
ax = plt.axes(xlim=(0, 25), ylim=(0, 60))
ax.axvline(x = 15, color = 'b')
line, = ax.plot([], [], marker='o', color='red')

                
def init():
    line.set_data([], [])
    return line

# animation function (will be called sequentially)
def animate(i):
    x = x_data[:int(i+1)]
    y = y_data[:int(i+1)]
    line.set_data(x, y)
    return line

anim = animation.FuncAnimation(figr, animate, init_func=init,
                               frames=20, interval=200, blit=True, repeat=True)
