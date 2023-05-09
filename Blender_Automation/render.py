import bpy
import numpy as np
import math

# # Taking pictures of the object in different positions
# def rotate_and_render(output_dir, output_file_pattern_string = 'render%d.jpg', rotation_steps = 5, rotation_angle = 0, subject = bpy.context.object):
#   import os
#   # original_rotation = subject.rotation_euler
#   for step in range(0, rotation_steps):
#     # subject.rotation_euler[2] = math.radians(step * (rotation_angle / rotation_steps))
#     bpy.context.scene.render.filepath = os.path.join(output_dir, (output_file_pattern_string % step))
#     bpy.ops.render.render(write_still = True)
#   # subject.rotation_euler = original_rotation



# Call to taking the Images and save tem in the desired folder
# rotate_and_render('Users/20193709/OneDrive - TU Eindhoven/Master/Master Courses/Quartile 4/4AI000/Blender_Automation/Test_Images', 'render%d.jpg')
def change_sun(sigma, volume0, rneedle, output_dir, output_file_pattern_string = 'render.png', sun_strength = 7, sun_steps = 4, sun_rotate = 90, sun_angle=180, subject = bpy.context.object):
  import os
  sun = bpy.data.lights["Sun"]
  # Check if sun is rotating around zero-point and not around itself
  
  bpy.context.scene.tool_settings.transform_pivot_point = 'CURSOR'
  bpy.ops.object.select_all(action='DESELECT')
  bpy.data.objects['Sun'].select_set(True)  
  # bpy.ops.object.origin_set(type='ORIGIN_CURSOR', center='MEDIAN')
  for step in range(1,sun_strength):
    for pos in range(sun_steps):
      # for ang in range(sun_steps-2):
        # bpy.ops.object.origin_set(type='ORIGIN_CURSOR')
        bpy.ops.transform.rotate(value=(np.pi*pos*(sun_rotate/sun_steps)/180), orient_axis = 'Z')   
        sun.energy = step
        # sun.angle = (math.pi*ang * (sun_angle / sun_steps))/180
        # bpy.context.scene.render.filepath = os.path.join(output_dir, ('drop' + '_s{}' + '_v{}' + '_r{}' + '_str{}' + '_pos{}' + '_ang{}' + '.png').format(sigma, volume0, rneedle, step, pos, ang))
        bpy.context.scene.render.filepath = os.path.join(output_dir, ('drop' + '_s{}' + '_v{}' + '_r{}' + '_str{}' + '_pos{}' + '.png').format(sigma, volume0, rneedle, step, pos))
        bpy.ops.render.render(write_still = True)
 