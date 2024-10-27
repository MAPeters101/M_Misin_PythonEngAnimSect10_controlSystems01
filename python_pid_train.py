import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import matplotlib.animation as animation
import numpy as np
import random

################################################################################

# ONLY CHANGE THESE INPUTS FOR THE CODE TO WORK PROPERLY

# Initial input values
trials=2
incl_angle=np.pi/6*1 # Keep the angle between 0 and +pi/6 radians
g=10
mass_cart=100 # [kg]

# Tune the constants
K_p=300
K_d=300
K_i=10
################################################################################

trials_globals=trials

# Generate random x-position for a falling cube
def set_s_ref(incl_angle):
    rand_h=random.uniform(0,120)
    rand_v=random.uniform(20+120*mp.tan(incl_angle)+6.5,40+120*np.tan(incl_angle)+6.5)
    return rand_h,rand_v

dt=0.02
t0=0
t_end=5
t=np.arange(t0,t_end+dt,dt)

F_g=mass_cart*g
displ_rail=np.zeros((trials,len(t)))
v_rail=np.zeros((trials,len(t)))
a_rail=np.zeros((trials,len(t)))
pos_x_train=np.zeros((trials,len(t)))
pos_y_train=np.zeros((trials,len(t)))
e=np.zeros((trials,len(t)))
e_dot=np.zeros((trials,len(t)))
e_int=np.zeros((trials,len(t)))

pos_x_cube=np.zeros((trials,len(t)))
pos_y_cube=np.zeros((trials,len(t)))

F_ga_t=F_g*np.sin(incl_angle) # Tangential component of the gravity force
init_pos_x=120
init_pos_y=120*np.tan(incl_angle)+6.5
init_displ_rail=(init_pos_x**2+init_pos_y**2)**(0.5)
init_vel_rail=0
init_a_rail=0


init_pos_x_global=init_pos_x # Used for determining the dimensions of the animation window.

trials_magn=trials
history=np.ones(trials)







################################################################################
################################################################################
################################################################################


