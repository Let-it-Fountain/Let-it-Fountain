__author__ = 'Andrew Kuchev (kuchevad@gmail.com)'


class Optional:
    def __init__(self, value, nullable=False):
        self.value = value
        self.nullable = nullable

    def has_value(self):
        return bool(self.value is not None or self.nullable)

    def map(self, f):
        return Optional(f(self.value)) if self.has_value() else Optional.empty()

    def or_else(self, default_value):
        return self.value if self.has_value() else default_value

    @staticmethod
    def empty():
        return Optional(None)
