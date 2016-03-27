__author__ = 'Andrew Kuchev (kuchevad@gmail.com)'


class LifContext:
    fountain_objects_group_name = '_LIF'
    nozzles_group_name = 'Nozzles'
    nozzle_water_part_name = 'Water'
    nozzle_name = 'Nozzle'

    @staticmethod
    def get_fountain(context):
        return context.scene.objects.get(LifContext.fountain_objects_group_name)

    @staticmethod
    def get_nozzle_water(nozzle):
        return next(c for c in nozzle.children if LifContext.nozzle_water_part_name in  c.name)

    @staticmethod
    def get_nozzle_water_material(nozzle_water):
        return nozzle_water.data.materials[0]