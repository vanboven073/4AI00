import bpy
import numpy as np
import math

def change_sun(sigma, volume0, rneedle, output_dir, output_file_pattern_string = 'render.png', sun_strength = 6, cam_steps=5, sun_steps = 4, sun_rotate = 360, sun_angle=180, subject = bpy.context.object):
  import os
  sun = bpy.data.lights["Sun"]
  bpy.ops.object.select_all(action='DESELECT')
  cursor_loc = bpy.context.scene.cursor.location
  for step in range(4,sun_strength):
    for pos in range(sun_steps):
        bpy.data.objects['Sun'].select_set(True)  
        bpy.data.objects['Camera'].select_set(False)  
        bpy.ops.transform.rotate(value=(np.pi*(sun_rotate/sun_steps)/180), orient_axis = 'Z', center_override=cursor_loc) 
          # sun.angle = (math.pi* (sun_angle / sun_steps))/180
        sun.energy = step        
        for cam in range(cam_steps):   
          bpy.data.objects['Sun'].select_set(False)  
          bpy.data.objects['Camera'].select_set(True)  
          bpy.ops.transform.rotate(value=(np.pi*(sun_rotate/cam_steps)/180), orient_axis = 'X', center_override=cursor_loc) 
          bpy.context.scene.render.filepath = os.path.join(output_dir, ('drop' + '_s{}' + '_v{}' + '_r{}' + '_str{}' + '_pos{}' + '_cam{}' + '.png').format(sigma, volume0, rneedle, step, pos, cam))
          bpy.ops.render.render(write_still = True)
 