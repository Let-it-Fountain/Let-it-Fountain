import bpy

from ..core import LifContext
from ..models import FountainModel


__author__ = 'Andrew Kuchev (kuchevad@gmail.com)'


class LetItFountainPanel(bpy.types.Panel):
    bl_label = 'Let it Fountain!'
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'TOOLS'
    bl_category = 'Let it Fountain!'

    def draw(self, context):
        fountain = self.get_fountain_model(context)

        if fountain is None:
            self.layout.label('Scene does not have a fountain. Consider create one')
            self.layout.operator('lif.initialize_fountain')
            return

        is_valid, error_message = fountain.is_valid()
        if not is_valid:
            self.layout.label('Fountain is in broken state')
            self.layout.label(error_message)
            return

        self.layout.label('Fountain found')
        print(fountain.nozzles_list)
        self.layout.label('Number of nozzles: {}'.format(len(fountain.nozzles_list)))
        self.layout.operator('lif.add_nozzle')

        if context.object not in fountain.nozzles_list:
            self.layout.label('Select a nozzle to change color or pressure')
            return

        self.layout.label('Selected nozzle: {}'.format(context.object.name))

        name_row = self.layout.row()
        name_row.prop(context.object, 'name', text="Name")

        color_row = self.layout.row()
        material = self.get_nozzle_water(context.object).data.materials[0]
        color_row.prop(material, "diffuse_color", text="Color")

    def get_nozzle_water(self, nozzle):
        return nozzle.children[0]

    def get_fountain_model(self, context):
        fountain = LifContext.get_fountain(context)
        return None if fountain is None else FountainModel(fountain)
