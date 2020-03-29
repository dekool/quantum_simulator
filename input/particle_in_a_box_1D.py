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
images = 140				# number of .png images
absorb_coeff = 0		# 0 = periodic boundary
output_choice = 3        # If 1, it plots on the screen but does not save the images
							# If 2, it saves the images but does not plot on the screen
							# If 3, it saves the images and plots on the screen
fixmaximum= 0            # Fixes a maximum scale of |psi|**2 for the plots. If 0, it does not fix it.


def psi_0(x,y):
	right_wall = 1.5
	left_wall = -1.5
	right = np.exp(-x) * np.heaviside([i-right_wall for i in x], 1) + 0.j
	left = np.exp(x) * (1 - np.heaviside([i-left_wall for i in x], 1)) + 0.j
	center = np.sin(x + (np.pi/2)) \
			 * (np.heaviside([i-left_wall for i in x], 1) - np.heaviside([i-right_wall for i in x], 1)) + 0.j

	return left + center + right


def V(x,y,t,psi):
	right_wall = 1.5 + t
	left_wall = -(1.5) + t
	right = 10 * (np.heaviside([i-right_wall for i in x], 1) - np.heaviside([i-(right_wall + 0.2) for i in x], 1))
	left = 10 * (np.heaviside([i-(left_wall - 0.2) for i in x], 1) - np.heaviside([i-left_wall for i in x], 1))

	return right + left
