import bpy


__author__ = 'Andrew Kuchev (kuchevad@gmail.com)'


def create_bpy_object(context, name=None, parent=None):
    bpy.ops.object.add()

    if parent is not None:
        context.object.parent = parent
    if name is not None:
        context.object.name = name

    return context.object
