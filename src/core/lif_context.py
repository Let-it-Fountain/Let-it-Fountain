__author__ = 'Andrew Kuchev (kuchevad@gmail.com)'


class LifContext:
    fountain_objects_group_name = '_LIF'
    nozzles_group_name = 'Nozzles'

    @staticmethod
    def get_fountain(context):
        return context.scene.objects.get(LifContext.fountain_objects_group_name)
