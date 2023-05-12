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
volume0=5
rneedle=0.5

sigma = np.array([40])
# volume = np.array([5,10])
for i in range(0,len(sigma)):
    # for k in range(0,len(volume))
        rr,zz = genSingleDrop(sigma[i],volume0,rneedle,output=0,savepath='.')
        Generate_Drop(rr,zz)
        # Take images while changing lighting conditions
        change_sun(sigma[i], volume0, rneedle, 'Users/20193709/OneDrive - TU Eindhoven/Master/Master Courses/Quartile 4/4AI000/Blender_Automation/Realistic_DropX')
        # After render delete old droplet and create a new one
        Remove_Drop()



