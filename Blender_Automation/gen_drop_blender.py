import numpy as np
import bpy

def Generate_Drop(rr,zz):
    cu = bpy.data.curves.new("poly", 'CURVE')
    cu.dimensions  = '3D'
    # Iteratove over arrays to set pts in right format
    points = np.array([(rr[z],0,zz[z]) for z in range(len(zz))])
    s = cu.splines.new('BEZIER')
    s.bezier_points.add(len(points) - 1)
    # Set points and flatten array
    s.bezier_points.foreach_set("co", points.flatten())
    # doesn't seem to work for handles so set them in loop
    for bp in s.bezier_points:
        bp.handle_left_type = bp.handle_right_type = 'AUTO'

    # lazy way to add curve object
    bpy.ops.curve.primitive_bezier_curve_add()
    ob = bpy.context.object
    ob.data = cu

    # Spins 360 on z-axis
    revolve = ob.modifiers.new("Screw", 'SCREW')
    revolve.steps = 128
    revolve.render_steps = 128

# Assigning Materials
    mat = bpy.data.materials.get("Droplet")
    if mat is None:
        mat = bpy.data.materials.new(name="Droplet")
        mat.use_nodes = True
        tree = mat.node_tree
        nodes = tree.nodes
        # bsdf = nodes["Principled BSDF"] 
        # # bsdf.inputs["Base Color"].default_value = (167/255, 219/255, 243/255, 0.8)        
        # bsdf.inputs["Base Color"].default_value = (0.08, 0.4, 0.8, 0.5)
        # mat.diffuse_color = (0.08, 0.4, 0.8, 0.5)
        # bsdf = nodes["Glass BSDF"] 
        # bsdf.inputs["Roughness"].default_value = (0.001)
        # bsdf.inputs["IOR"].default_value = (1.50)

    # Assign it to object
    if ob.data.materials:
        # assign to 1st material slot
        ob.data.materials[0] = mat
    else:
        # no slots
        ob.data.materials.append(mat)

    

def Remove_Drop():
    if bpy.context.object.mode == 'EDIT':
        bpy.ops.object.mode_set(mode='OBJECT')

    bpy.ops.object.select_all(action='DESELECT')
    bpy.data.objects['BezierCurve'].select_set(True)
    bpy.ops.object.delete()