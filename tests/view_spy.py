class ViewSpy:
    def __init__(self):
        self.sel_return = []
        self.first_insert_parameter = None
        self.second_insert_parameter = None
        self.third_insert_parameter = None

        self.substr_parameter = None
        self.substr_return_value = None

    def insert(self, edit, something, string_to_insert):
        self.first_insert_parameter = edit
        self.second_insert_parameter = something
        self.third_insert_parameter = string_to_insert

    def substr(self, region):
        self.substr_parameter = region

        return self.substr_return_value

    def sel(self):
        return self.sel_return
