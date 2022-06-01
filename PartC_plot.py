from nbody import System
import numpy as np
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d.axes3d as p3


"""
Plots the positions of particles at any frame of the simulation
"""

s = System.read("./ori/wisps/wisps_0.999.dat") #Reads the data file of the final frame of the simulation for a box with 64**3 particles.
x = s.all_x()
y = s.all_y()
z = s.all_z()

fig = plt.figure()
ax = p3.Axes3D(fig)
#ax.set_aspect('equal')
#ax.set_xlim(-1000, 1000)
#ax.set_ylim(-1000, 1000)
ax.set_xlim3d([0,50])
ax.set_ylim3d([0,50])
ax.set_zlim3d([0,50])
fig.set_facecolor('black')
ax.set_facecolor('black') 
#ax.grid(False)
ax.w_xaxis.pane.fill = False
ax.w_yaxis.pane.fill = False
ax.w_zaxis.pane.fill = False

line, = ax.plot(x, y, color="white", marker="o", markersize=5, linestyle='none', mfc="y", mec="r", mew=0.5)
line.set_3d_properties(z)
plt.show()