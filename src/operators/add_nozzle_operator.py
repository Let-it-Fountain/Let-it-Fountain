import bpy

from ..core import LifContext
from ..models import FountainModel
from ..utils.bpy_helpers import create_bpy_object
from ..utils.optional import Optional


__author__ = 'Andrew Kuchev (kuchevad@gmail.com)'


class AddNozzleOperator(bpy.types.Operator):
    bl_idname = "lif.add_nozzle"
    bl_label = "Add nozzle"

    def create_nozzle(self, context, name=None, parent=None):
        return create_bpy_object(context, name=name, parent=parent)

    def execute(self, context):
        nozzles_group = (Optional(LifContext.get_fountain(context))
                         .map(FountainModel)
                         .map(lambda f: f.nozzles_group)
                         .or_else(None))
        if nozzles_group is not None:
            self.create_nozzle(context, name='Nozzle', parent=nozzles_group)

        return {'FINISHED'}
