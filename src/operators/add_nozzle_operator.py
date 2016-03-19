import bpy

from ..core import LifContext
from ..models import FountainModel
from ..utils.bpy_helpers import create_bpy_cylinder, get_red_color, create_bpy_color
from ..utils.optional import Optional


__author__ = 'Andrew Kuchev (kuchevad@gmail.com)'


class AddNozzleOperator(bpy.types.Operator):
    bl_idname = "lif.add_nozzle"
    bl_label = "Add nozzle"

    def create_nozzle(self, context, name=None, parent=None):
        nozzle = create_bpy_cylinder(context, name=name, parent=parent, scale=[0.1, 0.1, 0.2])
        water = create_bpy_cylinder(context, name=LifContext.nozzle_water_part_name,
                                    parent=nozzle, scale=[0.9, 0.9, 1.1])
        bpy.ops.object.constraint_add(type='COPY_LOCATION')
        water.constraints['Copy Location'].target = nozzle
        water.constraints['Copy Location'].use_x = True
        water.constraints['Copy Location'].use_y = True
        water.constraints['Copy Location'].use_z = False
        water.data.materials.append(create_bpy_color(nozzle.name, (1, 0, 0)))
        return nozzle

    def execute(self, context):
        nozzles_group = (Optional(LifContext.get_fountain(context))
                         .map(FountainModel)
                         .map(lambda f: f.nozzles_group)
                         .or_else(None))
        if nozzles_group is not None:
            self.create_nozzle(context, name=LifContext.nozzle_name, parent=nozzles_group)

        return {'FINISHED'}
