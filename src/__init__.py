import bpy

from .operators.sound_equalizer import SoundEqualizer
from .operators.add_nozzle_operator import AddNozzleOperator
from .operators.initialize_fountain_operator import InitializeFountainOperator
from .panels import LetItFountainPanel


bl_info = {
    "name": "Let it Fountain",
    "author": "Andrew Kuchev",
    "version": (0, 1),
    "blender": (2, 76, 0),
    "category": "Development",
    "location": "View3D > Tools",
    "description": "",
    "warning": "",
    "wiki_url": "",
    "tracker_url": "",
}


def register():
    bpy.utils.register_class(InitializeFountainOperator)
    bpy.utils.register_class(SoundEqualizer)
    bpy.utils.register_class(AddNozzleOperator)
    bpy.utils.register_class(LetItFountainPanel)


def unregister():
    bpy.utils.unregister_class(LetItFountainPanel)
    bpy.utils.unregister_class(AddNozzleOperator)
    bpy.utils.unregister_class(SoundEqualizer)
    bpy.utils.unregister_class(InitializeFountainOperator)


if __name__ == '__main__':
    register()
