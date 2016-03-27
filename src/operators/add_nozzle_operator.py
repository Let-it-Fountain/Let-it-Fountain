import bpy

from ..core import LifContext
from ..models import FountainModel
from ..utils.bpy_helpers import create_bpy_cylinder, create_bpy_color
from ..utils.optional import Optional


__author__ = 'Andrew Kuchev (kuchevad@gmail.com)'


class AddNozzleOperator(bpy.types.Operator):
    bl_idname = "lif.add_nozzle"
    bl_label = "Add nozzle"

    def create_nozzle(self, context, name=None, parent=None):
        nozzle = create_bpy_cylinder(context, name=name, parent=parent, scale=[0.1, 0.1, 3])
        bpy.context.scene.cursor_location = bpy.context.active_object.location
        bpy.context.active_object.location.z -= 2.9
        bpy.context.scene.cursor_location.z += 1
        water = create_bpy_cylinder(context, name=LifContext.nozzle_water_part_name,
                                    parent=nozzle, scale=[0.8, 0.8, 0.5])
        bpy.ops.object.constraint_add(type='COPY_LOCATION')
        water.constraints['Copy Location'].target = nozzle
        water.constraints['Copy Location'].use_x = True
        water.constraints['Copy Location'].use_y = True
        water.constraints['Copy Location'].use_z = False
        water.data.materials.append(create_bpy_color(nozzle.name, (0.1, 0.5, 1)))
        water.select = False
        nozzle.select = True
        bpy.context.scene.objects.active = nozzle
        bpy.context.scene.cursor_location = nozzle.location
        bpy.context.scene.cursor_location = (0, 0, 0)
        return nozzle

    def execute(self, context):
        nozzles_group = (Optional(LifContext.get_fountain(context))
                         .map(FountainModel)
                         .map(lambda f: f.nozzles_group)
                         .or_else(None))
        if nozzles_group is not None:
            self.create_nozzle(context, name=LifContext.nozzle_name, parent=nozzles_group)

        return {'FINISHED'}
