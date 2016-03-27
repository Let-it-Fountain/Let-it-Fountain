import bpy

from ..core import LifContext
from ..utils.bpy_helpers import create_bpy_object, create_bpy_plane, create_bpy_color


__author__ = 'Andrew Kuchev (kuchevad@gmail.com)'


class InitializeFountainOperator(bpy.types.Operator):
    bl_idname = "lif.initialize_fountain"
    bl_label = "Initialize fountain"

    def create_fountain(self, context):
        return create_bpy_object(context, name=LifContext.fountain_objects_group_name, hide=True)

    def create_nozzles(self, fountain, context):
        nozzles = create_bpy_object(context, name=LifContext.nozzles_group_name, parent=fountain, hide=True)
        return nozzles

    def execute(self, context):
        plane = create_bpy_plane(context, location=(0, 0, -0.1), scale=(100, 100, 1))
        plane.data.materials.append(create_bpy_color('Plane color', (0.03, 0.03, 0.05)))
        fountain = self.create_fountain(context)
        nozzles = self.create_nozzles(fountain, context)

        # Awesome water lighting
        context.scene.world.light_settings.use_indirect_light = True
        context.scene.world.light_settings.gather_method = 'APPROXIMATE'
        context.scene.world.light_settings.indirect_bounces = 2

        if 'Lamp' in bpy.data.objects:
            bpy.data.objects['Lamp'].hide = True
            bpy.data.objects['Lamp'].hide_render = True

        return {'FINISHED'}
