import bpy


__author__ = 'Andrew Kuchev (kuchevad@gmail.com)'


def _create_bpy_object_internal(f, context, name=None, parent=None, scale=None, hide=None, location=None):
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
    if hide is not None:
        context.object.hide = hide
    if location is not None:
        context.object.location = location

    return context.object


def create_bpy_object(context, name=None, parent=None, scale=None, hide=None, location=None):
    return _create_bpy_object_internal(bpy.ops.object.add, context, name=name, parent=parent, scale=scale, hide=hide,
                                       location=location)


def create_bpy_cylinder(context, name=None, parent=None, scale=None, hide=None, location=None):
    return _create_bpy_object_internal(bpy.ops.mesh.primitive_cylinder_add,
                                       context, name=name, parent=parent, scale=scale, hide=hide, location=location)

def create_bpy_plane(context, name=None, parent=None, scale=None, hide=None, location=None):
    return _create_bpy_object_internal(bpy.ops.mesh.primitive_plane_add,
                                       context, name=name, parent=parent, scale=scale, hide=hide, location=location)


def create_bpy_color(name, rgb, emit=None):
    color = bpy.data.materials.new(name)
    color.diffuse_color = rgb
    if emit is not None:
        color.emit = emit
    return color


def get_red_color():
    return get_or_create_color('Red', (1, 0, 0))


def get_green_color():
    return get_or_create_color('Green', (0, 1, 0))


def get_blue_color():
    return get_or_create_color('Blue', (0, 0, 1))


def get_or_create_color(name, rgb):
    if name in bpy.data.materials:
        return bpy.data.materials[name]
    return create_bpy_color(name, rgb)
