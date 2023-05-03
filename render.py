import bpy
import numpy as np
import math

# Taking pictures of the object in different positions
def rotate_and_render(output_dir, output_file_pattern_string = 'render%d.jpg', rotation_steps = 32, rotation_angle = 360.0, subject = bpy.context.object):
  import os
  original_rotation = subject.rotation_euler
  for step in range(0, rotation_steps):
    subject.rotation_euler[2] = math.radians(step * (rotation_angle / rotation_steps))
    bpy.context.scene.render.filepath = os.path.join(output_dir, (output_file_pattern_string % step))
    bpy.ops.render.render(write_still = True)
  subject.rotation_euler = original_rotation


# Call to taking the Images and save tem in the desired folder
rotate_and_render('Users/20193709/OneDrive - TU Eindhoven/Master/Master Courses/Quartile 4/4AI000/Test_Images', 'render%d.jpg')
