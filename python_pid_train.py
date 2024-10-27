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
def set_x_ref(incl_angle):
    rand_h=random.uniform(0,120)
    rand_v=random.uniform(20+120*np.tan(incl_angle)+6.5,40+120*np.tan(incl_angle)+6.5)
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
while(trials>0):  # Determines how many times cube falls down.
    pos_x_cube_ref=set_x_ref(incl_angle)[0] # Cube's initial x position
    pos_y_cube_ref=set_x_ref(incl_angle)[1] # Cube's initial y position
    times=trials_magn-trials
    pos_x_cube[times]=pos_x_cube_ref
    pos_y_cube[times]=pos_x_cube_ref-g/2*t**2
    win=False
    delta=1

    # Implement PID for the train position
    for i in range(1,len(t)):
        # Insert the initial values into the beginning of the predefined arrays.
        if i==1:
            displ_rail[times][0]=init_displ_rail
            pos_x_train[times][0]=init_pos_x
            pos_y_train[times][0]=init_pos_y
            v_rail[times][0]=init_vel_rail
            a_rail[times][0]=init_a_rail

        # Compute the horizontal error
        e[times][i-1]=pos_x_cube_ref-pos_x_train[times][i-1]

        # Check if the ratio of the horizontal and vertical distance can be added
        if pos_y_cube[times][i-1]<10 or pos_y_cube[times][i-1]>-10:
            e[times][i-1]=e[times][i-1]
        else:
            e[times][i-1]=e[times][i-1]*(abs(e[times][i-1])/abs(pos_y_cube[times][i-1]))

        if i>1:
            e_dot[times][i-1]=(e[times][i-1]-e[times][i-2])/dt
            e_int[times][i-1]=e_int[times][i-2]+(e[times][i-2]+e[times][i-1])/2*dt
        if i==len(t)-1:
            e[times][-1]=e[times][-2]
            e_dot[times][-1]=e_dot[times][-2]
            e_int[times][-1]=e_int[times][-2]



################################################################################
################################################################################
################################################################################


