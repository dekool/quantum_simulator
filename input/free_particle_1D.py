import numpy as np

Nx = 600						# Grid points
Ny = Nx
dt = 0.001		      	# Evolution step
tmax = 6		        # End of propagation
xmax = 30 					# x-window size
ymax = xmax		      	# y-window size
dx = xmax / Nx
dy = ymax / Ny
distance_unit_x = (Nx / xmax) / 2
distance_unit_y = (Ny / ymax) / 2
images = 60				# number of .png images
absorb_coeff = 0		# 0 = periodic boundary
output_choice = 3        # If 1, it plots on the screen but does not save the images
							# If 2, it saves the images but does not plot on the screen
							# If 3, it saves the images and plots on the screen
fixmaximum= 0            # Fixes a maximum scale of |psi|**2 for the plots. If 0, it does not fix it.


def psi_0(x,y):
	sigma = 2
	center = 0
	return 0.j+(1/(sigma*np.sqrt(2*np.pi)))*np.exp(-0.5*((x-center/sigma)**2))


def V(x,y,t,psi):
	return np.zeros(len(x))
