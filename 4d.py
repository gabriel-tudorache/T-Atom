import matplotlib.pyplot as mplt
import numpy as np
from math import (sin, cos)
from random import random
import tkinter

from matplotlib.backends.backend_tkagg import ( 
    FigureCanvasTkAgg, NavigationToolbar2Tk)
QUARKS = 3
PI = 3.1415
ENERGY = 1.5032776*10**-10
ENERGY_NEUTRON = 1.50535*10**-10
ENERGY_ELECTRON = 8.18676092*10**-14
GRAVITY = 6.678*10**-11
PLANCK_SPACE = 	1.616255*10**-37
PLANCK_TEMPERATURE = 1.416 * 10**32
fig = mplt.figure()
ax = fig.add_subplot(projection='3d')
ax.set_box_aspect((1, 1, 1))

root = tkinter.Tk()
canvas = FigureCanvasTkAgg(fig, master=root)  # A tk.DrawingArea.
canvas.draw()
canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)

forwards = True
i = 0.1
atoms = []
for i in range(2):
	atoms.append(dict())
	atoms[i]["neutron"] = dict()
	atoms[i]["neutron"][0], atoms[i]["neutron"][1], atoms[i]["neutron"][2] = np.zeros( (35,35)),np.zeros( (35,35)),np.zeros( (35,35))
	atoms[i]["electron"] = dict()
	atoms[i]["electron"][0], atoms[i]["electron"][1], atoms[i]["electron"][2] = np.zeros( (35,35)),np.zeros( (35,35)),np.zeros( (35,35))
	atoms[i]["electron1"] = dict()
	atoms[i]["electron1"][0], atoms[i]["electron1"][1], atoms[i]["electron1"][2] = np.zeros( (35,35)),np.zeros( (35,35)),np.zeros( (35,35))
	atoms[i]["neutron1"] = dict()
	atoms[i]["neutron1"][0], atoms[i]["neutron1"][1], atoms[i]["neutron1"][2] = np.zeros( (35,35)),np.zeros( (35,35)),np.zeros( (35,35))
	atoms[i]["proton"] = dict()
	atoms[i]["proton"][0], atoms[i]["proton"][1], atoms[i]["proton"][2] = np.zeros( (35,35)),np.zeros( (35,35)),np.zeros( (35,35))
	atoms[i]["proton1"] = dict()
	atoms[i]["proton1"][0], atoms[i]["proton1"][1], atoms[i]["proton1"][2] = np.zeros( (35,35)),np.zeros( (35,35)),np.zeros( (35,35))
started = False
def draw_particles(position, ENERGY, TEMPERATURE, i, PHASE, location, particles, cmap):
		v = ENERGY*(6.626*10**-37)
		if(started):
			ENERGY = (np.max(position[0])-np.min(position[0]))+(np.max(position[1])-np.min(position[1]))+(np.max(position[2])-np.min(position[2]))/3

		i2 = (i*PHASE-(cos(ENERGY +(PHASE*PI))*5.539*10**-44))+TEMPERATURE+1
		frame = np.linspace(-i2, i2, 35) 
		
		THETA, PHI = np.meshgrid(frame, frame)
		R = PHI
		if(not started):
			#*5.539*10**-44 ):
			X = R * np.sin(PHI) * np.cos(THETA)  + location
			Y = R * np.sin(PHI) * np.sin(THETA)  + location
			Z = R * np.cos(PHI)  + location
		else:
			X = position[0]
			Y = position[1]
			Z = position[2]
	

			for particle in particles:
				#print(np.size(particle[0]))
				if (np.size(particle[0]) > 0):
					energyX = (X-np.average(X))+1
					energyY = (Y-np.average(Y))+1
					energyZ = (Z-np.average(Z))+1
					v2X = np.subtract(particle[0],np.average(particle[0]))+1
					v2Y = np.subtract(particle[1],np.average(particle[1]))+1
					v2Z = np.subtract(particle[2],np.average(particle[2]))+1
					#print(v2X)
					X =(X*PHASE -(np.sin(energyX)*np.cos(v2X ))*v2X*PLANCK_SPACE)
					X =(X*PHASE-(np.sin(energyX)*np.cos(v2X ))*v2X*PLANCK_SPACE)
					X =(X*PHASE -(np.sin(energyX)*np.cos(v2X))*v2X*PLANCK_SPACE)
					Y =(Y*PHASE -(np.sin(energyY)*np.sin(v2Y))*v2Y*PLANCK_SPACE)
					Y =(Y*PHASE -(np.sin(energyY)*np.sin(v2Y))*v2Y*PLANCK_SPACE)
					Y =(Y*PHASE -(np.sin(energyY)*np.sin(v2Y))*v2Y*PLANCK_SPACE)
					Z = (Z*PHASE -(np.sin(v2Z ))*v2Z*PLANCK_SPACE)
					Z = (Z*PHASE -(np.sin(v2X ))*v2Z*PLANCK_SPACE)
					Z = (Z*PHASE -(np.sin(v2Y ))*v2Z*PLANCK_SPACE)
					#print(X)	
					#print(Z*((i2*v2Z*(6.626*10**-37) * PI)))
		plot = ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=cmap, linewidth=0, antialiased=False, alpha=0.1)

		return X,Y,Z,i2
