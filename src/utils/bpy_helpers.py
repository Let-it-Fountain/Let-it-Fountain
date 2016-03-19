import bpy


__author__ = 'Andrew Kuchev (kuchevad@gmail.com)'


def _create_bpy_object_internal(f, context, name=None, parent=None, scale=None):
    """
    :param f: Creates new object. The result should be located in context.object
    :param context:
    :param name:
    :param parent:
    :return:
    """
    f()

    if parent is not None:
        context.object.parent = parent
    if name is not None:
        context.object.name = name
    if scale is not None:
        context.object.scale = scale

    return context.object


def create_bpy_object(context, name=None, parent=None, scale=None):
    return _create_bpy_object_internal(bpy.ops.object.add, context, name=name, parent=parent, scale=scale)


def create_bpy_cylinder(context, name=None, parent=None, scale=None):
    return _create_bpy_object_internal(bpy.ops.mesh.primitive_cylinder_add,
                                       context, name=name, parent=parent, scale=scale)
