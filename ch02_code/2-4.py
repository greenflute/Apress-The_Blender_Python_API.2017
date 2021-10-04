import bpy

# Returns bpy.data.objects datablock
bpy.context.object

# Longer synonym for the above line
bpy.context.active_object

# Accessing the 'name' and 'location' values of the datablock
print(bpy.context.object.name)
print(bpy.context.object.location)
