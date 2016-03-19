import bpy

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
    bpy.utils.register_module(__name__)


def unregister():
    bpy.utils.register_module(__name__)


if __name__ == '__main__':
    register()
