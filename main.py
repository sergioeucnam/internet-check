# do a function that pings google.com every 1 second and draw a graph with the ping time
# if there is no internet connection, it should show a message on the plot
# if there is internet connection, it should show the ping time on the plot
# the x axis should be time and the y axis should be ping time

import matplotlib.pyplot as plt
import matplotlib.animation as animation
import time
import os
import numpy as np

fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)

def animate(i):
    ping = os.system("ping -n 1 google.com")
    if ping == 0:
      # there is internet connection draw the a plot with the ping time
      # is there is internet the fig should be "Internet Connection: OK" in green
      fig.suptitle("Internet Connection: OK", color="green")
      ax1.clear()
      ax1.plot(time.time(), ping)
    else:
      # there is no internet connection draw the plot with a message
      fig.suptitle("Internet Connection: NO", color="red")
      # fig.suptitle("Internet Connection: NO")
      ax1.clear()
      ax1.plot(time.time(), 0)

def update(i):
    ax1.clear()
    ax1.plot(time.time(), 0)

ani = animation.FuncAnimation(fig, animate, interval=1000)
plt.show()



# import matplotlib.pyplot as plt
# import matplotlib.animation as animation
# import time
# import os

# fig = plt.figure()
# ax1 = fig.add_subplot(1,1,1)

# def animate(i):
#     ping = os.system("ping -n 1 google.com")
#     if ping == 0:
#       # there is internet connection draw the a plot with the ping time
#       # is there is internet the fig should be "Internet Connection: OK" in green
#       fig.suptitle("Internet Connection: OK", color="green")
#       ax1.clear()
#       ax1.plot(time.time(), ping)
#     else:
#       # there is no internet connection draw the plot with a message
#       fig.suptitle("Internet Connection: NO", color="red")
#       # fig.suptitle("Internet Connection: NO")
#       ax1.clear()
#       ax1.plot(time.time(), 0)

# def update(i):
#     ax1.clear()
#     ax1.plot(time.time(), 0)

# ani = animation.FuncAnimation(fig, animate, interval=1000)
# plt.show()


      
