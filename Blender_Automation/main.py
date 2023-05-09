import numpy as np
import bpy
import os
import sys

dir = os.path.dirname(bpy.data.filepath)
if not dir in sys.path:
    sys.path.append(dir )

from gen_single_drop import genSingleDrop
from gen_drop_blender import Generate_Drop
from gen_drop_blender import Remove_Drop
from render import change_sun

# Define the parameters physical parameters
sigma=100
volume0=15
rneedle=0.5

# Compute the r -and z-coordinates
# rr,zz = genSingleDrop(sigma,volume0,rneedle,output=0,savepath='.')
# # print(rr,zz)
# # Generate the drop in Blender
# Generate_Drop(rr,zz)

# change_sun(sigma, 'Users/20193709/OneDrive - TU Eindhoven/Master/Master Courses/Quartile 4/4AI000/Blender_Automation/Test_Images')




# Idea is to also have array of desired values to model
sigma2= np.array([75])
for i in range(0,len(sigma2)):
    rr,zz = genSingleDrop(sigma2[i],volume0,rneedle,output=0,savepath='.')
    Generate_Drop(rr,zz)
    # Take images while changing lighting conditions
    change_sun(sigma2[i], volume0, rneedle, 'Users/20193709/OneDrive - TU Eindhoven/Master/Master Courses/Quartile 4/4AI000/Blender_Automation/Test_Images')
    # After render delete old droplet and create a new one
    # Remove_Drop()