t = 1
TEMPERATURE = 3
TEMPERATURE = TEMPERATURE/PLANCK_TEMPERATURE
while 1==1:
		ax.clear()

		TEMPERATURE = sin(t)*3+300/PLANCK_TEMPERATURE
		for i in range(2):
			#print('proton')
			atoms[i]["proton"][0], atoms[i]["proton"][1], atoms[i]["proton"][2],t = draw_particles([atoms[i]["proton"][0], atoms[i]["proton"][1],atoms[i]["proton"][2]], ENERGY, TEMPERATURE,t,0.666,(i*10)+30*10**-11, 
																				[[atoms[i]["neutron"][0], atoms[i]["neutron"][1],atoms[i]["neutron"][2]],
																				[atoms[i]["neutron1"][0], atoms[i]["neutron1"][1],atoms[i]["neutron1"][2]],
																				[atoms[i]["proton1"][0], atoms[i]["proton1"][1],atoms[i]["proton1"][2]],
																				[atoms[i]["electron"][0], atoms[i]["electron"][1],atoms[i]["electron"][2]],
																				[atoms[i]["electron1"][0], atoms[i]["electron1"][1],atoms[i]["electron1"][2]]], 'Reds')
			#print('neutron')		
			atoms[i]["neutron"][0], atoms[i]["neutron"][1], atoms[i]["neutron"][2],t = draw_particles([atoms[i]["neutron"][0], atoms[i]["neutron"][1],atoms[i]["neutron"][2]], ENERGY_NEUTRON, TEMPERATURE,t,0.3333,(i*10)+25*10**-11, 
																				[[atoms[i]["proton"][0], atoms[i]["proton"][1],atoms[i]["proton"][2]],
																				[atoms[i]["neutron1"][0], atoms[i]["neutron1"][1],atoms[i]["neutron1"][2]],
																				[atoms[i]["proton1"][0], atoms[i]["proton1"][1],atoms[i]["proton1"][2]],
																				[atoms[i]["electron"][0], atoms[i]["electron"][1],atoms[i]["electron"][2]],
																				[atoms[i]["electron1"][0], atoms[i]["electron1"][1],atoms[i]["electron1"][2]]],'Blues')
			#print('proton1')		
			atoms[i]["proton1"][0], atoms[i]["proton1"][1], atoms[i]["proton1"][2],t = draw_particles([atoms[i]["proton1"][0], atoms[i]["proton1"][1],atoms[i]["proton1"][2]], ENERGY, TEMPERATURE,t,0.666,(i*10)+20*10**-11, 
																				[[atoms[i]["neutron"][0], atoms[i]["neutron"][1],atoms[i]["neutron"][2]],
																				[atoms[i]["neutron1"][0], atoms[i]["neutron1"][1],atoms[i]["neutron1"][2]],
																				[atoms[i]["proton"][0], atoms[i]["proton"][1],atoms[i]["proton"][2]],
																				[atoms[i]["electron"][0], atoms[i]["electron"][1],atoms[i]["electron"][2]],
																				[atoms[i]["electron1"][0], atoms[i]["electron1"][1],atoms[i]["electron1"][2]]], 'Reds')
			#print('neutron1')		
			atoms[i]["neutron1"][0], atoms[i]["neutron1"][1], atoms[i]["neutron1"][2],t = draw_particles([atoms[i]["neutron1"][0], atoms[i]["neutron1"][1], atoms[i]["neutron1"][2]], ENERGY_NEUTRON, TEMPERATURE,t,0.333,(i*10)+15*10**-11, 
																				[[atoms[i]["proton"][0], atoms[i]["proton"][1],atoms[i]["proton"][2]],
																				[atoms[i]["neutron"][0], atoms[i]["neutron"][1],atoms[i]["neutron"][2]],
																				[atoms[i]["proton1"][0], atoms[i]["proton1"][1],atoms[i]["proton1"][2]],
																				[atoms[i]["electron"][0], atoms[i]["electron"][1],atoms[i]["electron"][2]],
																				[atoms[i]["electron1"][0], atoms[i]["electron1"][1],atoms[i]["electron1"][2]]],'Blues')
			#print('electron')
			atoms[i]["electron1"][0], atoms[i]["electron1"][1], atoms[i]["electron1"][2],t = draw_particles([atoms[i]["electron1"][0], atoms[i]["electron1"][1], atoms[i]["electron1"][2]], ENERGY_ELECTRON, TEMPERATURE,t,-1,(i*10)+35*10**-11,
																				[[atoms[i]["proton"][0], atoms[i]["proton"][1],atoms[i]["proton"][2]],
																				[atoms[i]["neutron1"][0], atoms[i]["neutron1"][1],atoms[i]["neutron1"][2]],
																				[atoms[i]["proton1"][0], atoms[i]["proton1"][1],atoms[i]["proton1"][2]],
																				[atoms[i]["neutron"][0], atoms[i]["neutron"][1],atoms[i]["neutron"][2]],
																				[atoms[i]["electron"][0], atoms[i]["electron"][1],atoms[i]["electron"][2]]], 'Greens')
		
			atoms[i]["electron"][0], atoms[i]["electron"][1], atoms[i]["electron"][2],t = draw_particles([atoms[i]["electron"][0], atoms[i]["electron"][1], atoms[i]["electron"][2]], ENERGY_ELECTRON, TEMPERATURE,t,-1,(i*10)+5*10**-11,
																				[[atoms[i]["proton"][0], atoms[i]["proton"][1],atoms[i]["proton"][2]],
																				[atoms[i]["neutron1"][0], atoms[i]["neutron1"][1],atoms[i]["neutron1"][2]],
																				[atoms[i]["proton1"][0], atoms[i]["proton1"][1],atoms[i]["proton1"][2]],
																				[atoms[i]["neutron"][0], atoms[i]["neutron"][1],atoms[i]["neutron"][2]],
																				[atoms[i]["electron1"][0], atoms[i]["electron1"][1],atoms[i]["electron1"][2]]], 'Greens')
			#mplt.axis([-5*10**-46, 5*10**-46, -5*10**-46, 5*10**-46, -5*10**-46, 5*10**-46])
		ax.set_xlim(-10, 10)
		ax.set_ylim(-10, 10)
		ax.set_zlim(-10, 10)
		''''
		ax.set_xlim(np.min(atoms[1]["proton1"][0])*100, np.max(atoms[1]["proton1"][0])*100)
		ax.set_ylim(np.min(atoms[1]["proton1"][1])*100, np.max(atoms[1]["proton1"][1])*100)
		ax.set_zlim(np.min(atoms[1]["proton1"][2])*100, np.max(atoms[1]["proton1"][2])*100)
		#ax.set_box_aspect((np.max(Xelectron)/np.max(Yelectron)/np.max(Zelectron), np.max(Yelectron)/np.max(Yelectron)/np.max(Yelectron), np.max(Zelectron)/np.max(Zelectron)/np.max(Zelectron)))
		

		
		
		ax.set_xlim(np.min(Xproton), np.max(Xproton))
		ax.set_ylim(np.min(Yproton), np.max(Yproton))
		ax.set_zlim(np.min(Zproton), np.max(Zproton))
		ax.set_box_aspect((np.max(Xproton)/np.max(Yproton)/np.max(Zproton), np.max(Yproton)/np.max(Yproton)/np.max(Yproton), np.max(Zproton)/np.max(Zproton)/np.max(Zproton)))
		'''
		fig.canvas.draw()
		fig.canvas.flush_events()
		started = True
		t += 5.539*10**-44
		print("t="+str(t))
		#i+=1