import bpy

def mySelector(objName, additive=False):

    # By default, clear other selections
    if not additive:
        bpy.ops.object.select_all(action='DESELECT')

    # Set the 'select' property of the datablock to True
    # bpy.data.objects[objName].select = True
    '''
    API changed: AttributeError: 'Object' object has no attribute 'select'

    ['__doc__', '__module__', '__slots__', 'active_material', 'active_material_index', 'active_shape_key', 'active_shape_key_index', 'animation_data', 'animation_data_clear', 'animation_data_create', 'animation_visualization', 'asset_data', 'bl_rna', 'bound_box', 'cache_release', 'calc_matrix_camera', 'camera_fit_coords', 'children', 'closest_point_on_mesh', 'collision', 'color', 'constraints', 'convert_space', 'copy', 'cycles', 'cycles_visibility', 'data', 'delta_location', 'delta_rotation_euler', 'delta_rotation_quaternion', 'delta_scale', 'dimensions', 'display', 'display_bounds_type', 'display_type', 'empty_display_size', 'empty_display_type', 'empty_image_depth', 'empty_image_offset', 'empty_image_side', 'evaluated_get', 'face_maps', 'field', 'find_armature', 'generate_gpencil_strokes', 'grease_pencil_modifiers', 'hide_get', 'hide_render', 'hide_select', 'hide_set', 'hide_viewport', 'holdout_get', 'image_user', 'indirect_only_get', 'instance_collection', 'instance_faces_scale', 'instance_type', 'is_deform_modified', 'is_embedded_data', 'is_evaluated', 'is_from_instancer', 'is_from_set', 'is_instancer', 'is_library_indirect', 'is_modified', 'library', 'lineart', 'local_view_get', 'local_view_set', 'location', 'lock_location', 'lock_rotation', 'lock_rotation_w', 'lock_rotations_4d', 'lock_scale', 'make_local', 'material_slots', 'matrix_basis', 'matrix_local', 'matrix_parent_inverse', 'matrix_world', 'mode', 'modifiers', 'motion_path', 'name', 'name_full', 'original', 'override_create', 'override_library', 'override_template_create', 'parent', 'parent_bone', 'parent_type', 'parent_vertices', 'particle_systems', 'pass_index', 'pose', 'pose_library', 'preview', 'proxy', 'proxy_collection', 'ray_cast', 'rigid_body', 'rigid_body_constraint', 'rna_type', 'rotation_axis_angle', 'rotation_euler', 'rotation_mode', 'rotation_quaternion', 'scale', 'select_get', 'select_set', 'shader_effects', 'shape_key_add', 'shape_key_clear', 'shape_key_remove', 'show_all_edges', 'show_axis', 'show_bounds', 'show_empty_image_only_axis_aligned', 'show_empty_image_orthographic', 'show_empty_image_perspective', 'show_in_front', 'show_instancer_for_render', 'show_instancer_for_viewport', 'show_name', 'show_only_shape_key', 'show_texture_space', 'show_transparent', 'show_wire', 'soft_body', 'tag', 'to_curve', 'to_curve_clear', 'to_mesh', 'to_mesh_clear', 'track_axis', 'type', 'up_axis', 'update_from_editmode', 'update_tag', 'use_camera_lock_parent', 'use_dynamic_topology_sculpting', 'use_empty_image_alpha', 'use_fake_user', 'use_grease_pencil_lights', 'use_instance_faces_scale', 'use_instance_vertices_rotation', 'use_mesh_mirror_x', 'use_mesh_mirror_y', 'use_mesh_mirror_z', 'use_shape_key_edit_mode', 'user_clear', 'user_of_id', 'user_remap', 'users', 'users_collection', 'users_scene', 'vertex_groups', 'visible_get', 'visible_in_viewport_get']
    '''
    bpy.data.objects[objName].select_set(True)


# Select only 'Cube'
mySelector('Cube')

# Select 'Sphere', keeping other selections
mySelector('Sphere', additive=True)

# Translate selected objects 1 unit along the x-axis
bpy.ops.transform.translate(value=(1, 0, 0))   