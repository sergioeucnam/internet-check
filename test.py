import matplotlib.pyplot as plt
import matplotlib.animation as animation
import time
import os
import numpy as np
import speedtest

fig, ax = plt.subplots()
fig.subplots_adjust(left=0.05, bottom=0.05, right=0.95, top=0.95)
ax.set_title('Internet Connection: OK', color="green")
ax.set_xlabel('Time')
ax.set_ylabel('Ping Time')
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)
ax.grid()

xdata, ydata = [], []
ln, = plt.plot([], [], 'ro')

def init():
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    return ln,

# ping google.com with speedtest and get the ping time in ms and draw a plot with the ping time

def update(frame):
    ping = speedtest.Speedtest().results.ping
    ax.set_ylabel('Ping Time: ' + str(ping) + ' ms')
    xdata.append(frame)
    ydata.append(ping)
    ln.set_data(xdata, ydata)
    return ln,

        
 

ani = animation.FuncAnimation(fig, update, frames=np.linspace(0, 10, 100),
                                init_func=init, blit=True)

plt.show()