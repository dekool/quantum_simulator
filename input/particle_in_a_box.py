import numpy as np

Nx = 600						# Grid points
Ny = 300
dt = 0.001		      	# Evolution step
tmax = 7		        # End of propagation
xmax = 30 					# x-window size
ymax = 20		      	# y-window size
dx = xmax / Nx
dy = ymax / Ny
distance_unit_x = (Nx / xmax) / 2
distance_unit_y = (Ny / ymax) / 2
images = 140				# number of .png images
absorb_coeff = 0		# 0 = periodic boundary
output_choice = 3        # If 1, it plots on the screen but does not save the images
							# If 2, it saves the images but does not plot on the screen
							# If 3, it saves the images and plots on the screen
fixmaximum= 0            # Fixes a maximum scale of |psi|**2 for the plots. If 0, it does not fix it.


def psi_0(x,y):
	phi = np.zeros([Nx, Ny], dtype=np.complex)
	for x in range(Nx):
		x_axis = (x - (Nx / 2)) * dx
		if x < -(0.75*np.pi) * distance_unit_x + int(Nx/2):
			phi[x][int(Ny/2)+1] = (1/2) * np.exp((1/2) * x_axis)
		elif x > (0.75*np.pi) * distance_unit_x + int(Nx/2):
			phi[x][int(Ny/2)+1] = (1/2) * np.exp(-(1/2) * x_axis)
		else:
			phi[x][int(Ny/2)+1] = np.sin(x_axis + (np.pi/2))
	return phi

def V(x,y,t,psi):
	trap = np.zeros([Nx, Ny])
	for x in range(Nx):
		if -np.floor((0.75*np.pi + t) * distance_unit_x) + int(Nx/2) < x < -np.ceil((0.75*np.pi + t) * distance_unit_x) + int(Nx/2) + 2.5:
			trap[x][int(Ny/2)+1] = 10
		elif np.floor((0.75*np.pi) * distance_unit_x + t) + int(Nx/2) < x < np.ceil((0.75*np.pi) * distance_unit_x + t) + int(Nx/2) + 1:
			trap[x][int(Ny/2)+1] = 10
		else:
			trap[x][int(Ny/2)+1] = 0
	return trap
