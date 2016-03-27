import bpy

from ..core import LifContext
from ..models import FountainModel


__author__ = 'Andrew Kuchev (kuchevad@gmail.com)'


class SoundEqualizer(bpy.types.Operator):
    bl_idname = "lif.sound_equalizer"
    bl_label = "LIF! Sound equalizer"

    def execute(self, context):
        fountain = FountainModel(LifContext.get_fountain(context))

        bars = len(fountain.nozzles_list)
        max_freq = 20000
        min_freq = 100

        h = 1

        base = (max_freq / min_freq) ** (1 / (bars - 1))

        area_type = bpy.context.area.type
        bpy.context.area.type = 'SEQUENCE_EDITOR'
        bpy.ops.sequencer.sound_strip_add(filepath='/home/soon/sound.mp3',
                                          files=[{'name': 'sound.mp3'}], relative_path=True, frame_start=1,
                                          channel=1)

        bpy.app.debug = True

        for c, nozzle_water in enumerate(map(LifContext.get_nozzle_water, fountain.nozzles_list)):
            l = h
            h = min_freq * base ** (c - 1)

            for o in context.selected_objects[:]:
                o.select = False
            nozzle_water.select = True
            context.scene.objects.active = nozzle_water

            bpy.ops.anim.keyframe_insert_menu(type='Scaling')
            LifContext.get_nozzle_water_material(nozzle_water).keyframe_insert('diffuse_color', 0) # R
            LifContext.get_nozzle_water_material(nozzle_water).keyframe_insert('diffuse_color', 1) # G

            bpy.context.active_object.animation_data.action.fcurves[0].lock = True
            bpy.context.active_object.animation_data.action.fcurves[1].lock = True

            bpy.context.area.type = 'GRAPH_EDITOR'

            bpy.ops.graph.sound_bake(filepath="/home/soon/sound.mp3", low=l, high=h,
                                     attack=0.001, release=0.7)

            bpy.context.active_object.animation_data.action.fcurves[2].lock = True




        bpy.context.area.type = area_type
        bpy.context.scene.frame_end = 14000

        return {'FINISHED'}
