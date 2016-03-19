from ..core import LifContext


__author__ = 'Andrew Kuchev (kuchevad@gmail.com)'


class FountainModel:
    def __init__(self, fountain):
        self.fountain = fountain

    @property
    def nozzles_group(self):
        return next((n for n in self.fountain.children if n.name == LifContext.nozzles_group_name), None)

    @nozzles_group.setter
    def nozzles_group(self, value):
        value.name = 'Nozzles'
        value.parent = self.fountain

    @property
    def nozzles_list(self):
        nozzles_group = self.nozzles_group
        return None if nozzles_group is None else nozzles_group.children

    def is_valid(self):
        if self.nozzles_group is None:
            return False, '{nozzles} should be a child of {lif} object'.format(
                    nozzles=LifContext.nozzles_group_name, lif=LifContext.fountain_objects_group_name)

        return True, ''
