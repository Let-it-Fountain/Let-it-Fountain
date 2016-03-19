import bpy

from ..core import LifContext
from ..utils.bpy_helpers import create_bpy_object


__author__ = 'Andrew Kuchev (kuchevad@gmail.com)'


class InitializeFountainOperator(bpy.types.Operator):
    bl_idname = "lif.initialize_fountain"
    bl_label = "Initialize fountain"

    def create_fountain(self, context):
        return create_bpy_object(context, name=LifContext.fountain_objects_group_name)

    def create_nozzles(self, fountain, context):
        nozzles = create_bpy_object(context, name=LifContext.nozzles_group_name, parent=fountain)
        return nozzles

    def execute(self, context):
        fountain = self.create_fountain(context)
        nozzles = self.create_nozzles(fountain, context)

        return {'FINISHED'}
