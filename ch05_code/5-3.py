bl_info = {
    "name": "Simple Add-on",
    "author": "Chris Conlan",
    "location": "View3D > Tools > Simple Addon",
    "version": (1, 0, 0),
    "blender": (2, 7, 8),
    "description": "Starting point for new add-ons.",
    "wiki_url": "http://example.com",
    "category": "Development"
}


# Custom modules are imported here
# See end of chapter example for suggested protocol

import bpy

# Simple Operator with Extra Properties
class SimpleOperator(bpy.types.Operator):
    bl_idname = "object.simple_operator"
    bl_label = "Print an Encouraging Message"

    def execute(self, context):
        print("\n\n####################################################")
        print("# Add-on and Simple Operator executed succesfully!")
        print("# Encouraging Message:", context.scene.encouraging_message)
        print("# My Int:", context.scene.my_int_prop)
        print("# My Float:", context.scene.my_float_prop)
        print("# My Bool:", context.scene.my_bool_prop)
        print("# My Int Vector:", *context.scene.my_int_vector_prop)
        print("# My Float Vector:", *context.scene.my_float_vector_prop)
        print("# My Bool Vector:", *context.scene.my_bool_vector_prop)
        print("####################################################")
        return {'FINISHED'}

    @classmethod
    def register(cls):
        print("Registered class: %s " % cls.bl_label)

        bpy.types.Scene.encouraging_message = bpy.props.StringProperty(
            name="",
            description="Message to print to user",
            default="Have a nice day!")

        bpy.types.Scene.my_int_prop = bpy.props.IntProperty(
            name="My Int",
            description="Sample integer property to print to user",
            default=123,
            min=100,
            max=200)

        bpy.types.Scene.my_float_prop = bpy.props.FloatProperty(
            name="My Float",
            description="Sample float property to print to user",
            default=3.1415,
            min=0.0,
            max=10.0,
            precision=4)

        bpy.types.Scene.my_bool_prop = bpy.props.BoolProperty(
            name="My Bool",
            description="Sample boolean property to print to user",
            default=True)

        bpy.types.Scene.my_int_vector_prop = bpy.props.IntVectorProperty(
            name="My Int Vector",
            description="Sample integer vector property to print to user",
            default=(1, 2, 3, 4),
            subtype='NONE',
            size=4)

        bpy.types.Scene.my_float_vector_prop = bpy.props.FloatVectorProperty(
            name="My Float Vector",
            description="Sample float vector property to print to user",
            default=(1.23, 2.34, 3.45),
            subtype='XYZ',
            size=3,
            precision=2)

        bpy.types.Scene.my_bool_vector_prop = bpy.props.BoolVectorProperty(
            name="My Bool Vector",
            description="Sample bool vector property to print to user",
            default=(True, False, True),
            subtype='XYZ',
            size=3)

        bpy.types.Scene.my_color_prop = bpy.props.FloatVectorProperty(
            name="My Color Property",
            description="Returns a vector of length 4",
            default=(0.322, 1.0, 0.182, 1.0),
            min=0.0,
            max=1.0,
            subtype='COLOR',
            size=4)

    @classmethod
    def unregister(cls):
        print("Unregistered class: %s " % cls.bl_label)
        del bpy.types.Scene.encouraging_message


# Simple button in Tools panel
class SimplePanel(bpy.types.Panel):
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI" # 2.93 must be UI, otherwise cause RuntimeError
    bl_category = "Simple Add-on"
    bl_label = "Simple Add-on"
    bl_context = "objectmode"

    def draw(self, context):
        self.layout.operator("object.simple_operator",
                             text="Print Encouraging Message")
        self.layout.prop(context.scene, 'encouraging_message')
        self.layout.prop(context.scene, 'my_int_prop')
        self.layout.prop(context.scene, 'my_float_prop')
        self.layout.prop(context.scene, 'my_bool_prop')
        self.layout.prop(context.scene, 'my_int_vector_prop')
        self.layout.prop(context.scene, 'my_float_vector_prop')
        self.layout.prop(context.scene, 'my_bool_vector_prop')
        self.layout.prop(context.scene, 'my_color_prop')

    @classmethod
    def register(cls):
        print("Registered class: %s " % cls.bl_label)
        # Register properties related to the class here.

    @classmethod
    def unregister(cls):
        print("Unregistered class: %s " % cls.bl_label)

def register():

    print("%s registration start\n" % bl_info.get('name'))

    # Implicitly register objects inheriting bpy.types in current file and scope
    #bpy.utils.register_module(__name__)

    # Or explicitly register objects
    bpy.utils.register_class(SimpleOperator)
    bpy.utils.register_class(SimplePanel)

    print("%s registration complete\n" % bl_info.get('name'))


def unregister():

    # Always unregister in reverse order to prevent error due to
    # interdependencies
    print("%s unregister start\n" % bl_info.get('name'))

    # Explicity unregister objects
    bpy.utils.unregister_class(SimplePanel)
    bpy.utils.unregister_class(SimpleOperator)
    

    # Or unregister objects inheriting bpy.types in current file and scope
    # removed since 2.8
    # bpy.utils.unregister_module(__name__)
    print("%s unregister complete\n" % bl_info.get('name'))


# Only called during development with 'Text Editor -> Run Script'
# When distributed as plugin, Blender will directly
# and call register() and unregister()
if __name__ == "__main__":
    
    try:
        unregister()
    except Exception as e:
        # Catch failure to unregister explicity
        print(e)
        pass
    
    register()
