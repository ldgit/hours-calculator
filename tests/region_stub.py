class RegionStub:
    def end(self):
        return 'dummy region end'

    def empty(self):
        return False


class EmptyRegionStub:
    def __init__(self):
        self.dummy_region_end = 'dummy region end'

    def end(self):
        return self.dummy_region_end

    def empty(self):
        return True
