import numpy as np
import scipy.constants

omega = 1    # the omega of the harmonic trap
m = 1         # the mass of the particle



Nx = 600                        # Grid points
Ny = Nx
dt = 0.01                  # Evolution step
tmax = 20                # End of propagation
xmax = 30                     # x-window size
ymax = xmax                  # y-window size
dx = xmax / Nx
dy = ymax / Ny
distance_unit_x = (Nx / xmax) / 2
distance_unit_y = (Ny / ymax) / 2
images = 120                # number of .png images
absorb_coeff = 0        # 0 = periodic boundary
output_choice = 3        # If 1, it plots on the screen but does not save the images
                            # If 2, it saves the images but does not plot on the screen
                            # If 3, it saves the images and plots on the screen
fixmaximum= 0            # Fixes a maximum scale of |psi|**2 for the plots. If 0, it does not fix it.


def psi_0(x,y,n=2):
    alpha = m * omega
    coeff_gaus = 1/np.sqrt(np.math.factorial(n) * 2**n) * (alpha/scipy.constants.pi)
    return coeff_gaus * np.exp(-(alpha * (x**2)/2)) * hermitian_poly(n, np.sqrt(alpha)*x) + 0.j
    # return ((1/np.pi) ** (1/4)) * np.exp(-(x ** 2) / 2) * hermitian_poly(n,x) + 0.j

def hermitian_poly(n,z):
    herm = np.ones(len(z))    
    if n == 1:
        herm = 2*z
    elif n == 2:
        herm = 4*(z**2) - 2
    elif n == 3:
        herm = 8*(z**3) - 12*z
    elif n == 4:
        herm = 16*(z**4) -48*(z**2) + 12
    elif n == 5:
        herm = 32*(z**5) - 160*(z**3) + 120*z
    elif n == 6:
        herm = 64*(z**5) - 480*(z**4) + 720*(z**2) - 120
    elif n == 7:
        herm = 128*(z**7) - 1344*(z**5) + 3360*(z**3) -1680*z
    return herm
    
    
    
def V(x,y,t,psi):
    return 0.5 * m * (omega ** 2) * x ** 2 # Harmonic Trap centered at x=0
    # return (x ** 2) / 2
