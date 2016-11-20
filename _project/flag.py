class Flag(object):
    def __init__(self, id, isNegated):
        self.id = id
        self.isNegated = isNegated
        self.value = False

    def setFlag(self, value):
        self.value = value

    def getFlag(self):
        if self.isNegated:
            return not self.value
        return self.value
